# Generated by Django 2.1 on 2019-06-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190607_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opiniao',
            name='contras',
        ),
        migrations.RemoveField(
            model_name='opiniao',
            name='geral',
        ),
        migrations.RemoveField(
            model_name='opiniao',
            name='pros',
        ),
        migrations.RemoveField(
            model_name='opiniao',
            name='titulo',
        ),
        migrations.AddField(
            model_name='opiniao',
            name='consumo',
            field=models.IntegerField(default=0, verbose_name='Consumo'),
        ),
        migrations.AddField(
            model_name='opiniao',
            name='desempenho',
            field=models.IntegerField(default=0, verbose_name='Desempenho'),
        ),
        migrations.AddField(
            model_name='opiniao',
            name='interior',
            field=models.IntegerField(default=0, verbose_name='Interior'),
        ),
        migrations.AddField(
            model_name='opiniao',
            name='opiniao',
            field=models.TextField(default='dummy', verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='opiniao',
            name='acabamento',
            field=models.IntegerField(default=0, verbose_name='Acabamento'),
        ),
        migrations.AlterField(
            model_name='opiniao',
            name='estilo',
            field=models.IntegerField(default=0, verbose_name='Estilo'),
        ),
        migrations.AlterField(
            model_name='opiniao',
            name='idCarro',
            field=models.IntegerField(default=1, verbose_name='idCarro'),
        ),
    ]