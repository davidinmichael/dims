# Generated by Django 5.0.6 on 2024-08-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_admin_user',
            field=models.BooleanField(default=True),
        ),
    ]
