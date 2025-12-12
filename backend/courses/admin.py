from django.contrib import admin
from .models import Course, CourseEnrollment, CourseMaterial

# Ultra-minimal admin - just register without custom config
admin.site.register(Course)
admin.site.register(CourseEnrollment)
admin.site.register(CourseMaterial)
