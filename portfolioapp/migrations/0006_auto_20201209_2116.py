# Generated by Django 3.1.4 on 2020-12-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0005_contact_urlornot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='urlornot',
            field=models.CharField(default='no', max_length=3),
        ),
    ]
