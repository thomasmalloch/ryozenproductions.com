# Generated by Django 3.1.2 on 2020-11-07 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': [('change_other', "User can edit other another user's comment"), ('delete_other', "User can delete another user's comment")]},
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='description',
            field=models.CharField(default='Chapter Description', max_length=100, verbose_name='Description:'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(default='New Chapter', max_length=100, verbose_name='Title:'),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='projects.Tag'),
        ),
    ]
