# apps/audits/serializers.py

from rest_framework import serializers
from .models import Audit, Finding

class AuditSerializer(serializers.ModelSerializer):
    """
    Serializer لنموذج التدقيق (Audit).
    """
    # عرض اسم المدقق الرئيسي بدلاً من الـ ID
    lead_auditor_username = serializers.ReadOnlyField(source='lead_auditor.username')

    # عرض النص المقروء لحقول الاختيارات
    audit_type_display = serializers.CharField(source='get_audit_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Audit
        # تحديد الحقول التي ستظهر في الـ API
        fields = [
            'id', 
            'title', 
            'audit_type', 
            'audit_type_display',
            'status',
            'status_display',
            'lead_auditor_username',
            'planned_start_date',
            'planned_end_date',
            'actual_start_date',
            'actual_end_date',
        ]


class FindingSerializer(serializers.ModelSerializer):
    """
    Serializer لنموذج الملاحظات (Finding).
    """
    # عرض عنوان التدقيق التابعة له الملاحظة
    audit_title = serializers.ReadOnlyField(source='audit.title')

    # عرض النص المقروء لنوع الملاحظة
    finding_type_display = serializers.CharField(source='get_finding_type_display', read_only=True)

    class Meta:
        model = Finding
        fields = [
            'id',
            'audit', # نعرض رقم الـ ID للتدقيق لسهولة الربط
            'audit_title',
            'finding_type',
            'finding_type_display',
            'description',
        ]