# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('instance', models.ForeignKey(to_field='id', to='core.Instance')),
                ('timestamp', models.DateTimeField()),
                ('nickname', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'comment',
            },
            bases=(models.Model,),
        ),
    ]
