# Generated by Django 3.2.5 on 2021-10-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20211029_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=20, null=True),
        ),
    ]
