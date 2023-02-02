from django.db import models

# Create your models here.
# CREATE TABLE Question name string , date datetime

class Question(models.Model):
    question_text = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question_text