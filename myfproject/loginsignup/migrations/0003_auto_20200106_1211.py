# Generated by Django 2.2 on 2020-01-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsignup', '0002_auto_20200106_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchaccounts',
            name='yearsCompleted',
            field=models.IntegerField(choices=[('1', '1 year'), ('2', '2 years'), ('3', '3 years')], max_length=1),
        ),
    ]
