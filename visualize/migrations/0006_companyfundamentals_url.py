# Generated by Django 4.0.1 on 2022-02-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0005_alter_companyfundamentals_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyfundamentals',
            name='url',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
