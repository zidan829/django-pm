# Generated by Django 4.2.7 on 2023-11-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projects_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
