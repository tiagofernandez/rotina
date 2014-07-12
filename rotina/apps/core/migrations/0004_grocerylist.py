# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('instance', models.ForeignKey(to_field='id', to='core.Instance')),
                ('items', models.TextField(default='{}')),
            ],
            options={
                'db_table': 'grocery_list',
            },
            bases=(models.Model,),
        ),
    ]
