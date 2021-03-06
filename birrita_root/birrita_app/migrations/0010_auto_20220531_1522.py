# Generated by Django 3.2.13 on 2022-05-31 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birrita_app', '0009_alter_beerslist_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='brewerylist',
            name='bar_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='birrita_app.barlist'),
        ),
    ]
