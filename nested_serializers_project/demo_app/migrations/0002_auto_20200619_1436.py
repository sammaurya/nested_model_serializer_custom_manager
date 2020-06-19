# Generated by Django 3.0.7 on 2020-06-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='market',
            options={'ordering': ('id', 'name', 'sport')},
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ('id', 'name', 'startTime', 'sport', 'market'), 'verbose_name_plural': 'Matches'},
        ),
        migrations.AlterModelOptions(
            name='selection',
            options={'ordering': ('id', 'name', 'odds', 'market')},
        ),
        migrations.AlterModelOptions(
            name='sport',
            options={'ordering': ('id', 'name')},
        ),
        migrations.AddField(
            model_name='match',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
