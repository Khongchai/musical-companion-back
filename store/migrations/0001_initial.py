# Generated by Django 3.2.5 on 2021-08-22 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('composers', models.ManyToManyField(related_name='compositions', to='store.Composer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image_link', models.URLField(max_length=500)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items_in_cart', to='Cart.cart')),
                ('composition', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='store.composition')),
            ],
        ),
        migrations.CreateModel(
            name='DataAfterPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('midi_link', models.URLField(blank=True, max_length=500, null=True)),
                ('wav_link', models.URLField(blank=True, max_length=500, null=True)),
                ('flac_link', models.URLField(blank=True, max_length=500, null=True)),
                ('pdf_link', models.URLField(blank=True, max_length=500, null=True)),
                ('composition', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='store.composition')),
                ('purchased_by', models.ManyToManyField(related_name='purchased_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
