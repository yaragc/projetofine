# Generated by Django 4.2.5 on 2023-09-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserva",
            name="categoria_empresa",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="cnpj",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="nome_empresa",
            field=models.CharField(max_length=100),
        ),
    ]
