# Generated by Django 3.0.5 on 2020-04-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='writter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('id_number', models.IntegerField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
