# Generated by Django 2.1.2 on 2019-02-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
            options={
                'permissions': [('look_a_page', 'can get this a page message')],
            },
        ),
        migrations.CreateModel(
            name='Bpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
            options={
                'permissions': [('look_b_page', 'can get this a page message')],
            },
        ),
    ]
