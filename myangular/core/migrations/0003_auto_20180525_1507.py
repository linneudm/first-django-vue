# Generated by Django 2.0.5 on 2018-05-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_agenda_publicado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='id',
        ),
        migrations.AddField(
            model_name='agenda',
            name='agenda_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
