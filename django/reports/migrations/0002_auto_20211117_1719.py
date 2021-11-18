# Generated by Django 3.1.13 on 2021-11-17 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reported_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_reports', to=settings.AUTH_USER_MODEL, verbose_name='Reportado Por'),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_reports', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]