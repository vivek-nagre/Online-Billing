# Generated by Django 3.2.9 on 2022-07-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cust_Detals',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SR_No', models.TextField(max_length=255)),
                ('Date', models.DateTimeField(max_length=255, unique=True)),
                ('Cust_name', models.CharField(max_length=50)),
                ('Mobile', models.IntegerField()),
                ('WeightK', models.IntegerField()),
                ('WeightG', models.IntegerField()),
            ],
        ),
    ]
