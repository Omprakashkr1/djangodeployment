from django.db import models

class add(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to='image/')
    image_url=models.URLField(default='',blank=True)

    def _str_(self):
        return self.add
    
    class Meta:
        verbose_name_plural="advert"
        
class job_pages(models.Model):
    image=models.ImageField(upload_to='image/',default='',blank=True)
    image_url=models.URLField(default='',blank=True)
    organisation_name=models.CharField(max_length=200)
    role=models.TextField()

    def _str_(self):
        return self.job_page
    
    class Meta:
        verbose_name_plural="job_listing_pages"

class article(models.Model):
    title=models.CharField(max_length=200)
    author_name=models.CharField(max_length=100)
    upload_time=models.DateTimeField(auto_now_add=True)
    image=models.ImageField('image/',default='',blank=True)
    image_url=models.URLField(default='',blank=True)

    def _str_(self):
        return self.article
    
    class Meta:
        verbose_name_plural="article"

class contact(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField(max_length=200)
    contact_no=models.IntegerField(default=0)


class grant(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    amount_required=models.IntegerField(default=0)
    upvotes=models.IntegerField(default=0)
    protocol_link=models.URLField(default='',blank=True)
    contact=models.ForeignKey(contact,on_delete=models.CASCADE)

    def _str_(self):
        return self.grant
    
    class Meta:
        verbose_name_plural="grant"
