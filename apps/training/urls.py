# apps/training/urls.py
from django.urls import path
from .views import (
    TrainingListCreateView, TrainingDetailView,
    TrainingRecordListCreateView, TrainingRecordDetailView
)

urlpatterns = [
    path('courses/', TrainingListCreateView.as_view(), name='training-course-list'),
    path('courses/<int:pk>/', TrainingDetailView.as_view(), name='training-course-detail'),
    path('records/', TrainingRecordListCreateView.as_view(), name='training-record-list'),
    path('records/<int:pk>/', TrainingRecordDetailView.as_view(), name='training-record-detail'),
]