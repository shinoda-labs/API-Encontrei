# Generated by Django 2.2.2 on 2019-06-17 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('criado', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('imagem', models.URLField(max_length=255)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.IntegerField(max_length=8)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('telefone', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('sobre', models.TextField(max_length=255)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('whatsapp', models.IntegerField(max_length=11)),
                ('facebook', models.URLField(max_length=100)),
                ('ativo', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='categoria.Categoria')),
            ],
            options={
                'db_table': 'tb_estabelecimento',
            },
        ),
    ]
