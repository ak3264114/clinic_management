# Generated by Django 4.0.1 on 2022-02-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='about',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='add_Pincode',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_no',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='add_Pincode',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_no',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
