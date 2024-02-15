# Generated by Django 3.2 on 2024-02-07 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_user_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('preparing', 'Tayyorlanmoqda'), ('delivering', 'Yetkazilmoqda'), ('finished', 'Yetkazib berildi')], max_length=50)),
                ('products', models.ManyToManyField(to='main.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
