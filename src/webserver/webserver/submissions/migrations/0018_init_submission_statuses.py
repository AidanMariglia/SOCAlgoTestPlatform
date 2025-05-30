# Generated by Django 5.1.2 on 2025-03-22 02:27

from django.db import migrations

def create_initial_submission_statuses(apps, schema_editor):
    SubmissionStatus = apps.get_model('submissions', 'SubmissionStatus')
    initial_statuses = [
        {"name": "pending", "description": "submission is placed on queue"},
        {"name": "failed", "description": "submission has failed"},
        {"name": "completed", "description": "submission has been completed"},
        {"name": "started", "description": "submission is being processed"},
    ]
    #delete old table entries
    SubmissionStatus.objects.filter(name__in=["pending", "failed", "completed", "started"]).delete()
    for status in initial_statuses:
        SubmissionStatus.objects.get_or_create(name=status["name"], description=status["description"])

def reverse_func(apps, schema_editor):
    #if the migration is rolled back
    SubmissionStatus = apps.get_model('submissions', 'SubmissionStatus')
    SubmissionStatus.objects.filter(name__in=["pending", "failed", "completed", "started"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0017_alter_figure_file'),
    ]

    operations = [
        migrations.RunPython(create_initial_submission_statuses, reverse_func),
    ]
