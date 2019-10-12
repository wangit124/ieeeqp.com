from django.db import models
from django.contrib.auth.models import User
from landing.models import QPApplication
from django.core.validators import MaxValueValidator, MinValueValidator

class ScoreApplication(models.Model):
    application = models.ForeignKey(QPApplication, on_delete=models.DO_NOTHING)
    scorer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])

class ProjectProposal(models.Model):
    title = models.CharField(max_length=100, help_text="Project Title")
    description = models.CharField(max_length=2000, help_text="Project Description")
    team = models.CharField(max_length=300, help_text="Team Name")
    materials = models.CharField(max_length=2000, help_text="Bill of Materials (Eg: 1. Raspberry Pi B+, 3, www.amazon.com, 2. etc...)")
    timeline = models.CharField(max_length=2000, help_text="Timeline of Work (Eg: Week 1 - Design, Week 2 - Build, Week 3 - Polish, etc...)")
