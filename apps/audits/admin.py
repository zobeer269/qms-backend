# apps/audits/admin.py

from django.contrib import admin
from .models import Audit, Finding # 1. نستورد كلا النموذجين

# 2. نسجل كل نموذج على حدة
admin.site.register(Audit)
admin.site.register(Finding)