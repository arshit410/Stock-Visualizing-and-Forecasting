# Generated by Django 4.0.1 on 2022-02-02 04:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyFundamentals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('sector', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
                ('pe', models.FloatField()),
                ('pb', models.FloatField()),
                ('div', models.FloatField()),
                ('volume', models.BigIntegerField()),
                ('marketcap', models.BigIntegerField()),
                ('yearhigh', models.FloatField()),
                ('yearlow', models.FloatField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
