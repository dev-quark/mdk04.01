from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, GroupViewSet, LessonViewSet, MarkViewSet, StudentViewSet, SubjectViewSet
router = DefaultRouter()
router.register("groups", GroupViewSet); router.register("students", StudentViewSet); router.register("subjects", SubjectViewSet); router.register("lessons", LessonViewSet); router.register("marks", MarkViewSet); router.register("attendance", AttendanceViewSet)
urlpatterns = router.urls
