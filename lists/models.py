from django.db import models 

#class Item(models.Model):
#    pass

class Item(models.Model):
    #text = models.TextField()
    text = models.TextField(default ='')
    