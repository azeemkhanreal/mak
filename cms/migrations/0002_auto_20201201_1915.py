# Generated by Django 2.1.5 on 2020-12-01 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customize',
            name='founder_message',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='customize',
            name='how_we_work',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
