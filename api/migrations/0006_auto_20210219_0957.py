# Generated by Django 3.1.6 on 2021-02-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210219_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
    ]
