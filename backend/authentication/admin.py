from django.contrib import admin
from .models import (
    User, Student, Parent, PasswordResetToken,
    ParentRegistration, StudentRegistration, ParentStudentMapping, StudentProfile,
    CoinTransaction, UserCoinBalance, StudentFeedback,
    UserBadge, UserStreak, DailyActivity, LeaderboardEntry,
    Teacher, TeacherLegacy, Class
)

# Register your models here
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'firstname', 'lastname', 'role', 'createdat')
    list_filter = ('role', 'createdat')
    search_fields = ('username', 'email', 'firstname', 'lastname')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_field', 'parent')
    list_filter = ('class_field',)

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('parent',)

@admin.register(TeacherLegacy)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'qualification', 'experience_years', 'specialization')
    list_filter = ('qualification', 'experience_years')

@admin.register(ParentRegistration)
class ParentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('parent_username', 'email', 'first_name', 'last_name', 'phone_number', 'created_at')
    search_fields = ('parent_username', 'email', 'first_name', 'last_name')

@admin.register(StudentRegistration)
class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('student_username', 'student_email', 'first_name', 'last_name', 'parent_email', 'created_at')
    search_fields = ('student_username', 'student_email', 'first_name', 'last_name')

@admin.register(Teacher)
class TeacherRegistrationAdmin(admin.ModelAdmin):
    list_display = ('teacher_username', 'teacher_email', 'first_name', 'last_name', 'qualification', 'experience_years')
    search_fields = ('teacher_username', 'teacher_email', 'first_name', 'last_name')

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_username', 'grade', 'school')
    search_fields = ('student_username', 'grade', 'school')

@admin.register(CoinTransaction)
class CoinTransactionAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'coins', 'transaction_type', 'source', 'created_at')
    list_filter = ('transaction_type', 'source', 'created_at')

@admin.register(UserCoinBalance)
class UserCoinBalanceAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'total_coins', 'total_earned', 'total_spent', 'last_transaction_at')

@admin.register(StudentFeedback)
class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'rating', 'coins_awarded', 'reward_received', 'created_at')
    list_filter = ('rating', 'reward_received')

@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'badge_type', 'badge_title', 'earned_at', 'is_active')
    list_filter = ('badge_type', 'is_active')

@admin.register(UserStreak)
class UserStreakAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'current_streak', 'longest_streak', 'last_activity_date', 'total_days_active')

@admin.register(DailyActivity)
class DailyActivityAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'activity_date', 'quizzes_completed', 'mock_tests_completed', 'coins_earned')
    list_filter = ('activity_date',)

@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'ranking_type', 'rank', 'score', 'calculated_at')
    list_filter = ('ranking_type', 'rank')

# Register other models
admin.site.register(ParentStudentMapping)
admin.site.register(PasswordResetToken)
admin.site.register(Class)
