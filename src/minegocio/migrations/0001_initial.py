# Generated by Django 5.1.4 on 2024-12-16 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=13)),
                ('dni', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.CharField(choices=[('C', 'Celulares'), ('AU', 'Auriculares'), ('PE', 'Pequeños electrodomésticos'), ('T', 'Tablets')], default='PE', max_length=50)),
                ('dni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minegocio.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.PositiveIntegerField()),
                ('informe', models.CharField(max_length=25)),
                ('periodo', models.CharField(choices=[('MENSUAL', 'Mensual'), ('TRIMESTRAL', 'Trimestral'), ('ANUAL', 'Anual')], default='ANUAL', max_length=10)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='minegocio.transaccion')),
                ('dni', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='minegocio.vendedor')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('año', 'producto', 'periodo'), name='unico_informe_por_año')],
            },
        ),
    ]
