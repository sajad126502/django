# Generated by Django 4.0.3 on 2022-03-16 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
    ]
