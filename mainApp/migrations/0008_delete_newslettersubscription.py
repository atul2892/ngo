# Generated by Django 5.0.1 on 2024-05-11 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_alter_newslettersubscription_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsletterSubscription',
        ),
    ]
