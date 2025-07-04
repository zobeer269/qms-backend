# Generated by Django 5.2.3 on 2025-06-22 11:09

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
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان الوثيقة')),
                ('doc_id', models.CharField(max_length=50, unique=True, verbose_name='المعرّف الفريد للوثيقة')),
                ('version', models.CharField(max_length=20, verbose_name='رقم الإصدار')),
                ('status', models.CharField(choices=[('DRAFT', 'مسودة'), ('IN_REVIEW', 'قيد المراجعة'), ('APPROVED', 'معتمدة'), ('ARCHIVED', 'مؤرشفة')], default='DRAFT', max_length=20, verbose_name='حالة الوثيقة')),
                ('file', models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name='الملف المرفق')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ آخر تحديث')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='authored_documents', to=settings.AUTH_USER_MODEL, verbose_name='المؤلف')),
            ],
            options={
                'verbose_name': 'وثيقة',
                'verbose_name_plural': 'الوثائق',
                'ordering': ['-created_at'],
            },
        ),
    ]
