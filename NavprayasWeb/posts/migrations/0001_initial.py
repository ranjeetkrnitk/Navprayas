# Generated by Django 2.0.1 on 2018-04-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('timeStamp', models.DateField()),
                ('image', models.ImageField(upload_to='')),
                ('desc', models.TextField()),
                ('author', models.TextField(blank=True, null=True)),
            ],
        ),
    ]