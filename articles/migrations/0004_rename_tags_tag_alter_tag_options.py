# Generated by Django 4.0.3 on 2022-03-07 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articletag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
