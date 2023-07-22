# Generated by Django 4.2 on 2023-06-23 19:24

from django.db import migrations, models
import main.validator
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photographs',
            fields=[
                ('photograph_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photograph', models.ImageField(upload_to='photographs', validators=[main.validator.validate_image])),
                ('title', models.CharField(default='Untitled', max_length=100)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Photographs',
                'verbose_name_plural': 'Photographs',
            },
        ),
    ]