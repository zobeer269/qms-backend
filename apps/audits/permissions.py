# apps/audits/permissions.py

from rest_framework import permissions

class IsLeadAuditorOrReadOnly(permissions.BasePermission):
    """
    يسمح للمدقق الرئيسي فقط بتعديل أو حذف سجل التدقيق.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.lead_auditor == request.user

class IsParentAuditLeadAuditorOrReadOnly(permissions.BasePermission):
    """
    يسمح للمدقق الرئيسي للتدقيق الأب فقط بتعديل أو حذف الملاحظة.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # نتحقق من المستخدم عبر العلاقة مع التدقيق الأب
        return obj.audit.lead_auditor == request.user