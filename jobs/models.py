from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    required_skills = models.JSONField()

    def __str__(self):
        return self.title


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    skills = models.JSONField()

    def __str__(self):
        return self.name


class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.candidate.name} - {self.job.title}"