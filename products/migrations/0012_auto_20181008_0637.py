# Generated by Django 2.1.1 on 2018-10-08 06:37

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_productfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='//kadencho-ecommerce.s3.amazonaws.com/protected/'), upload_to=products.models.upload_product_file_loc),
        ),
    ]
