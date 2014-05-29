# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_grocerylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('instance', models.ForeignKey(to_field='id', to='core.Instance')),
                ('done', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'task',
            },
            bases=(models.Model,),
        ),
    ]
