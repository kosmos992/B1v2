# Generated by Django 3.2.12 on 2022-05-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0002_auto_20220502_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cctv',
            name='latitude',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cctv',
            name='longitude',
            field=models.CharField(max_length=100, null=True),
        ),
    ]