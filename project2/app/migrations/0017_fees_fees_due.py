# Generated by Django 2.2.2 on 2019-07-03 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_fees_fees_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='fees_due',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
