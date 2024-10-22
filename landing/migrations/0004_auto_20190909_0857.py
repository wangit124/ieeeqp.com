# Generated by Django 2.2.5 on 2019-09-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_remove_qpapplication_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qpapplication',
            name='course_work',
            field=models.TextField(help_text='List any coursework relevant to building projects or working in teams!', max_length=3000),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='extracurricular_work',
            field=models.TextField(help_text='List and describe up to 3 extracurricular projects or experiences', max_length=3000),
        ),
        migrations.AlterField(
            model_name='qpapplication',
            name='technical_skills',
            field=models.TextField(help_text='List any technical skills you have with a rating from 1 to 5 (eg: Photoshop (5),  AutoCAD (4), Python (3), Excel (1), etc.)', max_length=3000),
        ),
    ]
