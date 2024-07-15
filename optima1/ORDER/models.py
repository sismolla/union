from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    title = models.CharField(max_length=200,null=False,default='not given')
    number_of_pages = models.IntegerField()
    deadline = models.DateTimeField(max_length=100)
    abstract = models.FileField(upload_to='assignment/')
    description = models.TextField()
    accept_terms = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.firstname} - {self.lastname}'
    
class Business_plan(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    title = models.CharField(max_length=200,null=False,default='not given')
    number_of_pages = models.IntegerField()
    deadline = models.DateTimeField(max_length=100)
    abstract = models.FileField(upload_to='business_plan/')
    description = models.TextField()
    accept_terms = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.firstname} - {self.lastname}'

class Research(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    title = models.CharField(max_length=200,null=False,default='not given')
    number_of_pages = models.IntegerField()
    deadline = models.DateTimeField(max_length=100)
    abstract = models.FileField(upload_to='abstract/')
    description = models.TextField()
    accept_terms = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.firstname} - {self.lastname}'
    


class Thesis(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    title = models.CharField(max_length=200,null=False,default='not given')
    number_of_pages = models.IntegerField()
    deadline = models.DateTimeField(max_length=100)
    abstract = models.FileField(upload_to='Thesis/')
    description = models.TextField()
    accept_terms = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.firstname} - {self.lastname}'
    
class GraphicsDesignSubmission(models.Model):
    SERVICE_CHOICES = [
        ('logo', 'Logo'),
        ('photo_editing', 'Photo Editing'),
        ('banner', 'Banner'),
        ('birth_certificate', 'Birth Certificate'),
        ('wedding_card', 'Wedding Card'),
        ('business_card', 'Business Card'),
        ('poster', 'Poster'),
        ('advertisement', 'Advertisement'),
        ('presentation_template', 'Presentation Template'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    deadline = models.DateTimeField()
    design_file = models.FileField(upload_to='designs/')
    description = models.TextField(blank=True, null=True)
    accept_terms = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.service}"
    

class ProgrammingProjectSubmission(models.Model):
    WORK_AREA_CHOICES = [
        ('website', 'Website'),
        ('app', 'App'),
        ('desktop', 'Desktop'),
        ('game', 'Game'),
        ('other', 'Other'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    programming_language = models.CharField(max_length=100)
    specific_work_area = models.CharField(null=False,blank=False,max_length=50, choices=WORK_AREA_CHOICES)
    deadline = models.DateTimeField()
    project_file = models.FileField(upload_to='programming/')
    description = models.TextField(blank=True, null=True)
    accept_terms = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.title}"
    
class VideoEditingSubmission(models.Model):
    VIDEO_FORMAT_CHOICES = [
        ('wave', 'WAVE'),
        ('mp4', 'MP4'),
        ('mov', 'MOV'),
        ('avi', 'AVI'),
        ('mkv', 'MKV'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    video_length = models.CharField(max_length=50)
    video_format = models.CharField(max_length=10, choices=VIDEO_FORMAT_CHOICES)
    deadline = models.DateTimeField()
    project_file = models.FileField(upload_to='video_editing/')
    description = models.TextField(blank=True, null=True)
    accept_terms = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.title}"
    
class Transcription(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')))
    accept_terms = models.BooleanField()
    title = models.CharField(max_length=255)
    source_language = models.CharField(max_length=100)
    target_language = models.CharField(max_length=100)
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.title}"