# Generated by Django 4.2.7 on 2024-01-13 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_sub_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='sub_comment',
            new_name='parent',
        ),
    ]
