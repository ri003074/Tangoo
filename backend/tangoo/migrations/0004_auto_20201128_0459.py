# Generated by Django 3.1.3 on 2020-11-28 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tangoo', '0003_auto_20201125_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tangoo',
            name='c_counter',
            field=models.IntegerField(default=0),
        ),
    ]