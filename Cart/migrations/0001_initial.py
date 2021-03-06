# Generated by Django 3.2.5 on 2021-08-22 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('customer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
