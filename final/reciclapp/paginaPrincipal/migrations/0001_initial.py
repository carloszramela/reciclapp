# Generated by Django 3.0 on 2020-09-11 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desecho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_aprox', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Oferente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('movilidad', models.BooleanField()),
                ('horario_contacto', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDesecho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metal', models.BooleanField()),
                ('bombilladeluz', models.BooleanField()),
                ('escombros', models.BooleanField()),
                ('carton', models.BooleanField()),
                ('vidrio', models.BooleanField()),
                ('madera', models.BooleanField()),
                ('desechoselectronicos', models.BooleanField()),
                ('baterias', models.BooleanField()),
            ],
        ),
    ]
