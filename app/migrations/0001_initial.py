# Generated by Django 3.1.4 on 2020-12-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('email', models.TextField()),
                ('phone', models.TextField()),
                ('msg', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]