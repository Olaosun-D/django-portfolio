# Generated by Django 2.2.7 on 2019-12-20 05:56

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191218_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='projects',
            name='project_image',
        ),
        migrations.AlterField(
            model_name='projects',
            name='technologies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('html', 'Html'), ('js', 'Javacript'), ('node', 'Node Js'), ('gulp', 'Gulp Js'), ('cs', 'Css'), ('py', 'Python'), ('java', 'Java'), ('Elec', 'Electron'), ('Elec', 'Electron'), ('ps', 'Adobe Photoshop'), ('xd', 'Adobe XD')], max_length=44),
        ),
        migrations.CreateModel(
            name='PostPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_image', models.ImageField(upload_to='blog/post_pics')),
                ('postid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Post')),
            ],
        ),
    ]