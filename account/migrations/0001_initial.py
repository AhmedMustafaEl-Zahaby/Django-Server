# Generated by Django 4.1.2 on 2022-10-28 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Account', to='parent.parent')),
            ],
            options={
                'db_table': 'Account',
            },
        ),
    ]
