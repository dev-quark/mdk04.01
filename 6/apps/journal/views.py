from rest_framework import viewsets
from .models import Attendance, Group, Lesson, Mark, Student, Subject
from .serializers import AttendanceSerializer, GroupSerializer, LessonSerializer, MarkSerializer, StudentSerializer, SubjectSerializer

class GroupViewSet(viewsets.ModelViewSet): queryset = Group.objects.all(); serializer_class = GroupSerializer; search_fields = ("name",)
class StudentViewSet(viewsets.ModelViewSet): queryset = Student.objects.select_related("group"); serializer_class = StudentSerializer; filterset_fields = ("group", "active"); search_fields = ("full_name",)
class SubjectViewSet(viewsets.ModelViewSet): queryset = Subject.objects.all(); serializer_class = SubjectSerializer; search_fields = ("name",)
class LessonViewSet(viewsets.ModelViewSet): queryset = Lesson.objects.select_related("group", "subject"); serializer_class = LessonSerializer; filterset_fields = ("group", "subject", "date")
class MarkViewSet(viewsets.ModelViewSet): queryset = Mark.objects.select_related("student", "lesson"); serializer_class = MarkSerializer; filterset_fields = ("student", "lesson", "value")
class AttendanceViewSet(viewsets.ModelViewSet): queryset = Attendance.objects.select_related("student", "lesson"); serializer_class = AttendanceSerializer; filterset_fields = ("student", "lesson", "present")
