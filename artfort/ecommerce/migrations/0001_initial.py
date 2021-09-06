# Generated by Django 3.2.5 on 2021-09-05 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('product_desc', models.CharField(default='', max_length=200)),
                ('pub_date', models.DateField()),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
