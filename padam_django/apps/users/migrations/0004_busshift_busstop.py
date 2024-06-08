# Generated by Django 3.2.5 on 2024-06-08 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_auto_20211109_1456'),
        ('users', '0003_auto_20240608_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shifts', to='fleet.bus')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shifts', to='fleet.driver')),
            ],
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField()),
                ('arrival_time', models.DateTimeField()),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='users.busshift')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('shift', 'order')},
            },
        ),
    ]
