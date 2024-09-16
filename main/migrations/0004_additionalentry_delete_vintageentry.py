# Generated by Django 5.1.1 on 2024-09-16 23:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_vintageentry_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('era', models.CharField(max_length=50)),
                ('time', models.DateField(auto_now_add=True)),
                ('condition', models.TextField()),
                ('stock', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='VintageEntry',
        ),
    ]
