# Generated by Django 2.1.5 on 2019-02-10 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0003_service_description'),
        ('services', '0018_auto_20190207_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='subservicepage',
            name='parent_service',
            field=models.ForeignKey(blank=True, help_text='Link to this service in taxonomy', null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxonomy.Service'),
        ),
    ]
