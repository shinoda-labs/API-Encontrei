# Generated by Django 2.2.2 on 2019-06-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimento', '0008_auto_20190618_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='titulo',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
