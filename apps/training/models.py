# apps/training/models.py

from django.db import models
from django.conf import settings
from apps.documents.models import Document

class Training(models.Model):
    """
    يمثل دورة تدريبية أو متطلبًا تدريبيًا واحدًا.
    """
    title = models.CharField(max_length=255, verbose_name="عنوان التدريب")
    description = models.TextField(blank=True, verbose_name="وصف التدريب")

    # يمكن ربط التدريب مباشرة بوثيقة معينة
    related_document = models.ForeignKey(
        Document, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        verbose_name="الوثيقة التدريبية"
    )

    creation_date = models.DateField(auto_now_add=True, verbose_name="تاريخ إنشاء التدريب")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تدريب"
        verbose_name_plural = "التدريبات"

class TrainingRecord(models.Model):
    """
    يمثل سجل تدريب لموظف واحد على تدريب معين.
    """
    STATUS_CHOICES = [
        ('ASSIGNED', 'معين'),
        ('IN_PROGRESS', 'قيد الإنجاز'),
        ('COMPLETED', 'مكتمل'),
        ('OVERDUE', 'متأخر'),
    ]

    # الربط مع الموظف والتدريب
    trainee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="المتدرب")
    training = models.ForeignKey(Training, on_delete=models.CASCADE, verbose_name="التدريب")

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='ASSIGNED', verbose_name="حالة التدريب")

    assigned_date = models.DateField(auto_now_add=True, verbose_name="تاريخ التعيين")
    due_date = models.DateField(verbose_name="تاريخ الاستحقاق")
    completion_date = models.DateField(null=True, blank=True, verbose_name="تاريخ الإكمال")

    evidence = models.FileField(upload_to='training_evidence/', blank=True, null=True, verbose_name="إثبات الإكمال")

    def __str__(self):
        return f"{self.trainee.username} - {self.training.title}"

    class Meta:
        verbose_name = "سجل تدريبي"
        verbose_name_plural = "السجلات التدريبية"
        # نضمن عدم تعيين نفس التدريب لنفس الموظف مرتين
        unique_together = ('trainee', 'training')