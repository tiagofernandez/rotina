# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('instance', models.ForeignKey(to_field='id', to='core.Instance')),
                ('nickname', models.CharField(max_length=20)),
                ('rsvp', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('M', 'Maybe')], max_length=1)),
            ],
            options={
                'db_table': 'event',
            },
            bases=(models.Model,),
        ),
    ]
