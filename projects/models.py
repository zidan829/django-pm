from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProjectStatus(models.IntegerChoices):
    PENDING=1,'pending'
    COMPLETED=2,'completed'
    POSTPONED=3,'Postponed'
    CANCELED=4,'Canceled'



class Projects(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    status=models.IntegerField(
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING
    )
    created_at=models.DateTimeField(auto_created=True)
    update_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    user=models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title
class Task(models.Model):
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    project=models.ForeignKey(Projects,on_delete=models.CASCADE)