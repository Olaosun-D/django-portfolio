# Generated by Django 2.2.7 on 2020-01-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20200105_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_image_2',
            field=models.ImageField(blank=True, default='/assets/projects_placeholder.jpg', upload_to='projects'),
        ),
    ]