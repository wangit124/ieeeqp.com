# Generated by Django 2.2.5 on 2019-09-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0018_auto_20190911_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qpapplication',
            name='collab_situation',
            field=models.TextField(help_text='Describe a situation where you collaborated with others *', max_length=3000),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='course_work',
            field=models.TextField(help_text='List any coursework relevant to building projects or working in teams! *', max_length=1500),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='email',
            field=models.EmailField(help_text='Email *', max_length=100),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='extracurricular_work',
            field=models.TextField(help_text='List and describe up to 3 extracurricular projects or experiences *', max_length=3000),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='first_name',
            field=models.CharField(help_text='First Name *', max_length=100),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='last_name',
            field=models.CharField(help_text='Last Name *', max_length=100),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='programs',
            field=models.CharField(choices=[('qp', 'Quarterly Projects'), ('qp2', 'QP++'), ('b', 'Both')], default='qp', help_text='Which programs would you like to be considered for? *', max_length=50),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='project_goal_but_not_steps',
            field=models.TextField(help_text='Imagine that you know the goal of your project but are unsure of the intermediate steps necessary to achieve it. What would you do to figure out these intermediate steps in order to progress and finish your project? *', max_length=3000),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='project_motivation',
            field=models.TextField(help_text='In one to two sentences, what motivates you to be on a project? Why do you want to build a project, and what benefit does project experience bring to you and your teammates? *', max_length=1000),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='rude_team_member',
            field=models.TextField(help_text='You have a team member that is rude to your team members, does little work, and is in general hard to work with. How do you address this? *', max_length=3000),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='technical_skills',
            field=models.TextField(help_text='List any technical skills you have with a rating from 1 to 5 (eg: Photoshop (5),  AutoCAD (4), Python (3), Excel (1), etc.) *', max_length=1000),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='year_of_study',
            field=models.CharField(choices=[('fr', 'Freshman'), ('so', 'Sophomore'), ('ju', 'Junior'), ('se', 'Senior'), ('oth', 'Other')], default='fr', help_text='Year of Study', max_length=20),
        ),
    ]
