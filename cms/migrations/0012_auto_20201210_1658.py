# Generated by Django 3.1.3 on 2020-12-10 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20201210_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cms.portfoliocategories'),
        ),
    ]
