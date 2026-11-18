from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Group(models.Model):
    name = models.CharField("Название группы", max_length=50, unique=True)
    curator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Куратор")
    def __str__(self): return self.name
    class Meta: verbose_name = "Группа"; verbose_name_plural = "Группы"

class Student(models.Model):
    full_name = models.CharField("ФИО", max_length=150)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="students", verbose_name="Группа")
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Телефон", max_length=30, blank=True)
    active = models.BooleanField("Обучается", default=True)
    def __str__(self): return f"{self.full_name} ({self.group})"
    class Meta: verbose_name = "Студент"; verbose_name_plural = "Студенты"; ordering = ["full_name"]

class Subject(models.Model):
    name = models.CharField("Название предмета", max_length=100, unique=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="subjects", verbose_name="Преподаватель")
    def __str__(self): return self.name
    class Meta: verbose_name = "Предмет"; verbose_name_plural = "Предметы"

class Lesson(models.Model):
    date = models.DateField("Дата")
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="lessons", verbose_name="Группа")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="lessons", verbose_name="Предмет")
    topic = models.CharField("Тема занятия", max_length=255)
    homework = models.TextField("Домашнее задание", blank=True)
    def __str__(self): return f"{self.date} — {self.subject} — {self.group}"
    class Meta: verbose_name = "Занятие"; verbose_name_plural = "Занятия"; ordering = ["-date"]

class Mark(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="marks", verbose_name="Занятие")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="marks", verbose_name="Студент")
    value = models.PositiveSmallIntegerField("Оценка", validators=[MinValueValidator(2), MaxValueValidator(5)])
    comment = models.CharField("Комментарий", max_length=255, blank=True)
    def __str__(self): return f"{self.student} — {self.value}"
    class Meta:
        verbose_name = "Оценка"; verbose_name_plural = "Оценки"
        constraints = [models.UniqueConstraint(fields=["lesson", "student"], name="unique_mark_for_student_lesson")]

class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="attendance", verbose_name="Занятие")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance", verbose_name="Студент")
    present = models.BooleanField("Присутствовал", default=True)
    reason = models.CharField("Причина отсутствия", max_length=255, blank=True)
    class Meta:
        verbose_name = "Посещаемость"; verbose_name_plural = "Посещаемость"
        constraints = [models.UniqueConstraint(fields=["lesson", "student"], name="unique_attendance_for_student_lesson")]
