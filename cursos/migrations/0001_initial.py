import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, default='')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='cursos/')),
                ('duracion', models.PositiveSmallIntegerField(default=1, help_text='Duración en meses (1-12)')),
                ('profesor', models.ForeignKey(
                    blank=True,
                    limit_choices_to={'rol': 'PROFESOR'},
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='cursos_asignados',
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['codigo'],
            },
        ),
    ]
