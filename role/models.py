from django.db import models
from django.conf import settings
# Create your models here.
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class UserRole(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="role",on_delete=models.CASCADE)
    company = models.ForeignKey('account.Company',related_name="roles", null=True,blank=True,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,related_name="roles",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.group.name
    
    class Meta:
        db_table = 'userrole'