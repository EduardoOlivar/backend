# Generated by Django 4.1.2 on 2023-05-15 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_answer_essays'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='essays',
            new_name='essay',
        ),
    ]
