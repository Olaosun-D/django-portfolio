from django.db import models
from multiselectfield import MultiSelectField


# About Model
class About(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    short_description = models.CharField(max_length=100)
    description = models.TextField()
    profile_image = models.ImageField(upload_to="about", default='', blank=True) #profile image
    front_page_image = models.ImageField(upload_to="about", default='', blank=True) #hero image
    
    #Contact Details Section 
    phone_number = models.IntegerField(max_length=14, default= 4400000000000)
    user_email = models.EmailField(blank=True) #contact details
    github = models.URLField(blank=True)
    behance = models.URLField(blank=True)
    dribble = models.URLField(blank=True)
    instagram = models.URLField(blank=True)


    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About"

    def __str__(self):
        return self.first_name + ' ' + self.last_name



#Skill Model
class Skills(models.Model): 
    SKILL_TYPE_CHOICES = [
    ('Front End', (
            ('javascript', 'Javascript'),
            ('html', 'Html'),
            ('css', 'CSS'),
            ('electron', 'Electron'),
        )
    ),
    ('Back End', (
            ('python', 'Python'),
            ('node js', 'Node js'),
            ('java', 'Java'),
            ('php', 'Php'),
        )
    ),
    ('Design', (
            ('cad', 'CAD'),
            ('solidworks', 'Solidworks'),
            ('blender', 'Blender'),
            ('adobe', 'Adobe Creative Suite'),
            ('photoshop', 'Photoshop'),
            ('illustartor', 'illustartor'),
            ('Corel Draw', 'Corel Draw'),
        )
    ),
    ('web development', 'Web Development'),
]

    skill_type = MultiSelectField(choices = SKILL_TYPE_CHOICES)

    class Meta:
        verbose_name_plural = "skills"

    def __str__(self):
        return self.skill_type[0].capitalize()

class Projects(models.Model):
    TECHNOLOGIES_CHOICES = (('html', 'Html'),
            ('js', 'Javacript'),
            ('node', 'Node Js'),
            ('gulp js', 'Gulp Js'),
            ('csd', 'Css'),
            ('python', 'Python'),
            ('django', 'Django'),
            ('java', 'Java'),
            ('electron', 'Electron'),
            ('photoshop', 'Adobe Photoshop'),
            ('illustartor', 'Adobe illustartor'),
            ('wordpress', 'Wordpress'),
            ('invision', 'invision'),
            ('xd', 'Adobe XD'))
    

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    added_description = models.TextField(blank=True, null=True)
    technologies = MultiSelectField(choices = TECHNOLOGIES_CHOICES)
    project_image = models.ImageField(upload_to='projects', blank=True)
    project_image_1 = models.ImageField(upload_to='projects', blank=True, default='/assets/projects_placeholder.jpg')
    project_image_2 = models.ImageField(upload_to='projects', blank=True, default='/assets/projects_placeholder.jpg')
    project_image_3 = models.ImageField(upload_to='projects', blank=True, default='/assets/projects_placeholder.jpg')
    project_link = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title