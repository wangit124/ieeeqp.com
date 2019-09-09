from django.contrib import admin
from landing.models import QPApplication

# Register your models here.
@admin.register(QPApplication)
class QPApplicationAdmin(admin.ModelAdmin):
    list_display = ('email', 'personal_link', 'programs', 'first_name', 'last_name', 'department', 'year_of_study', 'how_did_you_hear', 'course_work', 'extracurricular_work',
                    'technical_skills', 'microcontrollers', 'collab_situation', 'project_motivation', 'project_goal_but_not_steps', 'rude_team_member', 'quarter_long_obligation', 'teammates', 'ieee_member_number', 'resume_upload')

