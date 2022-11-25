# Generated by Django 3.2.4 on 2022-11-23 15:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('useraccounts', '0003_alter_profile_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('content', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='useraccounts.profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
