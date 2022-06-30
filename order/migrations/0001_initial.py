# Generated by Django 2.2.6 on 2020-02-27 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dishes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('full_price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('adress', models.CharField(blank=True, max_length=255, null=True)),
                ('dishes', models.ManyToManyField(blank=True, null=True, to='dishes.InstanceDish')),
                ('drinks', models.ManyToManyField(blank=True, null=True, to='dishes.InstanceDrink')),
                ('user_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
