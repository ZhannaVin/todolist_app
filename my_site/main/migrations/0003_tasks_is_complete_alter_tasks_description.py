# Generated by Django 4.1.7 on 2023-02-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_tasks_date_tasks_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='Завершено'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.CharField(max_length=50, verbose_name='Задача'),
        ),
    ]
