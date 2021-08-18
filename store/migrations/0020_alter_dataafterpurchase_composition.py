# Generated by Django 3.2.5 on 2021-08-11 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_dataafterpurchase_composition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataafterpurchase',
            name='composition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='store.composition'),
        ),
    ]