# Generated by Django 2.1.7 on 2019-03-11 21:34

from django.conf import settings
from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0018_merge_20190307_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='BountyInvites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('status', models.CharField(blank=True, choices=[('pending', 'pending'), ('accepted', 'accepted')], max_length=20)),
                ('bounty', models.ManyToManyField(blank=True, related_name='bounty', to='dashboard.Bounty')),
                ('invitee', models.ManyToManyField(blank=True, related_name='invitee', to=settings.AUTH_USER_MODEL)),
                ('inviter', models.ManyToManyField(blank=True, related_name='inviter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]