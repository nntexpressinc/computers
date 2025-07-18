from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-computer/', views.create_computer, name='create_computer'),
    path('computer/<int:computer_id>/', views.computer_detail, name='computer_detail'),
    path('scanner/', views.scanner_view, name='scanner'),
    path('scan-qr/', views.scan_qr_code, name='scan_qr_code'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]