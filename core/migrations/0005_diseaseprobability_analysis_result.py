# Generated by Django 2.0.3 on 2018-05-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0004_auto_20180515_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseaseprobability',
            name='analysis_result',
            field=models.ManyToManyField(related_name='diseases_prob', to='core.AnalysisParams',
                                         verbose_name='выявленные отклонения в анализах'),
        ),
    ]