# Generated by Django 5.2 on 2025-05-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuarioSenhaHash',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
