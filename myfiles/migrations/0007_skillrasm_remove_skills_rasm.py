# Generated by Django 4.1.3 on 2022-12-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0006_delete_skillrasm_skills_rasm'),
    ]

    operations = [
        migrations.CreateModel(
            name='skillrasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='madia')),
            ],
        ),
        migrations.RemoveField(
            model_name='skills',
            name='rasm',
        ),
    ]
