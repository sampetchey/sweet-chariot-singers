# Generated by Django 3.2.19 on 2023-08-02 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('voice_type', models.CharField(choices=[('Lead', 'Lead - Singing the tune'), ('Tenor', 'Tenor - Normally a descant higher than the tune'), ('Baritone', 'Baritone - Similar range to Lead, but in harmony with it'), ('Bass', 'Bass - Low register, normally singing the root of the harmony'), ('Any', 'Versatile - Comfortable singing any part'), ('Unknown', "I'm not sure")], default='Lead', max_length=80)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('membership_fee', models.IntegerField(default=30)),
            ],
        ),
    ]
