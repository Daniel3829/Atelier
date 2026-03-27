import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_matricula', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='matriculas',
                    to='cursos.curso',
                )),
                ('estudiante', models.ForeignKey(
                    limit_choices_to={'rol': 'ESTUDIANTE'},
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='matriculas',
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={
                'verbose_name': 'Matricula',
                'verbose_name_plural': 'Matriculas',
                'ordering': ['-fecha_matricula'],
                'unique_together': {('estudiante', 'curso')},
            },
        ),
    ]
