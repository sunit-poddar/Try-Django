# Generated by Django 2.1 on 2018-09-22 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('number_of_employee', models.PositiveIntegerField()),
                ('establishment', models.DateField()),
                ('website', models.URLField()),
                ('ceo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]