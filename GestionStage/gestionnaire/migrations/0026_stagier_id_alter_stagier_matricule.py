# Generated by Django 4.0.1 on 2022-01-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0025_remove_stagier_id_alter_stagier_matricule'),
    ]

    operations = [
        migrations.AddField(
            model_name='stagier',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stagier',
            name='matricule',
            field=models.CharField(max_length=12, verbose_name='Matricule'),
        ),
    ]
