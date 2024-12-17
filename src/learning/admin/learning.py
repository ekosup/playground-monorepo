from django.contrib import admin
from unfold.admin import ModelAdmin

from learning.models import Course, Module, Lesson, UserCourse, UserCourseProgress


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    pass


@admin.register(Module)
class ModuleAdmin(ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(ModelAdmin):
    pass


@admin.register(UserCourse)
class UserCourseAdmin(ModelAdmin):
    pass


@admin.register(UserCourseProgress)
class UserCourseProgressAdmin(ModelAdmin):
    pass
