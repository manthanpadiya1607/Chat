# Generated by Django 4.1.7 on 2023-04-03 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_signup_alter_message_id_alter_room_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
    ]
