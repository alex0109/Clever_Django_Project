# Generated by Django 3.0.3 on 2020-05-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200426_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]