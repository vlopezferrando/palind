# Generated by Django 4.2.3 on 2023-11-02 20:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("datasets", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DatasetTag",
            new_name="Tag",
        ),
    ]