# Generated by Django 5.1.1 on 2024-09-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_additionalentry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='additionalentry',
            name='price',
            field=models.IntegerField(),
        ),
    ]
