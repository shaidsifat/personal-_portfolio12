__from django.db import models

# Create your models here.
class Topic(models.Model):

 text = models.CharField(max_height=200)
 date_added = models.DateTimeField(auto_now_add=True)
 
  def_str_(self):
        
     return self.text
     