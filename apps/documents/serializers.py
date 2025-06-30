# apps/documents/serializers.py

from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    """
    يقوم بتحويل بيانات نموذج الوثيقة إلى صيغة JSON والعكس.
    """
    # افتراضيًا، حقل المؤلف سيُظهر رقمه فقط (e.g., 1).
    # السطر التالي يجعله يظهر اسم المستخدم بدلاً من الرقم، وهو أفضل بكثير.
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Document
        # نحدد هنا الحقول التي نريد أن تظهر في الـ API
        fields = [
            'id', 
            'title', 
            'doc_id', 
            'version', 
            'status', 
            'file', 
            'author_username', # نستخدم الحقل المحسّن الذي عرفناه في الأعلى
            'created_at',
        ]