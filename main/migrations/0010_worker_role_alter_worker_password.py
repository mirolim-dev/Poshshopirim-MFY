# Generated by Django 4.2.4 on 2023-08-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_worker_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='role',
            field=models.CharField(max_length=30, null=True, verbose_name='Lavozim'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='password',
            field=models.CharField(default='69lY6Gtv', help_text='Ushbu parol         Xodimning tizimga kirishida ishlatiladi', max_length=10, verbose_name='Parol'),
        ),
    ]