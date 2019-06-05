# Generated by Django 2.1 on 2019-06-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('ano', models.IntegerField(verbose_name='Ano')),
                ('segmento', models.CharField(max_length=50, verbose_name='Segmento')),
                ('numVendas', models.IntegerField(verbose_name='numVendas')),
                ('precoFipe', models.FloatField(verbose_name='PrecoFipe')),
            ],
        ),
    ]