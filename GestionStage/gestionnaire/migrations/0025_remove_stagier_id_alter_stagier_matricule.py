# Generated by Django 4.0.1 on 2022-01-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0024_stagier_id_alter_stagier_matricule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stagier',
            name='id',
        ),
        migrations.AlterField(
            model_name='stagier',
            name='matricule',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Matricule'),
        ),
    ]
