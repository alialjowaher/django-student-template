from django.db import models

# Create your models here.


class Course(models.Model):
    class courseType(models.TextChoices):
        UNDERGRADUATE = 'UG'
        GRADUATE = 'GR',
    # my_key = models.BigAutoField(primary_key=True)  how to define primary key 
    name = models.CharField(max_length=200,blank=False,null=False)
    credit = models.IntegerField()
    type = models.CharField(max_length=30,choices=courseType.choices,default=courseType.UNDERGRADUATE)
    created_at = models.DateTimeField(auto_now_add=True)
    major = models.ForeignKey('Major', on_delete=models.CASCADE, related_name='courses', null=True, blank=True)
    


class Major(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name