from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name
    
    item_name=models.CharField(max_length=122)
    item_desc=models.CharField(max_length=122)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=5000, default='https://img.freepik.com/free-vector/loading-circles-blue-gradient_78370-2646.jpg?size=338&ext=jpg&ga=GA1.1.1224184972.1714262400&semt=sph')
