# Generated by Django 2.1.3 on 2018-11-28 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181128_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poem',
            name='author',
        ),
        migrations.AddField(
            model_name='poem',
            name='author_name',
            field=models.CharField(default='incognito', max_length=250),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Poem'),
        ),
    ]