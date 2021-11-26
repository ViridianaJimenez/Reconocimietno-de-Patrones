# Generated by Django 3.2.9 on 2021-11-26 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tejido_temperatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='tejido',
            name='color',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tejido',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
