# Generated by Django 4.2.1 on 2023-10-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolsite', '0004_alter_post_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='coolsite.tagpost'),
        ),
    ]