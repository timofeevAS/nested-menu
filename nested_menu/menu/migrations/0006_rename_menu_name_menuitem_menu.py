# Generated by Django 4.2.1 on 2023-05-05 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_rename_menu_menuitem_menu_name_menuitem_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='menu_name',
            new_name='menu',
        ),
    ]