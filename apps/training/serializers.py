# apps/training/serializers.py
from rest_framework import serializers
from .models import Training, TrainingRecord

class TrainingSerializer(serializers.ModelSerializer):
    related_document_title = serializers.ReadOnlyField(source='related_document.title', allow_null=True)

    class Meta:
        model = Training
        fields = '__all__' # سنأخذ كل الحقول

class TrainingRecordSerializer(serializers.ModelSerializer):
    trainee_username = serializers.ReadOnlyField(source='trainee.username')
    training_title = serializers.ReadOnlyField(source='training.title')
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = TrainingRecord
        fields = '__all__'