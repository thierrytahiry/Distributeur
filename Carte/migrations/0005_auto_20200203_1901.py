# Generated by Django 3.0 on 2020-02-03 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Carte', '0004_auto_20200203_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carte',
            name='montant_Par_Mois',
        ),
        migrations.RemoveField(
            model_name='carte',
            name='nb_Par_Mois',
        ),
    ]
