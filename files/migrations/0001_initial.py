import os
import csv

from datetime import datetime, timezone

import django.db.models.deletion

from django.db import migrations, models
from django.conf import settings


def populate_data(apps, schema_editor):

    def _get_entry_data(data):
        timestamp = datetime.fromtimestamp(int(data[1]), tz=timezone.utc)
        entry_data = {'experiment_id': data[0], 'timestamp': timestamp, 'value': data[2]}

        return entry_data


    Entry = apps.get_model('aether', 'Entry')
    Experiment = apps.get_model('aether', 'Experiment')

    entry_data = []

    dir_path = os.path.dirname(os.path.realpath(__file__))
    entry_data_path = os.path.join(dir_path, 'data', 'input_data.csv')
    with open(entry_data_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        entry_data = [_get_entry_data(row) for row in reader]


    experiment_data = []
    for data in entry_data:
        experiment_id = data['experiment_id']
        if experiment_id not in experiment_data:
            experiment_data.append(experiment_id)


    entries = [Entry(**entry) for entry in entry_data]
    experiments = [Experiment(id=experiment_id) for experiment_id in experiment_data]

    Experiment.objects.bulk_create(experiments, batch_size=settings.BATCH_SIZE)
    Entry.objects.bulk_create(entries, batch_size=settings.BATCH_SIZE)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('value', models.IntegerField()),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aether.experiment')),
            ],
        ),
        migrations.RunPython(populate_data),
    ]
