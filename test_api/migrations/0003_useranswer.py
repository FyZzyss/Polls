# Generated by Django 3.0.7 on 2020-06-22 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0002_auto_20200622_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=64)),
                ('answered_poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_api.Polls')),
            ],
        ),
    ]
