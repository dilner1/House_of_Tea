# Generated by Django 3.2 on 2022-11-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]