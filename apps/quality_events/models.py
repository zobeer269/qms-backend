# apps/quality_events/models.py

from django.db import models
from django.conf import settings
from apps.documents.models import Document # سنربط التقرير بالوثائق

class NonConformanceReport(models.Model):
    """
    يمثل تقرير عدم مطابقة (NCR).
    """
    SOURCE_CHOICES = [
        ('INTERNAL_AUDIT', 'تدقيق داخلي'),
        ('EXTERNAL_AUDIT', 'تدقيق خارجي'),
        ('CUSTOMER_COMPLAINT', 'شكوى عميل'),
        ('INTERNAL_TEST', 'فحص داخلي'),
        ('OTHER', 'مصدر آخر'),
    ]

    STATUS_CHOICES = [
        ('OPEN', 'مفتوح'),
        ('UNDER_INVESTIGATION', 'قيد التحقيق'),
        ('CAPA_OPEN', 'إجراء تصحيحي مفتوح'),
        ('CLOSED', 'مغلق'),
    ]

    title = models.CharField(max_length=255, verbose_name="عنوان عدم المطابقة")
    description = models.TextField(verbose_name="وصف تفصيلي للمشكلة")
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, verbose_name="مصدر التقرير")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='OPEN', verbose_name="حالة التقرير")

    # الربط مع النماذج الأخرى
    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        verbose_name="صاحب البلاغ"
    )
    # يمكن ربط التقرير بوثيقة معينة (مثل SOP) ولكن هذا الربط اختياري
    related_document = models.ForeignKey(
        Document, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="الوثيقة ذات الصلة"
    )

    reported_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإبلاغ")

    def __str__(self):
        return f"NCR-{self.id}: {self.title}"

    class Meta:
        verbose_name = "تقرير عدم مطابقة"
        verbose_name_plural = "تقارير عدم المطابقة"
        ordering = ['-reported_at']