# apps/quality_events/permissions.py

from rest_framework import permissions

class IsReporterOrReadOnly(permissions.BasePermission):
    """
    صلاحية مخصصة للسماح لصاحب البلاغ فقط بتعديل التقرير.
    """
    def has_object_permission(self, request, view, obj):
        # نسمح دائمًا بطلبات القراءة الآمنة (GET)
        if request.method in permissions.SAFE_METHODS:
            return True

        # نسمح بطلبات الكتابة (PUT, DELETE) فقط إذا كان المستخدم هو صاحب البلاغ
        return obj.reported_by == request.user