# Generated by Django 5.1.3 on 2024-11-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0004_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
