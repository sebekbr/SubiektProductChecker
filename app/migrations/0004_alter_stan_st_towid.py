# Generated by Django 4.1.7 on 2023-06-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_magazyn_table_alter_stan_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stan',
            name='st_TowId',
            field=models.IntegerField(db_column='st_TowId', primary_key=True, serialize=False),
        ),
    ]