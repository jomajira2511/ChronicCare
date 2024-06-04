# Generated by Django 5.0.6 on 2024-06-01 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categoria',
            field=models.CharField(choices=[('AR', 'Articulos'), ('RE', 'Revistas'), ('VI', 'Videos')], default='AR', max_length=3),
        ),
    ]