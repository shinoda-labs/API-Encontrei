# Generated by Django 2.2.2 on 2019-06-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='cep',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='telefone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='whatsapp',
            field=models.IntegerField(),
        ),
    ]