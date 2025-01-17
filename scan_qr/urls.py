from django.urls import path
from .views import *

app_name='scan_qr'

urlpatterns = [
    path('', scan_qr_view, name='scan_qr'),
    path('process-qr-data/', process_qr_data, name='process_qr_data'),
    path('detail/<int:id>/', detail_view, name='detail_view'),

]
