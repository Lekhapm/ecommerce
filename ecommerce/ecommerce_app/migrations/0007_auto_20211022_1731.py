# Generated by Django 3.2.8 on 2021-10-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0006_customer_storeadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]