# Generated by Django 2.2.3 on 2019-07-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]