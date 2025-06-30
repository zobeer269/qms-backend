# apps/users/views.py

from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer
from .models import User # 1. استيراد نموذج المستخدم

# ... كلاس UserRegistrationView يبقى كما هو ...
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


# 2. أضفنا هذا الكلاس الجديد
class CurrentUserView(generics.RetrieveAPIView):
    """
    View لجلب بيانات المستخدم المسجل دخوله حاليًا.
    """
    # نستخدم نفس الـ Serializer الخاص بالتسجيل ولكن يمكن إنشاء واحد مخصص لاحقًا
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    # نعيد تعريف هذه الدالة لتخبر الـ View بأن "الكائن" الذي يجب إرجاعه
    # هو ببساطة المستخدم المرتبط بالطلب الحالي (request.user)
    def get_object(self):
        return self.request.user