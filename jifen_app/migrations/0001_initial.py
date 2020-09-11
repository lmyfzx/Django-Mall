# Generated by Django 2.2.15 on 2020-09-02 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop_app', '0003_commodity_label'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Integral_commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity_name', models.CharField(help_text='Please enter the name of the product', max_length=50, verbose_name='商品名称')),
                ('integral_price', models.PositiveIntegerField(verbose_name='积分值')),
                ('surplus', models.PositiveIntegerField(help_text='Quantity of merchandise exchanged', verbose_name='商品剩余量')),
            ],
            options={
                'verbose_name': '积分商品表',
                'verbose_name_plural': '积分商品表',
                'db_table': 'Integral_commodity',
            },
        ),
        migrations.CreateModel(
            name='Integrals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fraction', models.PositiveIntegerField(default=0, verbose_name='积分')),
                ('category', models.CharField(max_length=10, verbose_name='商品种类')),
                ('consumer_time', models.DateTimeField(auto_now_add=True, verbose_name='消费时间')),
                ('commodity', models.ForeignKey(on_delete=False, related_name='integral', to='Shop_app.Commodity', verbose_name='购买的商品')),
                ('user', models.OneToOneField(on_delete=True, related_name='integral', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '积分表',
                'verbose_name_plural': '积分表',
                'db_table': 'Integral',
            },
            managers=[
                ('integral_', django.db.models.manager.Manager()),
            ],
        ),
    ]