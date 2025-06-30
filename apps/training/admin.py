# apps/training/admin.py

from django.contrib import admin
from .models import Training, TrainingRecord

admin.site.register(Training)
admin.site.register(TrainingRecord)