# Generated by Django 4.1.7 on 2023-03-23 06:56

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=123),
            preserve_default=False,
        ),
    ]
