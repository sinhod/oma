# Generated by Django 5.0 on 2023-12-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_messageforme_contact_message_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sendersPhonenumber',
            field=models.CharField(default='lähettäjän puh.nro', max_length=50),
        ),
    ]
