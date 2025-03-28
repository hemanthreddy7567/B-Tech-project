# Generated by Django 2.2.3 on 2020-07-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique='True')),
                ('password', models.CharField(max_length=40)),
                ('conformpassword', models.CharField(max_length=40)),
                ('mobileno', models.CharField(default='', max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'userregister',
            },
        ),
        migrations.CreateModel(
            name='viewdetailsmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('file', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'userviewdetailsmodel',
            },
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
