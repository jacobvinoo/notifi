# Generated by Django 2.1.15 on 2020-05-16 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_auto_20200516_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='receiver_employe',
            new_name='receiver_employee',
        ),
    ]
