# Generated by Django 3.2.8 on 2023-02-12 17:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_article_biography_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.CharField(error_messages={'unique': 'A user with that email address already exists.'}, max_length=256, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
