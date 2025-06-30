# apps/users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    نموذج المستخدم المخصص.
    يرث كل شيء من نموذج المستخدم الافتراضي في Django،
    ولكنه يسمح لنا بإضافة حقول مخصصة في المستقبل.
    """
    
    # يمكننا إضافة أي حقول مخصصة نريدها هنا في المستقبل.
    # على سبيل المثال، إذا أردنا إضافة منصب وظيفي:
    # job_title = models.CharField(max_length=100, blank=True)
    
    pass