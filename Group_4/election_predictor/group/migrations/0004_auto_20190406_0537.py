# Generated by Django 2.1.7 on 2019-04-06 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_group_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]
