# Generated by Django 2.2.5 on 2019-10-07 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_auto_20190915_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='upvotes',
            field=models.PositiveIntegerField(default=1, verbose_name='upvotes'),
        ),
    ]
