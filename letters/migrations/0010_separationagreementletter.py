# Generated by Django 5.1 on 2024-09-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0009_terminationletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeparationAgreementLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.CharField(max_length=255)),
                ('terminationDate', models.DateField()),
                ('finalSettlement', models.CharField(max_length=255)),
                ('confidentialityTerms', models.TextField()),
                ('managerName', models.CharField(max_length=255)),
                ('companyName', models.CharField(max_length=255)),
            ],
        ),
    ]
