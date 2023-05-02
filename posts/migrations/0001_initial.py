# Generated by Django 4.2 on 2023-05-02 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
                ('audio_one', models.URLField(blank=True)),
                ('audio_two', models.URLField(blank=True)),
                ('audio_three', models.URLField(blank=True)),
                ('audio_four', models.URLField(blank=True)),
                ('audio_five', models.URLField(blank=True)),
                ('draft', models.BooleanField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted_at'],
            },
        ),
    ]
