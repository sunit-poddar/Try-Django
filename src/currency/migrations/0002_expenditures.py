# Generated by Django 2.1 on 2018-09-22 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditures',
            fields=[
                ('transactions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='currency.Transactions')),
                ('notes', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('currency.transactions', models.Model),
        ),
    ]
