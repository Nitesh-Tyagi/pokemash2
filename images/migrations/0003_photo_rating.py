# Generated by Django 4.0.4 on 2022-05-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_remove_photo_id_photo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, default=1400, null=True),
        ),
    ]
