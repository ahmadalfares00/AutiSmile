# Generated by Django 4.0.4 on 2022-05-07 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_app', '0002_alter_autismrecord_jaundice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autismrecord',
            name='Jaundice',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='class_variable',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=10),
        ),
    ]
