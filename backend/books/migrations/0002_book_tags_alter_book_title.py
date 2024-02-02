# Generated by Django 5.0.1 on 2024-01-31 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="tags",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
