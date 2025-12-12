from django.contrib import admin
from .models import Assignment, AssignmentSubmission, Attendance, Grade, StudentProgress

# Ultra-minimal admin
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
admin.site.register(Attendance)
admin.site.register(Grade)
admin.site.register(StudentProgress)
