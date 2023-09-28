# Generated by Django 4.2.1 on 2023-09-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='choice',
            field=models.CharField(choices=[('ML', 'Machine Learning'), ('Web', 'Web Development'), ('Syntax', 'Programming Syntax'), ('Book', 'Book Reviews')], default='Syntax', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='default_image.jpg', upload_to='images/'),
        ),
    ]