# Generated by Django 5.1 on 2024-09-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0011_warningletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceReviewLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.CharField(max_length=100)),
                ('reviewPeriod', models.CharField(max_length=100)),
                ('reviewSummary', models.TextField()),
                ('strengths', models.TextField()),
                ('areasForImprovement', models.TextField()),
                ('managerName', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
            ],
        ),
    ]
