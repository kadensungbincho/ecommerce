# Generated by Django 2.1.1 on 2018-10-07 09:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_productpurchagemanager_productpurchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpurchase',
            name='user',
        ),
        migrations.AddField(
            model_name='productpurchase',
            name='order_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]
