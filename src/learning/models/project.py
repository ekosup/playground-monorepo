from django.db import models


class Organization(models.Model):
    title = models.CharField(max_length=500)
    settings = models.JSONField(default=dict)
    status = models.PositiveIntegerField()


class User(models.Model):
    name = models.CharField(max_length=500)
    settings = models.JSONField(default=dict, null=True, blank=True)
    status = models.PositiveIntegerField(null=True, blank=True)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True, blank=True)


class Department(models.Model):
    title = models.CharField(max_length=500)
    settings = models.JSONField(default=dict)
    status = models.PositiveIntegerField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name='department_user')


class Team(models.Model):
    title = models.CharField(max_length=500)
    settings = models.JSONField(default=dict)
    status = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name='team_user')


class Project(models.Model):
    title = models.CharField(max_length=500)
    settings = models.JSONField(default=dict)
    status = models.PositiveIntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name='project_user')


class Task(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    start = models.DateField()
    end = models.DateField()
    settings = models.JSONField(default=dict)
    status = models.PositiveIntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='task')
    user = models.ManyToManyField(User, related_name='task_user')
