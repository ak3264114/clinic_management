# Generated by Django 4.0.1 on 2022-02-23 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='add_Pincode',
            field=models.IntegerField(default=831001),
        ),
        migrations.AddField(
            model_name='patient',
            name='add_city',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='add_line_1',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='add_state',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='image',
            field=models.ImageField(default=1, upload_to='asset/profile-pic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Patient', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='asset/profile-pic')),
                ('add_line_1', models.CharField(max_length=50)),
                ('add_city', models.CharField(max_length=50)),
                ('add_state', models.CharField(max_length=20)),
                ('add_Pincode', models.IntegerField(default=831001)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]