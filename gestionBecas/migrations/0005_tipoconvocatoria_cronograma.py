# Generated by Django 4.2.5 on 2023-10-24 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBecas', '0004_programabeca'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoConvocatoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cronograma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripciones', models.DateField()),
                ('fecha_cierre_inscripciones', models.DateField()),
                ('fecha_seleccion_aspirantes', models.DateField()),
                ('fecha_entrevistas', models.DateField()),
                ('fecha_publicacion_beneficiarios', models.DateField()),
                ('programa_becas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionBecas.programabeca')),
                ('tipo_convocatoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionBecas.tipoconvocatoria')),
            ],
        ),
    ]