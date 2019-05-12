from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class UserRole(models.Model):
    user = models.OneToOneField(User,related_name="user_roles",on_delete=models.CASCADE)
    company = models.ForeignKey('Company', null=True,blank=True,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,related_name="userrole_group",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.group.name
    
    class Meta:
        db_table = 'userrole'