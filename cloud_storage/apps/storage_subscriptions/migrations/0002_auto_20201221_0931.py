# Generated by Django 3.1.3 on 2020-12-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagesubscription',
            name='size',
            field=models.IntegerField(),
        ),
    ]
