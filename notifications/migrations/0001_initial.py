# Generated by Django 4.0 on 2022-08-06 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('post', '0003_alter_post_tags_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField(choices=[(1, 'Like'), (2, 'Comment'), (3, 'Follow')])),
                ('text_preview', models.CharField(blank=True, max_length=90)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_post', to='post.post')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_from_user', to='auth.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_to_user', to='auth.user')),
            ],
        ),
    ]
