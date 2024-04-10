# Generated by Django 2.1.15 on 2024-04-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('rol', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=2)),
                ('telefono', models.CharField(max_length=20)),
                ('empresa', models.CharField(max_length=200)),
                ('empleados', models.CharField(max_length=20)),
                ('sector', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registromodelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_1', models.CharField(max_length=255)),
                ('respuesta_2', models.CharField(max_length=255)),
                ('respuesta_3', models.CharField(max_length=255)),
                ('respuesta_4', models.CharField(max_length=255)),
                ('respuesta_5', models.CharField(max_length=255)),
                ('respuesta_6', models.CharField(max_length=255)),
                ('respuesta_7', models.CharField(max_length=255)),
                ('respuesta_8', models.CharField(max_length=255)),
                ('respuesta_9', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Respuestascuatro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_28', models.CharField(max_length=255)),
                ('respuesta_29', models.CharField(max_length=255)),
                ('respuesta_30', models.CharField(max_length=255)),
                ('respuesta_31', models.CharField(max_length=255)),
                ('respuesta_32', models.CharField(max_length=255)),
                ('respuesta_33', models.CharField(max_length=255)),
                ('respuesta_34', models.CharField(max_length=255)),
                ('respuesta_35', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Respuestasdos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_10', models.CharField(max_length=255)),
                ('respuesta_11', models.CharField(max_length=255)),
                ('respuesta_12', models.CharField(max_length=255)),
                ('respuesta_13', models.CharField(max_length=255)),
                ('respuesta_14', models.CharField(max_length=255)),
                ('respuesta_15', models.CharField(max_length=255)),
                ('respuesta_16', models.CharField(max_length=255)),
                ('respuesta_17', models.CharField(max_length=255)),
                ('respuesta_18', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Respuestastres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_19', models.CharField(max_length=255)),
                ('respuesta_20', models.CharField(max_length=255)),
                ('respuesta_21', models.CharField(max_length=255)),
                ('respuesta_22', models.CharField(max_length=255)),
                ('respuesta_23', models.CharField(max_length=255)),
                ('respuesta_24', models.CharField(max_length=255)),
                ('respuesta_25', models.CharField(max_length=255)),
                ('respuesta_26', models.CharField(max_length=255)),
                ('respuesta_27', models.CharField(max_length=255)),
            ],
        ),
    ]
