# Generated by Django 2.1.7 on 2019-03-27 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190327_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='homerecommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hcomment1', models.CharField(max_length=4)),
                ('hcomment2', models.CharField(max_length=4)),
                ('hcomment3', models.CharField(max_length=4)),
                ('himage', models.ImageField(upload_to='recommend/')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='homerecommend',
        ),
        migrations.AddField(
            model_name='homerecommend',
            name='hproduct',
            field=models.ForeignKey(on_delete='CASCADE', to='product.product'),
        ),
    ]