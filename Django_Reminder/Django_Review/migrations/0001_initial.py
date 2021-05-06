# Generated by Django 3.1.7 on 2021-05-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon_Name', models.CharField(max_length=100)),
                ('weapon_Price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('weapon_Type', models.CharField(choices=[('AN', 'Ammo'), ('FE', 'Fin'), ('HY', 'Heavy'), ('ID', 'Improv'), ('LT', 'Light'), ('LG', 'Load'), ('RD', 'Range'), ('RH', 'Reach'), ('SL', 'Special'), ('TN', 'Thrown'), ('TD', 'TwoHand'), ('VE', 'Vers')], default='AN', max_length=2)),
            ],
        ),
    ]
