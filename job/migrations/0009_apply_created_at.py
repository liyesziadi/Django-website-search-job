# Generated by Django 3.1.3 on 2020-11-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
