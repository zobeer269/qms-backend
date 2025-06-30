# apps/audits/urls.py

from django.urls import path
# 1. استيراد الـ Views الجديدة
from .views import (
    AuditListCreateView, 
    AuditDetailView,
    FindingListCreateView,
    FindingDetailView,
    CreateNCRFromFindingView,
)

urlpatterns = [
    # مسارات عمليات التدقيق (Audits)
    path('audits/', AuditListCreateView.as_view(), name='audit-list'),
    path('audits/<int:pk>/', AuditDetailView.as_view(), name='audit-detail'), # 2. المسار الجديد

    # مسارات الملاحظات (Findings)
    path('findings/', FindingListCreateView.as_view(), name='finding-list'),
    path('findings/<int:pk>/', FindingDetailView.as_view(), name='finding-detail'), # 3. المسار الجديد
    path('findings/<int:pk>/create-ncr/', CreateNCRFromFindingView.as_view(), name='finding-create-ncr')

]