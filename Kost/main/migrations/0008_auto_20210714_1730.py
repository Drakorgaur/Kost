# Generated by Django 2.2.24 on 2021-07-14 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_currentnote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currentnote',
            options={'ordering': ['note']},
        ),
    ]
