# Generated by Django 2.2.24 on 2021-07-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210714_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testable',
            name='name',
            field=models.CharField(default='Name_', help_text='Model Representaion Name', max_length=200),
        ),
    ]
