# Generated by Django 4.0.4 on 2022-06-12 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='type_noification',
            new_name='type_notification',
        ),
    ]
