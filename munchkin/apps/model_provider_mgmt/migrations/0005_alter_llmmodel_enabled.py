# Generated by Django 4.2.7 on 2024-06-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_provider_mgmt', '0004_llmmodel_enabled_alter_llmskill_skill_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llmmodel',
            name='enabled',
            field=models.BooleanField(default=False, verbose_name='启用'),
        ),
    ]
