# Generated by Django 5.1.2 on 2024-11-07 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='completed_at',
            field=models.DateTimeField(null=True),
        ),
    ]