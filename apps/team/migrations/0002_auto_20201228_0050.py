# Generated by Django 3.1.4 on 2020-12-27 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='team',
            name='plan_end_date',
        ),
        migrations.RemoveField(
            model_name='team',
            name='plan_status',
        ),
        migrations.RemoveField(
            model_name='team',
            name='stripe_customer_id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='stripe_subscription_id',
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
