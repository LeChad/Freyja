# Generated by Django 4.2 on 2023-07-01 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photography_album', '0005_alter_photographs_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photographs',
            name='uploaded_by',
        ),
    ]
