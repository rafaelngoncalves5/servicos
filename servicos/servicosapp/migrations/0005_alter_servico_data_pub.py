# Generated by Django 4.1.7 on 2023-02-23 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('servicosapp', '0004_servico_descricao_alter_servico_data_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='data_pub',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de publicação'),
        ),
    ]
