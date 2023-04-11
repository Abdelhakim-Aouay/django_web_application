# Generated by Django 4.2 on 2023-04-11 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band')),
            ],
        ),
    ]
