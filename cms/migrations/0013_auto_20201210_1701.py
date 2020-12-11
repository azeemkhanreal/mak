# Generated by Django 3.1.3 on 2020-12-10 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20201210_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cms.portfoliocategories'),
        ),
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
