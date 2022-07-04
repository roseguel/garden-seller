# Generated by Django 4.0.4 on 2022-06-27 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BuyBeeApp', '0002_alter_envio_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepedido',
            name='producto',
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='BuyBeeApp.productoventa'),
        ),
    ]
