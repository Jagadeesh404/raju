# Generated by Django 4.1 on 2023-12-12 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_rename_pnumber_apjobs_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apjobs',
            name='address',
            field=models.CharField(max_length=910),
        ),
        migrations.AlterField(
            model_name='apjobs',
            name='company',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='apjobs',
            name='eligibility',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='apjobs',
            name='title',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='address',
            field=models.CharField(max_length=910),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='company',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='eligibility',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='title',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='kajobs',
            name='address',
            field=models.CharField(max_length=910),
        ),
        migrations.AlterField(
            model_name='kajobs',
            name='company',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='kajobs',
            name='eligibility',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='kajobs',
            name='title',
            field=models.CharField(max_length=90),
        ),
    ]
