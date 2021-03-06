# Generated by Django 3.2.8 on 2021-10-22 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.store')),
            ],
        ),
    ]
