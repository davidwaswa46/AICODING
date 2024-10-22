from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Allcourses(models.Model):
    coursename=models.CharField(max_length=200)
    insname=models.CharField(max_length=100)
    startedfrom=models.DateTimeField('Started from')
    def __str__(self):#whenever creating a function within a class you will have to specify the self parameter which is compulsory in python unlike java
         return self.coursename 
    
    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.startedfrom <=now
    
        
class details(models.Model):
    #foreign key method is used to connect this subclass to the main class
    #on_delete function is used in case I delete any courses present in Allcourses section I want to delete the details of that function as well
    course=models.ForeignKey(Allcourses, on_delete=models.CASCADE)#inhariting All courses method
    ct=models.CharField(max_length=500)
    your_choice=models.BooleanField(default=False)
    def __str__(self):
         return str(self.ct)



