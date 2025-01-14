# Generated by Django 4.1.7 on 2023-02-21 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCategoria', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table': 'categorias_productos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreProducto', models.CharField(max_length=100, verbose_name='Nombre')),
                ('precio', models.PositiveBigIntegerField(verbose_name='Precio')),
                ('StockDisponible', models.PositiveIntegerField(verbose_name='Precio')),
                ('Descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('FechaVencimiento', models.DateField()),
                ('Foto', models.ImageField(upload_to='')),
                ('Categoria', models.ManyToManyField(to='core.categoriaproducto', verbose_name='Categoría')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca', verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'productos',
            },
        ),
    ]
