# Generated by Django 3.0.7 on 2020-07-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='portfolio_template',
            field=models.CharField(blank=True, choices=[('portfolio_template1.html', 'Template 1'), ('portfolio_template2.html', 'Template 2')], max_length=100, null=True),
        ),
    ]
