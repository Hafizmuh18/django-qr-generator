from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

# In-memory data store for demo purposes (replace with your database logic)
QR_DATA_STORE = {}

def scan_qr_view(request):
    """
    Renders the QR Code scanner page.
    """
    return render(request, 'qr_scan.html')

def process_qr_data(request):
    """
    Handles the QR code data sent via POST and stores it.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        qr_data = data.get('qrData', '')

        # Store the QR data (you can replace this with database logic)
        new_id = len(QR_DATA_STORE) + 1
        QR_DATA_STORE[new_id] = qr_data

        # Return the ID of the stored data
        return JsonResponse({'id': new_id})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def detail_view(request, id):
    """
    Displays the details of the scanned QR code.
    """
    qr_data = QR_DATA_STORE.get(int(id), "QR data not found.")  # Replace with database query if needed
    return render(request, 'detail.html', {'qr_data': qr_data})
