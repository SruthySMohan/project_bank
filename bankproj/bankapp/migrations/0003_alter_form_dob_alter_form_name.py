# Generated by Django 4.1.2 on 2022-10-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_form_delete_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='dob',
            field=models.DateField(default=False),
        ),
        migrations.AlterField(
            model_name='form',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
