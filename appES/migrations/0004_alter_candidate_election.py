# Generated by Django 4.0.4 on 2022-05-14 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appES', '0003_alter_voter_election'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='Election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appES.election'),
        ),
    ]
