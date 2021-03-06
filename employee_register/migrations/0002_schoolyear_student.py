# Generated by Django 3.0.3 on 2020-02-29 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('home_address', models.CharField(max_length=20)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.SchoolYear')),
            ],
        ),
    ]
