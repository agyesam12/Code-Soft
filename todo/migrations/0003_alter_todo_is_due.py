# Generated by Django 5.1.2 on 2024-10-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_is_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='is_due',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
