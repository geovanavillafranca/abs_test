# Generated by Django 4.0.6 on 2022-07-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_client_phone_number_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]