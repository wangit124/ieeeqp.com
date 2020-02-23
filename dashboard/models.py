from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from landing.models import QPApplication, team

class ScoreApplication(models.Model):
    application = models.ForeignKey(QPApplication, on_delete=models.DO_NOTHING)
    scorer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])

class ProjectProposal(models.Model):
    title = models.CharField(max_length=100, help_text="Project Title")
    description = models.CharField(max_length=2000, help_text="Project Description")
    team_num = models.CharField(max_length=100, help_text="Team Number")
    team = models.CharField(max_length=300, help_text="Team Nickname")

    PROGRAM_CHOICES = (
        ('qp', 'QP'),
        ('qp2', 'QP++'),
    )

    program = models.CharField(
        max_length=50,
        choices=PROGRAM_CHOICES,
        default='qp',
        help_text='Program (QP or QP++)',
    )

    materials = models.CharField(max_length=2000, help_text="Bill of Materials (Enter a new line for every item. Please provide: name, quantity, vendor-link for each)")
    timeline = models.CharField(max_length=2000, help_text="Timeline of Work (Enter a new line for every week. Please provide: week # and task description for each)")
    confidence = models.CharField(max_length=2000, help_text="Collect a sentence from each member stating why you are confident you will succeed in making this project")

class Milestone(models.Model):
    REPORT_NUM_CHOICES = (
        ('1', 'Week 5'),
        ('2', 'Week 7'),
    )

    report_num = models.CharField(
        max_length=50,
        choices=REPORT_NUM_CHOICES,
        default='2',
        help_text='Choose a milestone report',
    )

    team_num = models.IntegerField(help_text="Team Number (Please enter a number from 1 - 113)")

    PROGRAM_CHOICES = (
        ('qp', 'QP'),
        ('qp2', 'QP++'),
    )

    program = models.CharField(
        max_length=50,
        choices=PROGRAM_CHOICES,
        default='qp',
        help_text='Program (QP or QP++)',
    )

    accomplishments = models.CharField(max_length=2000, help_text="What have you accomplished so far?")
    projected = models.CharField(max_length=2000, help_text="What do you hope to accomplish in the next 2 weeks?")
    blockers = models.CharField(max_length=2000, null=True, blank=True, help_text="Name a few issues that are hindering/preventing your progress (Leave blank if none)")