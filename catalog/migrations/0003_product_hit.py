# Generated by Django 5.1.3 on 2024-12-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hit',
            field=models.BooleanField(default=False),
        ),
    ]
