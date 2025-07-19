from django.db import models
from django.contrib.auth.models import User
import qrcode
import io
import base64

class Computer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    surname = models.CharField(max_length=100, verbose_name="Familya")
    monitors_count = models.PositiveIntegerField(default=1, verbose_name="Monitorlar soni")
    computers_count = models.PositiveIntegerField(default=1, verbose_name="Kompyuterlar soni")
    keyboards_count = models.PositiveIntegerField(default=1, verbose_name="Klaviaturalar soni")
    mice_count = models.PositiveIntegerField(default=1, verbose_name="Sichqonchalar soni")
    image = models.ImageField(upload_to='computer_images/', verbose_name="Rasm", null=True, blank=True)
    signature = models.TextField(verbose_name="Imzo", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Kim yaratgan")
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def generate_qr_code(self):
        """QR kod generatsiya qilish"""
        qr_data = f"Computer ID: {self.id}\nName: {self.name} {self.surname}\nMonitors: {self.monitors_count}\nComputers: {self.computers_count}\nKeyboards: {self.keyboards_count}\nMice: {self.mice_count}\nCreated: {self.created_at.strftime('%Y-%m-%d %H:%M')}"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Base64 ga o'girish
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        return f"data:image/png;base64,{img_str}"
    
    class Meta:
        verbose_name = "Kompyuter"
        verbose_name_plural = "Kompyuterlar"
        ordering = ['-created_at']