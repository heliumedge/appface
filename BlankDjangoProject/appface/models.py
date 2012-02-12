from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User 

# Create your models here.
class Appface(models.Model):
    description = models.TextField()
    icon = models.ImageField(upload_to="/appIcons")
    submission_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, related_name='creator')
    attendees = models.ManyToManyField(User, through="Attendance")
        
    def __unicode__(self):
        return self.icon
    
class Attendance(models.Model):
    user= models.ForeignKey(User)
    app = models.ForeignKey(Appface)
    adhesion_date = models.DateField(default=datetime.now)
    notification_count = models.IntegerField()
    
class Notification_Group(models.Model):
    member=models.ManyToManyRel(User)
    name= models.TextField()

class Notification(models.Model):
    message=models.TextField()
    author =models.ForeignKey(User,related_name="Author")
    notification_group = models.ForeignKey(Notification_Group)
    message_type=models.TextField()
    
        
    
    
    
    
    
    