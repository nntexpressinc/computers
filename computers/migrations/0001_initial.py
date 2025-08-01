# Generated by Django 5.2.4 on 2025-07-18 16:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ism')),
                ('surname', models.CharField(max_length=100, verbose_name='Familya')),
                ('image', models.ImageField(blank=True, null=True, upload_to='computer_images/', verbose_name='Rasm')),
                ('signature', models.TextField(blank=True, null=True, verbose_name='Imzo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqt')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kim yaratgan')),
            ],
            options={
                'verbose_name': 'Kompyuter',
                'verbose_name_plural': 'Kompyuterlar',
                'ordering': ['-created_at'],
            },
        ),
    ]
