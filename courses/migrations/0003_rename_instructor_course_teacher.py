# Generated by Django 4.2.3 on 2023-07-12 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_users_course_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='instructor',
            new_name='teacher',
        ),
    ]
