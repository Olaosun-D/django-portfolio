# Generated by Django 2.2.7 on 2019-12-20 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191220_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='about',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.About'),
        ),
    ]
