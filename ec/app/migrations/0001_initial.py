# Generated by Django 5.0.6 on 2024-05-31 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('fuente', models.CharField(max_length=100)),
                ('idioma', models.CharField(max_length=100)),
                ('fecha_publi', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen_producto', models.ImageField(upload_to='product')),
            ],
        ),
    ]