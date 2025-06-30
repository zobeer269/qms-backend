"""
URL configuration for qms_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include # 1. تأكد من إضافة include هنا

urlpatterns = [
    path('admin/', admin.site.urls),

    # 2. قم بتوجيه أي طلب يبدأ بـ api/users/ إلى ملف العناوين الخاص بتطبيق users
    path('api/users/', include('apps.users.urls')),

    # 3. أضف هذا السطر الجديد لتوجيه طلبات الوثائق
    path('api/documents/', include('apps.documents.urls')),
    path('api/quality-events/', include('apps.quality_events.urls')),
    path('api/auditing/', include('apps.audits.urls')),


]