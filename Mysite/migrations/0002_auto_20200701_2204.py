# Generated by Django 3.0.8 on 2020-07-01 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Subject',
            new_name='subject',
        ),
    ]
