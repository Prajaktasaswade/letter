# Generated by Django 5.1 on 2024-09-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0006_transferletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.CharField(max_length=100)),
                ('leaveType', models.CharField(max_length=50)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('managerName', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
            ],
        ),
    ]
