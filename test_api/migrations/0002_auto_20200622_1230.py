# Generated by Django 3.0.7 on 2020-06-22 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('start_date', models.DateField(auto_now=True)),
                ('finish_date', models.DateField()),
                ('definition', models.CharField(max_length=256)),
                ('answer_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_api.Answer')),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]