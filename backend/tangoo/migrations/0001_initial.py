# Generated by Django 3.1.3 on 2020-11-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tangoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase_en', models.CharField(max_length=200)),
                ('phrase_ja', models.CharField(max_length=200)),
                ('word_en', models.CharField(max_length=200)),
            ],
        ),
    ]
