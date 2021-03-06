# Generated by Django 2.1.7 on 2019-03-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('ccount', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cstar', models.IntegerField(max_length=1)),
                ('ctime', models.DateTimeField()),
                ('rate', models.IntegerField(max_length=10)),
                ('context', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sellcount', models.IntegerField(max_length=10)),
                ('viewcount', models.IntegerField(max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('pnumber', models.IntegerField(max_length=10)),
                ('star', models.IntegerField(default=0, max_length=1)),
                ('homerecommend', models.BooleanField(default=False)),
                ('kind', models.ForeignKey(on_delete='CASCADE', to='product.kind')),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=15)),
                ('ueaddress', models.CharField(max_length=50)),
                ('upassword', models.CharField(max_length=16)),
                ('uLastLoginTime', models.DateTimeField(auto_now=True)),
                ('uBrithday', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='product.tags'),
        ),
        migrations.AddField(
            model_name='comment',
            name='cproduct',
            field=models.ForeignKey(on_delete='CASCADE', to='product.product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='cuser',
            field=models.ForeignKey(on_delete='CASCADE', to='product.user'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cproduct',
            field=models.ForeignKey(on_delete='CASCADE', to='product.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cuser',
            field=models.ForeignKey(on_delete='CASCADE', to='product.user'),
        ),
    ]
