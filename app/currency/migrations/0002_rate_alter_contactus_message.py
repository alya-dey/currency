# Generated by Django 4.0.6 on 2022-07-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_currency_type', models.CharField(max_length=3)),
                ('currency_type', models.CharField(max_length=3)),
                ('sale', models.DecimalField(decimal_places=4, max_digits=10)),
                ('buy', models.DecimalField(decimal_places=4, max_digits=10)),
                ('source', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=10000),
        ),
    ]