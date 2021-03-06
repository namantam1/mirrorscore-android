# Generated by Django 3.1 on 2020-08-30 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussionwall', '0002_loginmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussionwall.studentboard')),
                ('studentclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussionwall.studentclass')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussionwall.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
