# Generated by Django 2.2.12 on 2022-02-18 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='img',
            new_name='image',
        ),
    ]