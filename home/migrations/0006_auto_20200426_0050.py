# Generated by Django 3.0.5 on 2020-04-25 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200426_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Writter'),
        ),
    ]