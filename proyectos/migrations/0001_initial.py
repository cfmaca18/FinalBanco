# Generated by Django 4.2 on 2023-05-05 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Centros_de_formacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('encargado', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(unique=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
                ('modalidad', models.CharField(choices=[('presencial', 'Presencial'), ('virtual', 'Virtual')], default='presencial', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grupo', models.CharField(max_length=50, unique=True)),
                ('usuarios', models.ManyToManyField(blank=True, related_name='grupos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('aprendiz', 'Aprendiz'), ('instructor', 'Instructor'), ('admin', 'Admin'), ('anonimo', 'Anonimo')], max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Revision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=5000)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='proyectos/foto')),
                ('codigo_fuente', models.URLField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('terminado', 'terminado'), ('en revision', 'en revision'), ('en desarrollo', 'en desarrollo')], default='en revision', max_length=20)),
                ('autor', models.IntegerField(blank=True, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('editado', models.DateTimeField(auto_now=True)),
                ('categorias', models.ManyToManyField(blank=True, null=True, to='proyectos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300, unique=True)),
                ('centros_de_formacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proyectos.centros_de_formacion')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.PositiveIntegerField(unique=True)),
                ('tipo_documento', models.CharField(choices=[('CC', 'CC'), ('TI', 'TI'), ('CE', 'CE'), ('PASAPORTE', 'PASAPORTE')], max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='perfiles')),
                ('web', models.URLField(blank=True, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('editado', models.DateTimeField(auto_now=True)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proyectos.rol')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], max_length=10)),
                ('proyecto', models.IntegerField()),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.ficha')),
                ('nombre_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.grupo')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.perfil')),
            ],
        ),
        migrations.AddField(
            model_name='ficha',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proyectos.programa'),
        ),
        migrations.CreateModel(
            name='Equipo_trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_grupo', models.CharField(max_length=15, unique=True)),
                ('proyecto', models.IntegerField(blank=True, null=True)),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proyectos.ficha')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proyectos.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.CharField(blank=True, choices=[('aprobado', 'Aprobado'), ('desaprobado', 'desaprobado')], max_length=20, null=True)),
                ('descripcion_entrega', models.CharField(max_length=5000)),
                ('respuesta_instructor', models.CharField(blank=True, max_length=5000, null=True)),
                ('instructor', models.CharField(blank=True, max_length=300, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('editado', models.DateTimeField(auto_now=True)),
                ('aprendiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.equipo_trabajo')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proyectos.proyecto')),
                ('tipo_revision', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proyectos.tipo_revision')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.FileField(upload_to='proyectos/documentos')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('editado', models.DateTimeField(auto_now=True)),
                ('entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.entrega')),
            ],
        ),
        migrations.AddField(
            model_name='centros_de_formacion',
            name='regional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proyectos.regional'),
        ),
    ]
