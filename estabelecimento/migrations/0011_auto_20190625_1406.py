# Generated by Django 2.2.2 on 2019-06-25 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimento', '0010_auto_20190625_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categoria.Categoria'),
        ),
    ]
