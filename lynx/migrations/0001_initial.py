# Generated by Django 4.2.5 on 2023-09-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exceldata',
            fields=[
                ('Chr', models.CharField(db_index=True, max_length=200)),
                ('Start', models.IntegerField(primary_key=True, serialize=False)),
                ('End', models.IntegerField()),
                ('Ref', models.CharField(max_length=10)),
                ('Alt', models.CharField(max_length=10)),
                ('Func_refGene', models.CharField(max_length=200)),
                ('ExonicFunc_refGene', models.CharField(max_length=200)),
                ('OMIM', models.IntegerField()),
                ('dbSNP_ID', models.CharField(max_length=200)),
                ('ClinVar_Sig', models.CharField(max_length=200)),
                ('Ref_Gene', models.CharField(max_length=200)),
                ('InterVar_InterVar', models.CharField(max_length=1000)),
                ('Freq_gnomAD_genome_ALL', models.CharField(max_length=200)),
                ('Freq_esp6500siv2_all', models.CharField(max_length=200)),
                ('Freq_1000g2015aug_all', models.CharField(max_length=200)),
                ('CADD_raw', models.CharField(max_length=200)),
                ('CADD_phred', models.CharField(max_length=200)),
                ('SIFT_score', models.CharField(max_length=200)),
            ],
        ),
    ]
