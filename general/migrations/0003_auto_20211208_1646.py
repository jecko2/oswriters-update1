# Generated by Django 3.2.9 on 2021-12-08 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_rename_oder_form_secondoder_order_form'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FirstOder',
            new_name='FirstOrder',
        ),
        migrations.RenameModel(
            old_name='SecondOder',
            new_name='SecondOrder',
        ),
    ]