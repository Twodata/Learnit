from django.db import models

#from django.utils import timezone

from django.contrib.auth.models import User



section_list = (
            ('Agriculture', 'Agriculture'),
            ('Catering/Hospitality', 'Catering/Hospitality'),
            ('Education', 'Education'),
            ('Event Management', 'Event Management'),
            ('IT/Programming', 'IT/Programming'),
            ('Fashion', 'Fashion'),
            ('Health', 'Health'),
            ('IT/Programming', 'IT/Programming'),
            ('Technology', 'Technology'),            
            ('General', 'General'),
            )

class market(models.Model):    
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    section = models.CharField(max_length = 40,
                               choices = section_list, default = 'Agriculture')
    businessname = models.CharField(max_length = 100, unique = True)
    logo = models.ImageField(upload_to = 'logo', default = 'logo', null = True, blank = True)
    location = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200, null = True, blank = True)
    phone_no = models.CharField(max_length = 15)
    website = models.URLField(null = True, blank = True, 
                              default = 'http://learnit.com')
    services = models.TextField(default = 'Add a brief description of your products/services here')
    added_by = models.CharField(max_length = 50, default = '')
    
    def __str__(self):
        return self.businessname
    
    
class article(models.Model):
        added_by = models.CharField(max_length = 50)
        topic = models.CharField(max_length = 100)    
        section = models.CharField(max_length = 40,
                               choices = section_list )
        enterprise = models.CharField(max_length = 100, null = True, blank = True )
        date_posted = models.DateField(auto_now_add = True)    
        article = models.TextField( )
        image_1 = models.ImageField(upload_to = 'image', default = 'image', null = True, blank = True)
        image_2 = models.ImageField(upload_to = 'image', default = 'image', null = True, blank = True)
        image_3 = models.ImageField(upload_to = 'image', default = 'image', null = True, blank = True)
        likes = models.IntegerField(default = 0)
        approved_article = models.BooleanField(default = False, blank = True)


        def approve(self):
            self.approved_article = True
            self.save()


        def disapprove(self):
            self.approved_article = False
            self.save()
    

        def __str__(self):
            return self.topic + ' by ' + self.added_by



class Liked(models.Model):
    added_by = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(article, on_delete = models.CASCADE)
    class Meta:
        unique_together = ('added_by', 'post')

    def __str__(self):
        return str(self.added_by)
    
    
class Comment(models.Model):
    added_by = models.CharField(max_length = 50, null = True, blank = True)
    article = models.ForeignKey(article, related_name = 'comments', 
                                on_delete = models.CASCADE, blank = True, null = True)
    text = models.TextField()
    date_posted = models.DateField(auto_now_add = True)
    approved_comment = models.BooleanField(default = False, blank = True)
    article_author = models.CharField(max_length = 50, default = '')
    image = models.ImageField(upload_to = 'comment', default = 'comment', null = True, blank = True)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.added_by
    
    def approved_comments(self):
        return self.comments.filter(approved_comment = True)
    


class Internship(models.Model):    
    businessname = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to = 'logo', default = 'logo', null = True, blank = True)
    business_profile = models.CharField(max_length = 500)
    intern_position = models.CharField(max_length = 150, default = '')    
    intern_ad = models.TextField(default = 'Add internship description here')
    added_by = models.CharField(max_length = 50, default = '')
    
    def __str__(self):
        return self.intern_position +' intern position(s) by '+ self.added_by  
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    website = models.URLField(null = True, blank = True, 
                              default = 'http://www.learnit')
    skillset = models.CharField(max_length = 500, null = True, blank = True)
    quote = models.CharField(max_length = 250, null = True, blank = True)
    picture = models.ImageField(upload_to = 'profile_picture', default = 'profile_picture', 
                                null = True, blank = True)
    
    def __str__(self):
        return self.user.username
    

    
class Friend(models.Model):
    current_user = models.ForeignKey(User, on_delete = models.PROTECT, related_name = 'owner')
    following = models.ManyToManyField(User)
    
    @classmethod
    def add_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user = current_user)
        friend.following.add(new_friend)
        
    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user = current_user)
        friend.following.remove(new_friend)
    

class Workshop(models.Model):    
    workshop_title = models.CharField(max_length = 150)
    workshop_flyer = models.ImageField(upload_to = 'workshop', default = 'workshop', null = True, blank = True)
    workshop_details = models.TextField(default = 'Add workshop/training details here')
    added_by = models.CharField(max_length = 50, default = '')
    
    def __str__(self):
        return self.workshop_title + ' by ' + self.added_by
    





            