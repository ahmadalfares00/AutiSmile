# Generated by Django 4.0.4 on 2022-06-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_app', '0005_alter_autismrecord_family_mem_with_asd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autismrecord',
            name='A1',
            field=models.IntegerField(choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never')], default=None),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='A10',
            field=models.IntegerField(choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never')], default=None),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='A2',
            field=models.IntegerField(choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never')], default=None),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='A3',
            field=models.IntegerField(choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never')], default=None),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='A4',
            field=models.IntegerField(choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never')], default=None),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='A5',
            field=models.IntegerField(choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never')], default=None),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='A6',
            field=models.IntegerField(choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never')], default=None),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='A7',
            field=models.IntegerField(choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never')], default=None),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='A8',
            field=models.IntegerField(choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never')], default=None),
        ),
        migrations.AlterField(
            model_name='autismrecord',
            name='A9',
            field=models.IntegerField(choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never')], default=None),
        ),
    ]
