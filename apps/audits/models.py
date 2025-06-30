# apps/audits/models.py

from django.db import models
from django.conf import settings

class Audit(models.Model):
    """
    يمثل عملية تدقيق واحدة، سواء كانت داخلية أو خارجية.
    """
    AUDIT_TYPE_CHOICES = [
        ('INTERNAL', 'تدقيق داخلي'),
        ('EXTERNAL', 'تدقيق خارجي'),
        ('SUPPLIER', 'تدقيق مورد'),
    ]

    STATUS_CHOICES = [
        ('PLANNED', 'مخطط له'),
        ('IN_PROGRESS', 'قيد التنفيذ'),
        ('COMPLETED', 'مكتمل'),
        ('CANCELLED', 'ملغى'),
    ]

    title = models.CharField(max_length=255, verbose_name="عنوان أو نطاق التدقيق")
    audit_type = models.CharField(max_length=50, choices=AUDIT_TYPE_CHOICES, verbose_name="نوع التدقيق")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PLANNED', verbose_name="حالة التدقيق")

    lead_auditor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        verbose_name="المدقق الرئيسي"
    )

    planned_start_date = models.DateField(verbose_name="تاريخ البدء المخطط له")
    planned_end_date = models.DateField(verbose_name="تاريخ الانتهاء المخطط له")
    actual_start_date = models.DateField(null=True, blank=True, verbose_name="تاريخ البدء الفعلي")
    actual_end_date = models.DateField(null=True, blank=True, verbose_name="تاريخ الانتهاء الفعلي")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تدقيق"
        verbose_name_plural = "عمليات التدقيق"


class Finding(models.Model):
    """
    يمثل ملاحظة أو نتيجة واحدة تم تسجيلها أثناء عملية تدقيق.
    """
    FINDING_TYPE_CHOICES = [
        ('OBSERVATION', 'ملاحظة'),
        ('MINOR_NC', 'عدم مطابقة صغرى'),
        ('MAJOR_NC', 'عدم مطابقة كبرى'),
    ]

    # كل ملاحظة تتبع لعملية تدقيق واحدة
    audit = models.ForeignKey(Audit, related_name='findings', on_delete=models.CASCADE, verbose_name="التدقيق التابع له")
    finding_type = models.CharField(max_length=50, choices=FINDING_TYPE_CHOICES, verbose_name="نوع الملاحظة")
    description = models.TextField(verbose_name="وصف الملاحظة")

    # لاحقًا، يمكننا إضافة حقل لفتح NCR من هذه الملاحظة
    # ncr = models.OneToOneField('quality_events.NonConformanceReport', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"ملاحظة رقم {self.id} في تدقيق: {self.audit.title}"

    class Meta:
        verbose_name = "ملاحظة تدقيق"
        verbose_name_plural = "ملاحظات التدقيق"