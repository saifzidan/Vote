# Generated by Django 3.2.18 on 2023-08-22 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Worker', '0003_alter_question_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='vote',
            new_name='question_text',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
