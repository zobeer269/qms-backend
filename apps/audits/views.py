# apps/audits/views.py

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response # <-- هذا هو الاستيراد الصحيح لـ Response
from .models import Audit, Finding
from .serializers import AuditSerializer, FindingSerializer
from .permissions import IsLeadAuditorOrReadOnly, IsParentAuditLeadAuditorOrReadOnly
from apps.quality_events.models import NonConformanceReport

# --- Views for Audits ---

class AuditListCreateView(generics.ListCreateAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(lead_auditor=self.request.user)

class AuditDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = [IsLeadAuditorOrReadOnly]


# --- Views for Findings ---

class FindingListCreateView(generics.ListCreateAPIView):
    serializer_class = FindingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        يقوم بفلترة الملاحظات بناءً على 'audit' query parameter
        (e.g., /api/auditing/findings/?audit=1)
        """
        queryset = Finding.objects.all()
        audit_id = self.request.query_params.get('audit')
        if audit_id is not None:
            queryset = queryset.filter(audit_id=audit_id)
        return queryset

class FindingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    permission_classes = [IsParentAuditLeadAuditorOrReadOnly]


# --- View للإجراء المخصص ---
class CreateNCRFromFindingView(APIView):
    """
    API View مخصص لإنشاء NCR من Finding موجود.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        try:
            finding = Finding.objects.get(pk=pk)
            new_ncr = NonConformanceReport.objects.create(
                title=f"NCR from Finding: {finding.id}",
                description=finding.description,
                source=finding.audit.audit_type,
                reported_by=request.user
            )
            return Response(
                {'message': 'NCR created successfully', 'ncr_id': new_ncr.id}, 
                status=status.HTTP_201_CREATED
            )
        except Finding.DoesNotExist:
            return Response({'error': 'Finding not found'}, status=status.HTTP_404_NOT_FOUND)