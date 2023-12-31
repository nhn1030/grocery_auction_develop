# Generated by Django 2.2.4 on 2023-11-26 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('buyer_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
                ('user_type', models.CharField(max_length=255)),
                ('user_business_info', models.TextField()),
                ('user_address', models.CharField(max_length=255)),
                ('account_info', models.TextField()),
                ('payment_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateTimeField()),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_status', models.CharField(max_length=255)),
                ('transaction_type', models.CharField(max_length=255)),
                ('is_safe_payment', models.BooleanField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Buyer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('supply_id', models.AutoField(primary_key=True, serialize=False)),
                ('supply_date', models.DateTimeField()),
                ('supply_region', models.CharField(max_length=255)),
                ('supply_item', models.CharField(max_length=255)),
                ('supply_quantity', models.IntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.User')),
            ],
        ),
        migrations.AddField(
            model_name='seller',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='market.User'),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Seller'),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('match_date', models.DateTimeField()),
                ('match_type', models.CharField(max_length=255)),
                ('demender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Buyer')),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Seller')),
            ],
        ),
        migrations.AddField(
            model_name='buyer',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='market.User'),
        ),
    ]
