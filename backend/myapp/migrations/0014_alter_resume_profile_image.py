# Generated by Django 5.0.7 on 2024-09-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_resume_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='./media/profile_images/'),
        ),
    ]
