# Generated by Django 3.0.4 on 2020-03-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200325_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='type',
            field=models.CharField(choices=[('DE', 'DEBIT'), ('CR', 'CREDIT')], default='DE', max_length=2),
        ),
    ]