# apps/documents/urls.py

from django.urls import path
from .views import DocumentListView, DocumentDetailView

urlpatterns = [
    # عنوان لعرض قائمة كل الوثائق
    path('', DocumentListView.as_view(), name='document-list'),
    # عنوان لعرض وثيقة واحدة حسب رقمها التعريفي (pk)
    path('<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
]