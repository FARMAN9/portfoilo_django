# Generated by Django 5.0.6 on 2024-07-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('link', models.URLField(null=True)),
                ('image1', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Eduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('frm', models.CharField(max_length=100)),
                ('to', models.CharField(default='Present', max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='mainx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(default=' ', max_length=100, null=True)),
                ('cantact', models.CharField(default=' ', max_length=100, null=True)),
                ('portfilo', models.CharField(default=' ', max_length=100, null=True)),
                ('resume', models.CharField(default=' ', max_length=100, null=True)),
                ('Skills', models.CharField(default=' ', max_length=100, null=True)),
                ('certificates', models.CharField(default=' ', max_length=100, null=True)),
                ('profile', models.ImageField(upload_to='images/')),
                ('background', models.ImageField(upload_to='images/')),
                ('iam1', models.CharField(default='Developer', max_length=100, null=True)),
                ('iam2', models.CharField(default='Developer', max_length=100, null=True)),
                ('iam3', models.CharField(default='Developer', max_length=100, null=True)),
                ('iam4', models.CharField(default='Developer', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professional_Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('frm', models.CharField(max_length=100)),
                ('to', models.CharField(default='present', max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('p1', models.CharField(max_length=255)),
                ('p2', models.CharField(max_length=255)),
                ('p3', models.CharField(max_length=255)),
                ('p4', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('project_url', models.URLField(null=True)),
                ('client', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('val', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='summery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summery', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('name', models.CharField(default='Syed Farman Ali', max_length=100, null=True)),
            ],
        ),
    ]
