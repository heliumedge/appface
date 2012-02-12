from django.contrib import admin
from appface.models import Appface, Attendance, Notification , Notification_Group

admin.site.register(Appface)
admin.site.register(Attendance)
admin.site.register(Notification_Group)
admin.site.register(Notification)