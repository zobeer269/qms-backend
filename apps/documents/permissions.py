# apps/documents/permissions.py

from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    صلاحية مخصصة للسماح لمؤلفي الوثيقة فقط بتعديلها.
    يتم السماح بالقراءة للجميع (المستخدمين المسجلين).
    """

    def has_object_permission(self, request, view, obj):
        # يتم السماح بطلبات القراءة (GET, HEAD, OPTIONS) للجميع
        if request.method in permissions.SAFE_METHODS:
            return True

        # يتم السماح بطلبات الكتابة (PUT, DELETE) فقط إذا كان المستخدم هو مؤلف الوثيقة
        return obj.author == request.user