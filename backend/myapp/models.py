from django.db import models


# Create your models here.
class Jobpost(models.Model):
    company_name=models.CharField(max_length=100,default="Default Company")
    job_name=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    salary=models.CharField(max_length=50,null=True)
    experience_level=models.CharField(max_length=100,null=True)
    skills=models.TextField(null=True)
    language=models.CharField(max_length=100,blank=True,null=True)#optional field
    job_type=models.CharField(max_length=100)
    requirement=models.IntegerField(default=0)
    email=models.EmailField(null=True)
    phone=models.IntegerField(default=0)
    is_approved=models.BooleanField(default=False)

    def __str__(self):
        return self.job_name
    
class Resume(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contactnumber = models.CharField(max_length=10)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    language = models.JSONField(default=list)  
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
    description = models.TextField(blank=True, null=True)
    experience = models.JSONField(default=list)  
    education = models.JSONField(default=list)  
    skills = models.JSONField(default=list)  
    hobbies = models.JSONField(default=list)  
    project = models.URLField(blank=True,null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

class ResourcePython(models.Model):
    title = models.CharField(max_length=200)  # Field for the title of the topic
    description = models.TextField()           # Field for a detailed description
    link = models.URLField(blank=True)         # Field for a URL link, optional

    def __str__(self):
        return self.title
    
class ResourceReact(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField()           
    link = models.URLField(blank=True)         

    def __str__(self):
        return self.title

class Tracking(models.Model):
    title=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    contact=models.IntegerField()
    date=models.DateField()
    note=models.TextField()

    def __str__(self) -> str:
        return self.title
    
    

