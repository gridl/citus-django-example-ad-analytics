# Generated by Django 2.1.7 on 2019-03-15 16:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_analytics', '0003_campaign_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='blacklisted_site_urls',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
    ]
