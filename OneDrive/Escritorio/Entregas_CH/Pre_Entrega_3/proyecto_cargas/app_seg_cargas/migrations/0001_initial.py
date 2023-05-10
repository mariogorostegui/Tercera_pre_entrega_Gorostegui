# Generated by Django 4.2.1 on 2023-05-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fwr', models.CharField(max_length=64)),
                ('abrev_fwr', models.CharField(max_length=6)),
                ('ctc_fwr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cargas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mawb', models.CharField(max_length=12)),
                ('hawb', models.CharField(max_length=12)),
                ('incoterm', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=64)),
                ('abrev_fwr', models.CharField(max_length=6)),
                ('cotizacion', models.FloatField()),
                ('bultos', models.IntegerField()),
                ('peso', models.FloatField()),
                ('volumen', models.FloatField()),
                ('atd', models.DateField()),
                ('ata', models.DateField()),
                ('estado', models.CharField(max_length=12)),
                ('retiro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('area', models.CharField(max_length=64)),
            ],
        ),
    ]