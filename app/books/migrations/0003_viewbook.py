# Generated by Django 5.0.1 on 2024-01-31 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0002_book_tags_alter_book_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewBook',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('ip', models.GenericIPAddressField()),
                (
                    'book',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to='books.book',
                    ),
                ),
            ],
        ),
    ]
