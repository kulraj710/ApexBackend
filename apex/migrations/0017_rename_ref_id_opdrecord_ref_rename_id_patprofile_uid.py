# Generated by Django 4.1.5 on 2023-01-24 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apex', '0016_rename_uid_patprofile_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opdrecord',
            old_name='ref_id',
            new_name='ref',
        ),
        migrations.RenameField(
            model_name='patprofile',
            old_name='id',
            new_name='uid',
        ),
    ]