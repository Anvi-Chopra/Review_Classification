# Generated by Django 3.2.9 on 2021-11-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='shuanakk09', max_length=122, verbose_name='username')),
                ('name', models.CharField(max_length=122, verbose_name='name')),
                ('desc', models.FloatField(verbose_name='desc')),
            ],
        ),
    ]