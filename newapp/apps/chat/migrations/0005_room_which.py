# Generated by Django 3.1 on 2020-10-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20201022_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='which',
            field=models.CharField(default='private', max_length=20),
        ),
    ]
