# Generated by Django 3.2.5 on 2021-08-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='school_or_university',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]