# Generated by Django 2.2.2 on 2019-09-03 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lazer', '0006_auto_20190902_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='aluno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
