'''
Imports the relevant packages
'''
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Status of user posts
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    '''
    Post model
    '''
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    post_tag = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    upvotes = models.ManyToManyField(User, related_name='post_upvotes')
    downvotes = models.ManyToManyField(User, related_name='post_downvotes')

    class Meta:
        '''
        Orders the posts by when they were created
        '''
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def total_votes(self):
        total_upvotes = self.upvotes.count()
        total_downvotes = self.downvotes.count()
        total_votes = total_upvotes - total_downvotes
        return total_votes


class Comment(models.Model):
    '''
    Comment model
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True, related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Orders comments by when they were created
        '''
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Tags(models.Model):
    '''
    Tags model - Can be also called 'categories'
    '''
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class UserProfile(models.Model):
    '''
    Extends User model to allow users to have more settings
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user_profile')
    user_image = CloudinaryField('image', blank=True, null=True)
    user_bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse('home')


# Function which creates UserProfile model for new registrations
# and sets default user image
def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.get_or_create(
            user=instance,
            user_image='https://res.cloudinary.com/craity/image/'
                       'upload/v1651927366/CIPP4/default_profile.png')


post_save.connect(user_created_receiver, sender=User)
