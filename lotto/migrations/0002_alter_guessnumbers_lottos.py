# Generated by Django 5.1.1 on 2024-10-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guessnumbers',
            name='lottos',
            field=models.CharField(default='[1,2,3,4,5,6]', max_length=255),
        ),
    ]
