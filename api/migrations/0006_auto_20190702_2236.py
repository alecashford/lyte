# Generated by Django 2.2.3 on 2019-07-02 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organization_id',
            field=models.BigIntegerField(default=1),
        ),
    ]
