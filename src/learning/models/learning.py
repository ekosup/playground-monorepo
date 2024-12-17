from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey("user.User", related_name="courses", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'courses'
        ordering = ['title']
        verbose_name_plural = 'Courses'


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.title}: {self.title}"

    class Meta:
        db_table = 'course_modules'
        ordering = ['course', 'order']
        verbose_name_plural = 'Courses Modules'


class Lesson(models.Model):
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course_lessons'
        ordering = ['order']
        verbose_name_plural = 'Courses Lessons'

    def __str__(self):
        return f"{self.module.title}: {self.title}"


class UserCourse(models.Model):
    user = models.ForeignKey("user.User", related_name="courses_joined", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="students", on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course_users'
        ordering = ['joined_at']
        unique_together = ['user', 'course']
        verbose_name_plural = 'Courses Students'

    def __str__(self):
        return f"{self.user} - {self.course}"


class UserCourseProgress(models.Model):
    user_course = models.OneToOneField(UserCourse, related_name="progress", on_delete=models.CASCADE)
    lessons = models.ForeignKey(Lesson, related_name="progress", on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course_user_progress'
        ordering = ['completed_at']
        verbose_name_plural = 'Courses Progress'

    def __str__(self):
        return f"{self.user_course} - {self.completed_at}"
