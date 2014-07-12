# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(choices=[('EV', 'Event'), ('GL', 'Grocery List'), ('TA', 'Task')], max_length=2)),
                ('cron', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'routine',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('routine', models.ForeignKey(to_field='id', to='core.Routine')),
                ('occurrence', models.DateTimeField()),
            ],
            options={
                'db_table': 'instance',
            },
            bases=(models.Model,),
        ),
    ]
