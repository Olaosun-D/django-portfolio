# Generated by Django 2.2.7 on 2019-12-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191220_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='front_page_image',
            field=models.ImageField(default='', upload_to='about'),
        ),
    ]
