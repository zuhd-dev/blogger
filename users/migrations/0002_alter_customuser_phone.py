# Generated by Django 4.2.4 on 2023-09-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Phone'),
        ),
    ]