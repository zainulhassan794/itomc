# Generated by Django 4.2.4 on 2023-08-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_free_tutorials_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free_tutorials',
            name='body',
            field=models.CharField(max_length=100, null=True),
        ),
    ]