# Generated by Django 4.0.1 on 2022-01-24 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0015_rename_numencadreur_groupe_idencadreur_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encadreur',
            name='idOrganisme',
        ),
        migrations.AddField(
            model_name='promoteur',
            name='idOrganisme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.organisme', verbose_name='Organisme'),
            preserve_default=False,
        ),
    ]