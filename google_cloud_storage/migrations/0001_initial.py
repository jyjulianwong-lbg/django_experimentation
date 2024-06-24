# Generated by Django 4.2.13 on 2024-06-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('file_gcs_path', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]
