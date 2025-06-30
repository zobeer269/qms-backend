# apps/quality_events/views.py

from rest_framework import generics, permissions
from .models import NonConformanceReport
from .serializers import NonConformanceReportSerializer
from .permissions import IsReporterOrReadOnly # 1. استيراد الحارس الجديد

class NonConformanceReportListView(generics.ListCreateAPIView):
    # ... (هذا الكلاس يبقى كما هو بدون تغيير) ...
    queryset = NonConformanceReport.objects.all()
    serializer_class = NonConformanceReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)

# 2. أضفنا هذا الكلاس الجديد
class NonConformanceReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View لعرض أو تعديل أو حذف تقرير عدم مطابقة واحد.
    """
    queryset = NonConformanceReport.objects.all()
    serializer_class = NonConformanceReportSerializer
    # 3. نستخدم الحارس المخصص هنا
    permission_classes = [IsReporterOrReadOnly]