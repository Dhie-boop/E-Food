# Generated by Django 3.0.4 on 2020-07-20 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('specifications', models.CharField(default='Non-Jain/Medium Spicy', max_length=200)),
                ('delivery_date', models.DateField(default=timezone.now, max_length=100)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
