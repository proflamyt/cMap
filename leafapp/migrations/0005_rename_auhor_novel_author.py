# Generated by Django 3.2.10 on 2021-12-29 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leafapp', '0004_auto_20211229_0541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='novel',
            old_name='auhor',
            new_name='author',
        ),
    ]
