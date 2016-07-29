from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        # when you visit the object of Employee it will return _unicode_ 's return
        return self.name

class Girl(models.Model):
    name = models.CharField(max_length=20)
    name='san'
    def __unicode__(self):
            # when you visit the object of Employee it will return _unicode_ 's return
            return self.name