# Generated by Django 4.0 on 2022-01-12 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_movie_reviews_remove_review_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='descption',
            new_name='description',
        ),
    ]