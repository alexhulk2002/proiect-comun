# Generated by Django 4.1.2 on 2022-11-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cazare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photos', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
