# Generated by Django 2.0.1 on 2019-04-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chengzaiwang', '0002_remove_chengzaiwang_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='chengzaiwang',
            name='status',
            field=models.CharField(default='未出库', max_length=100),
        ),
    ]
