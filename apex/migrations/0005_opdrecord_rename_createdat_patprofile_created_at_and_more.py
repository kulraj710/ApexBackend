# Generated by Django 4.1.5 on 2023-01-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apex', '0004_remove_patprofile_createdat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpdRecord',
            fields=[
                ('date', models.DateTimeField()),
                ('weight', models.CharField(blank=True, max_length=11, null=True)),
                ('height', models.CharField(blank=True, max_length=15, null=True)),
                ('temp', models.CharField(blank=True, max_length=5, null=True)),
                ('ref', models.CharField(blank=True, max_length=20, null=True)),
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('charge', models.IntegerField()),
            ],
            options={
                'db_table': 'opd_record',
            },
        ),
        migrations.RenameField(
            model_name='patprofile',
            old_name='createdAt',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='patprofile',
            old_name='referredBy',
            new_name='referred_by',
        ),
        migrations.AlterField(
            model_name='patprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patprofile',
            name='sex',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
