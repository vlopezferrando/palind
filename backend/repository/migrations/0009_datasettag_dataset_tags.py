# Generated by Django 4.2.3 on 2023-11-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("repository", "0008_submission_abbr_zip_code_at_birth_token_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DatasetTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="dataset",
            name="tags",
            field=models.ManyToManyField(to="repository.datasettag"),
        ),
    ]