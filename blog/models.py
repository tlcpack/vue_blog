from django.db import models

# Create your models here.
# class Topic(models.Model):
#     name = models.CharField(max_length=100, help_text="What's the topic")

#     def __str__(self):
#         return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=250)
    # author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=1000)
    url = models.URLField(blank=True, null=True, help_text="www.website.com")
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
    
class Season(models.Model):
    year = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    era_plus = models.FloatField()
    bat_ave = models.FloatField()
    ops = models.FloatField()
    run_diff = models.IntegerField()

    def __str__(self):
        return str(self.year)
