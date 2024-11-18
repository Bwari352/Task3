# Generated by Django 5.1.3 on 2024-11-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0002_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('profile_picture', models.FileField(upload_to='teams/')),
                ('twitter_url', models.CharField(max_length=200)),
                ('facebook_url', models.CharField(max_length=200)),
                ('linkedin_url', models.CharField(max_length=200)),
            ],
        ),
    ]
