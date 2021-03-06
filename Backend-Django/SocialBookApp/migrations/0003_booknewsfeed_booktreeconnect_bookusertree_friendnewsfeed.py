# Generated by Django 3.1.5 on 2021-03-12 20:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0002_bookcomments_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendNewsFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('publist', unixtimestampfield.fields.UnixTimeStampField(auto_now=True, null=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendfriend', to='SocialBookApp.app_user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendyou', to='SocialBookApp.app_user')),
            ],
        ),
        migrations.CreateModel(
            name='BookUserTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tn_ancestors_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Ancestors pks')),
                ('tn_ancestors_count', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Ancestors count')),
                ('tn_children_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Children pks')),
                ('tn_children_count', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Children count')),
                ('tn_depth', models.PositiveSmallIntegerField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Depth')),
                ('tn_descendants_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Descendants pks')),
                ('tn_descendants_count', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Descendants count')),
                ('tn_index', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Index')),
                ('tn_level', models.PositiveSmallIntegerField(default=1, editable=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Level')),
                ('tn_priority', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)], verbose_name='Priority')),
                ('tn_order', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Order')),
                ('tn_siblings_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Siblings pks')),
                ('tn_siblings_count', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Siblings count')),
                ('UserName', models.CharField(max_length=200)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialBookApp.book')),
                ('tn_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tn_children', to='SocialBookApp.bookusertree', verbose_name='Parent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialBookApp.app_user')),
            ],
            options={
                'verbose_name': 'BookUserTree',
                'verbose_name_plural': 'BookUserTrees',
                'ordering': ['tn_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookTreeConnect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tree', models.IntegerField(default=0)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialBookApp.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookNewsFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('publist', unixtimestampfield.fields.UnixTimeStampField(auto_now=True, null=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='youself', to='SocialBookApp.app_user')),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialBookApp.book')),
                ('Buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookBuyer', to='SocialBookApp.app_user')),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedreferrer', to='SocialBookApp.app_user')),
            ],
        ),
    ]
