# Generated by Django 2.2.26 on 2022-07-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vince', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpgpemail',
            name='pgp_key_data',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='vendor_type',
            field=models.CharField(choices=[('Contact', 'Contact'), ('Vendor', 'Vendor'), ('User', 'User'), ('Coordinator', 'Coordinator')], default='Vendor', max_length=50),
        ),
    ]
