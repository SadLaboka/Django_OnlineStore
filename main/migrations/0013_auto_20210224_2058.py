# Generated by Django 3.1.6 on 2021-02-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210224_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='related_customer', to='main.Order', verbose_name='Заказы покупателя'),
        ),
    ]
