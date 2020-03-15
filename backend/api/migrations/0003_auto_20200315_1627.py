# Generated by Django 3.0.4 on 2020-03-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_entry_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cashdetails',
            options={'get_latest_by': '-date', 'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-date', 'type']},
        ),
        migrations.AlterModelOptions(
            name='salesummary',
            options={'get_latest_by': '-date', 'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='settlement',
            options={'get_latest_by': '-date', 'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateField(),
        ),
    ]