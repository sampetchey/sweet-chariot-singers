from django.db import models

class Vacancy(models.Model):
    job_title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "vacancies"
        ordering = ['job_title']

    def __str__(self):
        return self.job_title