from django.contrib import admin
from dashboard.models import ScoreApplication

@admin.register(ScoreApplication)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('application', 'scorer', 'score')