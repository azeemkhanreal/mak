# Generated by Django 2.1.5 on 2020-12-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bimage_title', models.CharField(blank=True, max_length=50, null=True)),
                ('bimage_desc', models.CharField(blank=True, max_length=300, null=True)),
                ('bimage', models.ImageField(default='', upload_to='banner/images')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cimage_title', models.CharField(blank=True, max_length=50, null=True)),
                ('cimage', models.ImageField(default='', upload_to='clients/images')),
            ],
        ),
        migrations.CreateModel(
            name='Customize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('founder_message', models.CharField(blank=True, max_length=50, null=True)),
                ('how_we_work', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pimage_title', models.CharField(blank=True, max_length=50, null=True)),
                ('pimage_desc', models.CharField(blank=True, max_length=300, null=True)),
                ('pimage_cat', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(default='', upload_to='portfolios/images')),
            ],
        ),
    ]
