import segno
import base64
from django.shortcuts import render, redirect
from io import BytesIO
from .models import Penerima

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            # Look for a user with the provided email
            user = Penerima.objects.get(email=email)

            # Verify the password manually (since you're not using Django auth)
            if user.password == password:  # Replace with proper hashing if passwords are hashed
                # Create a session for the user
                request.session['user_id'] = user.id  # Store the user ID in the session
                request.session['user_name'] = user.name  # Optionally store other details
                request.session['user_email'] = user.email  # Optionally store other details

                # Generate QR code containing user's email and name
                qr_data = f"Email: {user.email}\nName: {user.name}"
                
                # Create QR code using segno
                qr = segno.make(qr_data)

                # Save the QR code to a BytesIO object (can be displayed directly in the template)
                qr_stream = BytesIO()
                qr.save(qr_stream, kind='png')  # You can specify other formats like 'svg' if needed
                qr_stream.seek(0)

                # Convert the image to base64 for embedding in HTML
                qr_base64 = base64.b64encode(qr_stream.getvalue()).decode('utf-8')

                # Send the base64 QR code to the template
                return render(request, "home.html", {
                    "qr_code": qr_base64,
                    "user": user,  # Pass the user to the template as well
                })
            else:
                # Incorrect password
                raise Penerima.DoesNotExist
        except Penerima.DoesNotExist:
            print("gagal")
            # Authentication failed
            return render(request, "login.html", {
                "error_message": "Invalid email or password."
            })

    return render(request, "login.html")
