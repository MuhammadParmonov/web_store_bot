# Generated by Django 3.2 on 2024-02-04 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_seb_category_product_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
