# Generated by Django 3.0.3 on 2022-05-12 05:45

import cloud_app.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileDetailInfo',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('file_title', models.CharField(max_length=50)),
                ('file_upload', models.DateField()),
                ('file_images', models.TextField()),
                ('file_url', models.TextField()),
                ('owner', djongo.models.fields.EmbeddedField(model_container=cloud_app.models.Owner)),
                ('guest', djongo.models.fields.EmbeddedField(model_container=cloud_app.models.Guest)),
                ('comment', djongo.models.fields.EmbeddedField(model_container=cloud_app.models.Comment)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('images', models.TextField()),
                ('phone_num', models.CharField(max_length=15)),
            ],
        ),
    ]
