# apps/training/views.py
from rest_framework import generics, permissions
from .models import Training, TrainingRecord
from .serializers import TrainingSerializer, TrainingRecordSerializer

# --- Views for Trainings (Admin only) ---
class TrainingListCreateView(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = [permissions.IsAdminUser]

class TrainingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = [permissions.IsAdminUser]

# --- Views for Training Records ---
class TrainingRecordListCreateView(generics.ListCreateAPIView):
    serializer_class = TrainingRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = TrainingRecord.objects.all()

        # --- هذا هو الجزء الجديد ---
        # فلترة حسب التدريب إذا تم توفيره في عنوان URL
        training_id = self.request.query_params.get('training')
        if training_id is not None:
            return queryset.filter(training_id=training_id)
        # --------------------------

        # فلترة حسب المتدرب إذا لم يكن مديرًا
        if user.is_staff:
            return queryset
        return queryset.filter(trainee=user)

    def perform_create(self, serializer):
        serializer.save()

class TrainingRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrainingRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return TrainingRecord.objects.all()
        return TrainingRecord.objects.filter(trainee=user)