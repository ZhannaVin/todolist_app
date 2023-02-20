from django.db import models

# Create your models here.

class Tasks(models.Model):
    description = models.CharField("Задача", max_length=50)
    deadline = models.CharField("Дедлайн", max_length=50,  default='SOME STRING')
    is_complete = models.BooleanField("Завершено", default=False)
    user = models.CharField("Пользователь", max_length=30,default="")

    def __str__(self):
        return self.description