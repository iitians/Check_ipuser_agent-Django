# Generated by Django 3.0.2 on 2020-03-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetail',
            name='location',
            field=models.CharField(default='PL', max_length=4),
            preserve_default=False,
        ),
    ]
