from django.db import models

# Create your models here.


class Client(models.Model):
    cimage_id = models.AutoField
    cimage_title = models.CharField(max_length=50, null=True, blank=True)
    cimage = models.ImageField(upload_to="clients/images", default="")
    def __str__(self):
        return self.cimage_title


class BannerImage(models.Model):
    bimage_id = models.AutoField
    bimage_title = models.CharField(max_length=50, null=True, blank=True)
    bimage_desc = models.CharField(max_length=300, null=True, blank=True)
    bimage = models.ImageField(upload_to="banner/images", default="")

    def __str__(self):
        return self.bimage_title


class About(models.Model):
    custom_id = models.AutoField
    founder_message = models.CharField(max_length=10000, null=True, blank=True)
    how_we_work = models.CharField(max_length=10000, null=True, blank=True)
    def __str__(self):
        return self.founder_message


class PortfolioCategories(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

        
class Post(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    desc =  models.CharField(max_length=300, null=True, blank=True)
    category = models.ForeignKey(PortfolioCategories,default=None,on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post,default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/",blank=True)

    def __str__(self):
        return self.post.title

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=70,default="")
    message = models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name



