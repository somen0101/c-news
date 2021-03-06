# Generated by Django 2.2.5 on 2020-03-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200330_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='topic_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='topics',
            name='author',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='topics',
            name='image_url',
            field=models.TextField(null=True),
        ),
    ]
