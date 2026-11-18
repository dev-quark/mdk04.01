from django.contrib import admin
from .models import Attendance, Group, Lesson, Mark, Student, Subject

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin): 
    list_display = ("name", "curator"); 
    search_fields = ("name",)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin): 
    list_display = ("full_name", "group", "active"); 
    list_filter = ("group", "active"); search_fields = ("full_name",)
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin): 
    list_display = ("name", "teacher"); 
    search_fields = ("name",)
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin): 
    list_display = ("date", "group", "subject", "topic"); 
    list_filter = ("group", "subject", "date"); search_fields = ("topic",)
@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin): 
    list_display = ("student", "lesson", "value"); 
    list_filter = ("value",); search_fields = ("student__full_name",)
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin): 
    list_display = ("student", "lesson", "present"); 
    list_filter = ("present",)
