# Generated by Django 4.1.7 on 2023-06-13 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zdjecie',
            name='zd_IdTowar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.towar'),
        ),
    ]
