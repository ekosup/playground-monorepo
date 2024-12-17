from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'quizzes'
        ordering = ['title']


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'quiz_questions'
        ordering = ['created_at']


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer

    class Meta:
        db_table = 'quiz_answers'
        ordering = ['created_at']


class UserQuizResult(models.Model):
    user = models.ForeignKey("user.User", related_name="quiz_results", on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name="user_results", on_delete=models.CASCADE)
    answer = models.JSONField(default=dict)
    score = models.FloatField()
    taken_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_quiz_results'
        ordering = ['taken_at']
        unique_together = ['user', 'quiz']

    def __str__(self):
        return f"{self.user} - {self.quiz}"
