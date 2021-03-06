# Generated by Django 3.1.3 on 2020-12-08 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscriptions', '0006_add_slugs'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(max_length=255)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.subscriptionplan')),
            ],
        ),
    ]
