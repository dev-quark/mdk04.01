from rest_framework import serializers
from .models import Attendance, Group, Lesson, Mark, Student, Subject

class GroupSerializer(serializers.ModelSerializer):
    class Meta: model = Group; fields = "__all__"
class StudentSerializer(serializers.ModelSerializer):
    class Meta: model = Student; fields = "__all__"
class SubjectSerializer(serializers.ModelSerializer):
    class Meta: model = Subject; fields = "__all__"
class LessonSerializer(serializers.ModelSerializer):
    class Meta: model = Lesson; fields = "__all__"
class MarkSerializer(serializers.ModelSerializer):
    class Meta: model = Mark; fields = "__all__"
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta: model = Attendance; fields = "__all__"
