# apps/quality_events/urls.py

from django.urls import path
# 1. استيراد الـ View الجديد
from .views import NonConformanceReportListView, NonConformanceReportDetailView

urlpatterns = [
    path('', NonConformanceReportListView.as_view(), name='ncr-list'),
    # 2. إضافة المسار الجديد للتعامل مع تقرير واحد بواسطة رقمه (pk)
    path('<int:pk>/', NonConformanceReportDetailView.as_view(), name='ncr-detail'),
]