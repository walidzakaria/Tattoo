# Generated by Django 5.1.6 on 2025-03-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0013_whychooseus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whychooseus',
            name='description',
        ),
        migrations.AddField(
            model_name='whychooseus',
            name='section_a',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whychooseus',
            name='section_b',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
