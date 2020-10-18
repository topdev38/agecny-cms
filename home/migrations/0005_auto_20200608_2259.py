# Generated by Django 3.0.5 on 2020-06-09 05:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200608_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='counter',
            field=wagtail.core.fields.StreamField([('counter', wagtail.core.blocks.StructBlock([('number', wagtail.core.blocks.IntegerBlock(required=True)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Add additional text', required=True)), ('delay', wagtail.core.blocks.IntegerBlock(required=True)), ('thousand', wagtail.core.blocks.BooleanBlock())]))], blank=True, null=True),
        ),
    ]