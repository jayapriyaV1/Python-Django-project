# Generated by Django 5.0.3 on 2024-03-26 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankloan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=70)),
                ('credit_score', models.IntegerField()),
                ('occupation', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('income', models.IntegerField()),
                ('loan_type', models.CharField(max_length=20)),
            ],
        ),
    ]