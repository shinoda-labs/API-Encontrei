# Generated by Django 2.2.2 on 2019-06-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('imagem', models.URLField(max_length=255)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tb_categoria',
            },
        ),
    ]
