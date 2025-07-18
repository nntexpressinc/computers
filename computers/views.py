from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Computer
from .forms import LoginForm, ComputerForm
import json

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    computers = Computer.objects.all()
    return render(request, 'dashboard.html', {'computers': computers})

@login_required
def create_computer(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST, request.FILES)
        if form.is_valid():
            computer = form.save(commit=False)
            computer.created_by = request.user
            computer.save()
            messages.success(request, 'Kompyuter muvaffaqiyatli yaratildi!')
            return redirect('computer_detail', computer_id=computer.id)
    else:
        form = ComputerForm()
    return render(request, 'create_computer.html', {'form': form})

@login_required
def computer_detail(request, computer_id):
    computer = get_object_or_404(Computer, id=computer_id)
    qr_code = computer.generate_qr_code()
    return render(request, 'computer_detail.html', {
        'computer': computer,
        'qr_code': qr_code
    })

@login_required
def scanner_view(request):
    return render(request, 'scanner.html')

@login_required
def scan_qr_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            qr_data = data.get('qr_data', '')
            
            print(f"QR data received: {qr_data}")  # Debug uchun
            
            # QR koddan kompyuter ID sini olish
            if 'Computer ID:' in qr_data:
                computer_id = qr_data.split('Computer ID:')[1].split('\n')[0].strip()
                print(f"Computer ID extracted: {computer_id}")  # Debug uchun
                try:
                    computer = Computer.objects.get(id=int(computer_id))
                    print(f"Computer found: {computer.name} {computer.surname}")  # Debug uchun
                    return JsonResponse({
                        'success': True,
                        'computer': {
                            'id': computer.id,
                            'name': computer.name,
                            'surname': computer.surname,
                            'created_at': computer.created_at.strftime('%Y-%m-%d %H:%M'),
                            'image_url': computer.image.url if computer.image else None,
                            'signature': computer.signature
                        }
                    })
                except Computer.DoesNotExist:
                    print(f"Computer not found with ID: {computer_id}")  # Debug uchun
                    return JsonResponse({
                        'success': False,
                        'error': 'Kompyuter topilmadi'
                    })
                except ValueError:
                    print(f"Invalid computer ID: {computer_id}")  # Debug uchun
                    return JsonResponse({
                        'success': False,
                        'error': 'Noto\'g\'ri kompyuter ID formati'
                    })
            else:
                print(f"QR code format invalid: {qr_data}")  # Debug uchun
                return JsonResponse({
                    'success': False,
                    'error': f'Noto\'g\'ri QR kod formati. QR kod: {qr_data[:100]}...'
                })
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")  # Debug uchun
            return JsonResponse({
                'success': False,
                'error': 'JSON format xatosi'
            })
        except Exception as e:
            print(f"General error: {e}")  # Debug uchun
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Faqat POST so\'rovlar qabul qilinadi'})

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})