from django.conf.urls import include
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path("", include("user_site.urls", namespace="user_site")),
    path("scan/", include("scan_qr.urls", namespace="scan_qr")),
    path("qr-code-demo/", include("qr_code_demo.urls", namespace="qr_code_demo")),
    path("qr-code/", include("qr_code.urls", namespace="qr_code")),
]
