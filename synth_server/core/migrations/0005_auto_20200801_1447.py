# Generated by Django 3.0.8 on 2020-08-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200731_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lines',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
