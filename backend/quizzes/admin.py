from django.contrib import admin
from .models import Quiz, Question, QuizAttempt, QuizAnswer

# Ultra-minimal admin
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuizAttempt)
admin.site.register(QuizAnswer)
