# Generated by Django 3.2.4 on 2021-08-14 22:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('phone_ext', models.CharField(max_length=4)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('profile_image', models.URLField()),
                ('is_business', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('images', models.URLField()),
                ('is_available', models.BooleanField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(choices=[(1.0, 1.0), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0)], decimal_places=1, max_digits=2)),
                ('review', models.TextField()),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_business', to='mainApp.user')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_customer', to='mainApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('is_available', models.BooleanField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.service')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('BKD', 'Booked'), ('CND', 'Cancelled')], default='BKD', max_length=3)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.user')),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.package')),
            ],
        ),
    ]
