# Generated by Django 3.1.3 on 2020-12-30 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0007_auto_20201221_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='size',
        ),
        migrations.AddField(
            model_name='file',
            name='byte_size',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
