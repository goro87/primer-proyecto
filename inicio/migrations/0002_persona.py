# Generated by Django 4.2.2 on 2023-06-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Persona', models.CharField(max_length=20)),
                ('edad_Persona', models.IntegerField()),
            ],
        ),
    ]