# Generated by Django 4.2.5 on 2023-12-15 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_rename_ratings_maindatabase_product_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlipkartData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=1000)),
                ('image_source', models.CharField(max_length=1000)),
                ('ratings', models.CharField(max_length=50)),
                ('brand_name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('actual_price', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GemData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=1000)),
                ('image_source', models.CharField(max_length=1000)),
                ('ratings', models.CharField(max_length=50)),
                ('brand_name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('actual_price', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='FlipkartDatabase',
        ),
        migrations.DeleteModel(
            name='MainDatabase',
        ),
    ]
