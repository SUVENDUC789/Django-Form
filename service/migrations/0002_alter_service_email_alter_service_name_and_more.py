# Generated by Django 4.1 on 2022-09-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='email',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=130),
        ),
        migrations.AlterField(
            model_name='service',
            name='reg',
            field=models.CharField(max_length=130),
        ),
        migrations.AlterField(
            model_name='service',
            name='roll',
            field=models.CharField(max_length=130),
        ),
    ]