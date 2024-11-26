# Generated by Django 5.1.3 on 2024-11-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del cliente')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido del cliente')),
                ('telefono', models.CharField(max_length=20, verbose_name='Telefono del cliente')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('edad', models.PositiveIntegerField()),
                ('genero', models.CharField(choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre')], default='Hombre', max_length=30, verbose_name='Género')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]