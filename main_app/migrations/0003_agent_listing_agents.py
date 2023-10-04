# Generated by Django 4.2.5 on 2023-10-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_listing_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='agents',
            field=models.ManyToManyField(to='main_app.agent'),
        ),
    ]
