# Generated by Django 3.0.2 on 2020-03-07 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=10)),
                ('plates', models.CharField(max_length=6)),
                ('date', models.CharField(max_length=10)),
                ('ip', models.GenericIPAddressField(null=True)),
                ('user_agent', models.TextField(null=True)),
            ],
        ),
    ]
