# apps/quality_events/admin.py

from django.contrib import admin
from .models import NonConformanceReport # 1. نستورد نموذج التقرير

# 2. نسجل النموذج ليظهر في لوحة التحكم
admin.site.register(NonConformanceReport)