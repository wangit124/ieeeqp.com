# Generated by Django 2.2.5 on 2019-09-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0019_auto_20190911_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qpapplication',
            name='programs',
            field=models.CharField(choices=[('qp', 'Quarterly Projects'), ('qp2', 'QP++'), ('b', 'Both')], default='qp', help_text='Which programs would you like to be considered for?', max_length=50),
        ),
    ]
