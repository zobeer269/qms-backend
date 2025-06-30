# apps/quality_events/serializers.py

from rest_framework import serializers
from .models import NonConformanceReport

class NonConformanceReportSerializer(serializers.ModelSerializer):
    """
    يقوم بتحويل بيانات تقرير عدم المطابقة إلى صيغة JSON.
    """
    # لجعل الـ API أكثر فائدة، سنعرض أسماء الحقول المرتبطة بدلاً من أرقام ID فقط
    reported_by_username = serializers.ReadOnlyField(source='reported_by.username')

    # لعرض عنوان الوثيقة المرتبطة بدلاً من رقمها
    related_document_title = serializers.ReadOnlyField(source='related_document.title', allow_null=True)

    # لعرض النص المقروء لحقول الاختيارات (choices)
    source_display = serializers.CharField(source='get_source_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = NonConformanceReport
        # نحدد هنا الحقول التي نريد أن تظهر في الـ API
        fields = [
            'id',
            'title',
            'description',
            'source',          # القيمة الداخلية (e.g., 'INTERNAL_AUDIT')
            'source_display',  # القيمة المقروءة (e.g., 'تدقيق داخلي')
            'status',
            'status_display',
            'reported_by_username',
            'related_document_title',
            'reported_at',
        ]