# Generated by Django 3.0.6 on 2020-05-09 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_of_institute', models.CharField(choices=[('c', 'college'), ('h', 'high school')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_number', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('gender', models.CharField(choices=[('f', 'female'), ('m', 'male'), ('u', 'undisclosed')], max_length=1)),
                ('percentage', models.FloatField()),
                ('institute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Institute')),
            ],
        ),
    ]
