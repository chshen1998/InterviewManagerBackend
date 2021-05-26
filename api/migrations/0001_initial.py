# Generated by Django 3.1.2 on 2021-01-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=50)),
                ('stage', models.CharField(max_length=20)),
                ('state', models.BooleanField(default=False)),
                ('date', models.DateTimeField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
