# Generated by Django 5.1.4 on 2025-01-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='detail',
            field=models.TextField(default='Rich Dad Poor Dad'),
            preserve_default=False,
        ),
    ]
