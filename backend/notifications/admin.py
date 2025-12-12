from django.contrib import admin
from .models import Announcement, Event, Feedback, Message, Notification

# Ultra-minimal admin
admin.site.register(Announcement)
admin.site.register(Event)
admin.site.register(Feedback)
admin.site.register(Message)
admin.site.register(Notification)
