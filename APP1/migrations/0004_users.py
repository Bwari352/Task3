# Generated by Django 5.1.3 on 2024-11-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0003_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
