# Generated by Django 3.1.5 on 2021-03-11 18:33

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0005_booktree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktree',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='SocialBookApp.booktree'),
        ),
    ]
