# Generated by Django 3.0.5 on 2020-06-19 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200619_0205'),
        ('contact', '0002_auto_20200618_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='navigation_bar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.NavigationSnippet'),
        ),
    ]
