# Generated by Django 5.1.5 on 2025-01-16 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0005_tag_alter_book_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="file",
            field=models.FileField(upload_to="books/file/%Y/%m/%d/"),
        ),
    ]
