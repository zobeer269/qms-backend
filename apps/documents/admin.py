# apps/documents/admin.py

from django.contrib import admin
from .models import Document # 1. نستورد نموذج "الوثيقة" الذي أنشأناه

# 2. نسجل النموذج هنا ليظهر في لوحة التحكم
admin.site.register(Document)