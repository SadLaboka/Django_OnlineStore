# Generated by Django 3.1.6 on 2021-02-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210224_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='main.Order', verbose_name='Заказы покупателя'),
        ),
    ]
