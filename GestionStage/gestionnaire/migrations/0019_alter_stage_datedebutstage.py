# Generated by Django 4.0.1 on 2022-01-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0018_alter_stage_datedebutstage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='dateDebutStage',
            field=models.DateTimeField(null=True),
        ),
    ]
