# Generated by Django 2.2 on 2020-01-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=25)),
                ('Yearstart', models.IntegerField(max_length=4)),
                ('yearsCompleted', models.IntegerField(choices=[('1', '1 year'), ('2', '2 years'), ('3', '3 years')])),
                ('Invester', models.IntegerField(max_length=7)),
                ('total_profit', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Companybranches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_Lname', models.CharField(max_length=25)),
                ('Manager_Name', models.CharField(max_length=25)),
                ('branch_ConNo', models.IntegerField(max_length=10)),
                ('branch_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=25)),
                ('name_emp', models.CharField(max_length=25)),
                ('Yearofjoin', models.IntegerField(max_length=4)),
                ('Designation', models.CharField(choices=[('m', 'manager'), ('P', 'Programer analyst'), ('A', 'Assosiate')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=25)),
                ('totalemp_branch', models.IntegerField(max_length=800)),
                ('number_projects', models.IntegerField(max_length=10)),
                ('project_name', models.CharField(max_length=50)),
                ('manager_name', models.CharField(max_length=25)),
                ('emp_inproject', models.IntegerField(max_length=100)),
                ('projectincome', models.IntegerField(max_length=7)),
            ],
        ),
    ]
