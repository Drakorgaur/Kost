# Generated by Django 3.2.6 on 2021-09-14 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210815_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='add_field',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='main_field',
            field=models.CharField(help_text='Main text', max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.CharField(help_text='Name', max_length=200),
        ),
    ]
