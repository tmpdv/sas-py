# Generated by Django 3.1.5 on 2021-01-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='creation_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='destination',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='last_updated',
            field=models.DateTimeField(null=True),
        ),
    ]
