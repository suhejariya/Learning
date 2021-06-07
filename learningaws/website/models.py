from django.db import models

# Create your models here.
class QuesAns(models.Model):
    ques = models.TextField(blank=True, null=True)
    ans = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.ques}'