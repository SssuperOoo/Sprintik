# Generated by Django 5.0.6 on 2024-07-02 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default='1A', max_length=2)),
                ('summer', models.CharField(choices=[('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default='1A', max_length=2)),
                ('autumn', models.CharField(choices=[('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default='1A', max_length=2)),
                ('spring', models.CharField(choices=[('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A')], default='1A', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('fam', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('otc', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_title', models.CharField(max_length=255)),
                ('connect', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'в работе'), ('accepted', 'принятно'), ('rejected', 'отклонено')], default='new', max_length=10)),
                ('coord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coord', to='sprint.coord')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='sprint.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='sprint.user')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='sprint.pereval')),
            ],
        ),
    ]
