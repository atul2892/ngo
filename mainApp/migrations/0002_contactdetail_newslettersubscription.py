# Generated by Django 5.0.1 on 2024-05-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank='true', default='', max_length=254, null='true')),
                ('company', models.CharField(blank='true', default='', max_length=200, null='true')),
                ('message', models.TextField(blank='true', default='', null='true')),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank='true', default='', max_length=254, null='true')),
            ],
        ),
    ]
