# apps/documents/views.py

from rest_framework import generics, permissions
from .models import Document
from .serializers import DocumentSerializer
from .permissions import IsAuthorOrReadOnly # 1. استيراد الحارس المخصص

class DocumentListView(generics.ListCreateAPIView):
    # ... (هذا الكلاس يبقى كما هو بدون تغيير) ...
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# 2. تم تغيير RetrieveAPIView إلى RetrieveUpdateDestroyAPIView
class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View لعرض أو تعديل أو حذف وثيقة واحدة.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    # 3. تم تغيير الصلاحية لاستخدام الحارس المخصص
    permission_classes = [IsAuthorOrReadOnly]