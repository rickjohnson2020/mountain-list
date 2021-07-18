# Generated by Django 3.1.7 on 2021-07-10 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mountain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mountain_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('height', models.PositiveIntegerField()),
                ('difficulty', models.CharField(max_length=100)),
                ('days_to_climb', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]