# Generated by Django 2.2.2 on 2019-06-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimento', '0003_auto_20190617_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='atualizado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='criado',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]