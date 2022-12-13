# Generated by Django 4.1.3 on 2022-12-13 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compartilhamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ligacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('cabo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='compartilhamento.cabo')),
                ('ponto_a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ponto_a_ligacao', to='compartilhamento.ponto')),
                ('ponto_b', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ponto_b_ligacao', to='compartilhamento.ponto')),
                ('rota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rota_ligacao', to='compartilhamento.rota')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trajeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('ligacao', models.ManyToManyField(to='maps.ligacao')),
                ('rota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rota_trajeto', to='compartilhamento.rota')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
