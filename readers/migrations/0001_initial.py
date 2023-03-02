# Generated by Django 4.1.7 on 2023-03-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GDP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('country_iso', models.CharField(max_length=2)),
                ('gross_domestic_product', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StackOverflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('age_first_code', models.CharField(max_length=30)),
                ('languages_raw', models.TextField()),
            ],
        ),
    ]