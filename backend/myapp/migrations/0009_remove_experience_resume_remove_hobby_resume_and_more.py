# Generated by Django 5.0.7 on 2024-09-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_contact_resume_contactnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='hobby',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='address',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='contactnumber',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='image',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='summary',
        ),
        migrations.AddField(
            model_name='resume',
            name='company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='contact_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='degree',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='education_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='education_start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='hobbies',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='resume',
            name='institution',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='language',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='position',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='profile_images/'),
        ),
        migrations.AddField(
            model_name='resume',
            name='project_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='work_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='work_experience_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='work_experience_start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='resume',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.JSONField(default=list),
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Hobby',
        ),
    ]
