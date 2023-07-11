from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.charFeild(max_Length=200)
    
    def __str__ (self):
        return self.name
    
class Item(models.Model):
    ToDoList = models.models.ForeignKey(ToDoList, on_delete = models.CASCADE)
    text = models.CharFeild(max_Length=300)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.text 