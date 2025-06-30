# apps/documents/models.py

from django.db import models
from django.conf import settings # سنستخدمه لربط الوثيقة بالمستخدم

class Document(models.Model):
    """
    النموذج الرئيسي الذي يمثل أي وثيقة في النظام.
    """
    
    # تعريف الحالات المختلفة التي يمكن أن تمر بها الوثيقة
    STATUS_CHOICES = [
        ('DRAFT', 'مسودة'),
        ('IN_REVIEW', 'قيد المراجعة'),
        ('APPROVED', 'معتمدة'),
        ('ARCHIVED', 'مؤرشفة'),
    ]

    # --- معلومات أساسية عن الوثيقة ---
    title = models.CharField(max_length=255, verbose_name="عنوان الوثيقة")
    doc_id = models.CharField(max_length=50, unique=True, verbose_name="المعرّف الفريد للوثيقة")
    version = models.CharField(max_length=20, verbose_name="رقم الإصدار")
    
    # --- حالة الوثيقة ومحتواها ---
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='DRAFT', 
        verbose_name="حالة الوثيقة"
    )
    # FileField يسمح للمستخدم برفع ملف (مثل PDF أو Word)
    file = models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name="الملف المرفق")

    # --- الربط مع نماذج أخرى ---
    # ForeignKey هو علاقة "واحد-إلى-متعدد"، فالمستخدم الواحد يمكن أن يكون مؤلفًا لعدة وثائق
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, # نستخدم نموذج المستخدم الذي عرفناه في settings.py
        on_delete=models.PROTECT, # يمنع حذف مستخدم إذا كان مؤلفًا لوثيقة
        related_name='authored_documents',
        verbose_name="المؤلف"
    )
    
    # --- تواريخ مهمة ---
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ آخر تحديث")

    def __str__(self):
        # هذه الدالة تحدد كيف سيظهر اسم الوثيقة في لوحة التحكم (مثال: "SOP-001 - v1.0")
        return f"{self.doc_id} - v{self.version}"

    class Meta:
        verbose_name = "وثيقة"
        verbose_name_plural = "الوثائق"
        ordering = ['-created_at'] # ترتيب الوثائق من الأحدث إلى الأقدم