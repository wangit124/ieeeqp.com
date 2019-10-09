from django.db import models
from django.contrib.auth.models import User
from landing.models import QPApplication
from django.core.validators import MaxValueValidator, MinValueValidator

class ScoreApplication(models.Model):
    application = models.ForeignKey(QPApplication, on_delete=models.DO_NOTHING)
    scorer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
