# Generated by Django 2.1.5 on 2019-03-18 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0002_auto_20190211_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantMascotas', models.IntegerField()),
                ('razones', models.TextField()),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Persona')),
            ],
        ),
    ]
