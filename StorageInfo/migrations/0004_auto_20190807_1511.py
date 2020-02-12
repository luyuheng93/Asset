# Generated by Django 2.2.4 on 2019-08-07 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StorageInfo', '0003_auto_20190807_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanswitch',
            name='domain_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Domain_ID'),
        ),
        migrations.AddField(
            model_name='storagedevice',
            name='memo',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='storagedevice',
            name='nas_ip',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='NAS_IP'),
        ),
        migrations.AddField(
            model_name='storagedevice',
            name='vsp_ip',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='VSP/管理机IP'),
        ),
    ]