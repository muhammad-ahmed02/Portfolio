# Generated by Django 3.1.4 on 2020-12-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
