# Generated by Django 5.0.7 on 2024-08-05 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_details', '0003_alter_post_id_alter_worker_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LittleHeadName', models.CharField(max_length=20)),
                ('LittleTextInfo', models.TextField(max_length=100)),
                ('LargeHeadName', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='images/')),
                ('DetailHead', models.CharField(max_length=25)),
                ('DetailText', models.TextField()),
            ],
        ),
    ]
