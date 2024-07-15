# Generated by Django 5.0.6 on 2024-07-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=40000),
        ),
        migrations.AlterField(
            model_name='eduction',
            name='about',
            field=models.CharField(max_length=40000),
        ),
        migrations.AlterField(
            model_name='mainx',
            name='Skills',
            field=models.CharField(default=' ', max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='mainx',
            name='about',
            field=models.CharField(default=' ', max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='mainx',
            name='cantact',
            field=models.CharField(default=' ', max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='mainx',
            name='certificates',
            field=models.CharField(default=' ', max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='mainx',
            name='portfilo',
            field=models.CharField(default=' ', max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='mainx',
            name='resume',
            field=models.CharField(default=' ', max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='professional_experience',
            name='address',
            field=models.CharField(max_length=40000),
        ),
        migrations.AlterField(
            model_name='professional_experience',
            name='p1',
            field=models.CharField(max_length=40000),
        ),
        migrations.AlterField(
            model_name='professional_experience',
            name='p2',
            field=models.CharField(max_length=40000),
        ),
        migrations.AlterField(
            model_name='professional_experience',
            name='p3',
            field=models.CharField(max_length=40000),
        ),
        migrations.AlterField(
            model_name='professional_experience',
            name='p4',
            field=models.CharField(max_length=40000),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='summery',
            name='summery',
            field=models.CharField(max_length=40000),
        ),
    ]