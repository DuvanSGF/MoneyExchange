# Generated by Django 2.2.4 on 2019-08-16 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changehouse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='com_tipo',
            new_name='Com_tipo',
        ),
    ]