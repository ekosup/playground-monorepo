from django.db import models


class Classroom(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'classrooms'
        ordering = ['title']
        verbose_name = 'Classrooms'
        verbose_name_plural = 'Classrooms'


class UserClassroom(models.Model):
    user = models.ForeignKey("user.User", related_name="classrooms", on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, related_name="users", on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'classroom_user'
        ordering = ['joined_at']
        unique_together = ['user', 'classroom']
        verbose_name = 'Classrooms User'
        verbose_name_plural = 'Classrooms Users'

    def __str__(self):
        return f"{self.user} - {self.classroom}"


class ClassroomTask(models.Model):
    classroom = models.ForeignKey(Classroom, related_name="tasks", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'classroom_task'
        ordering = ['completed', '-completed_at']
        verbose_name = 'Classrooms Task'
        verbose_name_plural = 'Classrooms Tasks'

    def __str__(self):
        return f"{self.title}"


class UserClassroomTask(models.Model):
    user_classroom = models.ForeignKey(UserClassroom, related_name="tasks", on_delete=models.CASCADE)
    task = models.ForeignKey(ClassroomTask, related_name="user_classroom", on_delete=models.CASCADE)
    score = models.FloatField(blank=True, null=True, default=0)

    class Meta:
        db_table = 'classroom_user_task'
        ordering = ['user_classroom', 'task']
        verbose_name = 'Classrooms User Task'
        verbose_name_plural = 'Classrooms Users Tasks'

    def __str__(self):
        return f"{self.user_classroom} - {self.task}"
