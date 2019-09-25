from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission
from django.core.validators import MaxValueValidator, MinValueValidator

permission = GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.USER,
   "foo@mailinator.com"
)

gd_storage = GoogleDriveStorage()

# Create your models here.
class QPApplication(models.Model):
    """Model representing a single QP application."""
    score = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])

    num_of_scores = models.IntegerField(help_text="# of scorers")

    first_name = models.CharField(max_length=100, help_text="First Name *")

    last_name = models.CharField(max_length=100, help_text="Last Name *")

    email = models.EmailField(max_length=100, help_text="Email *")

    personal_link = models.URLField(null=True, blank=True, help_text="Link to personal website, portfolio or Github", max_length=200)

    PROGRAM_CHOICES = (
        ('qp', 'Quarterly Projects'),
        ('qp2', 'QP++'),
        ('bo', 'Both')
    )

    programs = models.CharField(
        max_length=50,
        choices=PROGRAM_CHOICES,
        default='qp',
        help_text='Which programs would you like to be considered for? *',
    )

    DEPARTMENT_CHOICES = (
        ('ece', 'Electrical and Computer Engineering'),
        ('cse', 'Computer Science and Engineering'),
        ('mae', 'Mechanical and Aerospace Engineering'),
        ('be', 'BioEngineering'),
        ('ne', 'NanoEngineering'),
        ('se', 'Structural Engineering'),
        ('cs', 'Cognitive Science'),
        ('ds', 'Data Science'),
        ('math', 'Mathematics'),
        ('bs', 'Biological Sciences'),
        ('candb', 'Chemistry & Biochemistry'),
        ('p', 'Physics'),
        ('bus', 'Business'),
        ('hum', 'Humanities'),
        ('oth', 'Other'),
    )

    department = models.CharField(
        max_length=100,
        choices=DEPARTMENT_CHOICES,
        default='ece',
        help_text='Select your department *',
    )

    YEAR_OF_STUDY_CHOICES = (
        ('fr', 'Freshman'),
        ('so', 'Sophomore'),
        ('ju', 'Junior'),
        ('se', 'Senior'),
        ('oth', 'Other'),
    )

    year_of_study = models.CharField(
        max_length=20,
        choices=YEAR_OF_STUDY_CHOICES,
        default='fr',
        help_text='Year of Study *'
    )

    HOW_DID_YOU_HEAR_CHOICES = (
        ('gbm', 'IEEE GBM'),
        ('fb', 'Facebook'),
        ('news', 'Newsletter'),
        ('fly', 'Flyer'),
        ('ta', 'Tabling (Engineers on the Green, Library Walk, etc.)'),
        ('fr', 'Friend in IEEE UC San Diego'),
        ('pr', 'Previously in IEEE Quarterly Projects'),
        ('oth', 'Other'),
    )

    how_did_you_hear = models.CharField(
        max_length=100,
        choices=HOW_DID_YOU_HEAR_CHOICES,
        default='gbm',
        help_text='How did you hear about Quarterly Projects? *',
    )

    course_work = models.TextField(
        max_length=1500, help_text='List any coursework relevant to building projects or working in teams! *')

    extracurricular_work = models.TextField(
        max_length=3000, help_text='List and describe up to 3 extracurricular projects or experiences *')

    technical_skills = models.TextField(
        max_length=1000, help_text='List any technical skills you have with a rating from 1 to 5 (eg: Photoshop (5),  AutoCAD (4), Python (3), Excel (1), etc.) *')
    
    MICROCONTROLLER_CHOICES = (
        ('y', 'Yes'),
        ('n', 'No'),
    )

    microcontrollers = models.CharField(
        max_length=3,
        choices=MICROCONTROLLER_CHOICES,
        default='y',
        help_text='Have you used microcontrollers before (Raspberry Pi, Arduino, STM, etc)? *',
    )

    collab_situation = models.TextField(
        max_length=3000, help_text='Describe a situation where you collaborated with others *')

    project_motivation = models.TextField(
        max_length=1000, help_text='In one to two sentences, what motivates you to be on a project? Why do you want to build a project, and what benefit does project experience bring to you and your teammates? *')

    project_goal_but_not_steps = models.TextField(
        max_length=3000, help_text='Imagine that you know the goal of your project but are unsure of the intermediate steps necessary to achieve it. What would you do to figure out these intermediate steps in order to progress and finish your project? *')

    rude_team_member = models.TextField(
        max_length=3000, help_text='You have a team member that is rude to your team members, does little work, and is in general hard to work with. How do you address this? *')

    QUARTER_LONG_CHOICES = (
        ('y', 'Yes'),
    )

    quarter_long_obligation = models.CharField(
        max_length=3,
        choices=QUARTER_LONG_CHOICES,
        default='n',
        help_text='I understand that this is a quarter long obligation and that not showcasing my project will negatively impact my team. *',
    )

    teammates = models.TextField(null=True, blank=True,
        max_length=1000, help_text='Hoping to work with other people? Please list their full name, email and major. (eg: John Smith, jsmith@gmail.com, ECE)')

    resume_upload = models.FileField(null=True, blank=True, upload_to='resumes/', storage=gd_storage, help_text='Please upload your resume in "firstname_lastname_CV.pdf" format')

    class Meta:
        ordering = ['-score']
