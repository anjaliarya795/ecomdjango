# Generated by Django 4.1.3 on 2023-03-16 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_address_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
