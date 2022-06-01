# Generated by Django 4.0.4 on 2022-05-07 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autismrecord',
            name='Jaundice',
            field=models.CharField(choices=[(1, 'Yes'), (0, 'No')], default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='Why_are_you_taken_the_screening',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='class_variable',
            field=models.CharField(choices=[(0, 'No'), (1, 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
