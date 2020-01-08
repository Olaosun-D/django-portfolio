# Generated by Django 2.2.7 on 2019-12-20 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191220_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='front_page_image',
            field=models.ImageField(default='', upload_to='yoo'),
        ),
        migrations.AlterField(
            model_name='details',
            name='about',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.About'),
        ),
    ]
