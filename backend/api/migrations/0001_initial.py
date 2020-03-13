# Generated by Django 3.0.4 on 2020-03-10 14:40

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=50)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=50)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaleSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('data', jsonfield.fields.JSONField(null=True)),
                ('sale', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=50)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('entity_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.EntityType')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CR', 'CREDIT'), ('DE', 'DEBIT')], default='CR', max_length=2)),
                ('mode', models.CharField(choices=[('CA', 'CASH'), ('AC', 'ACCOUNT'), ('TR', 'TREASURE')], default='CA', max_length=2)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(max_length=50)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.EntryCategory')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Entity')),
                ('settlement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Settlement')),
            ],
        ),
        migrations.AddField(
            model_name='entity',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ExpenseCategory'),
        ),
        migrations.AddField(
            model_name='entity',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.EntityType'),
        ),
    ]
