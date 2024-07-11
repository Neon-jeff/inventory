from django.db import models

# Create your models here.

class Item(models.Model):
    barcode_id=models.CharField(max_length=400,default='')
    name=models.CharField(max_length=400,null=True,blank=True)
    description=models.TextField(default='')
    unit_price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    image=models.ImageField(upload_to='Inventory-Images',null=True,blank=True)

    def __str__(self) -> str:
        return f'Inventory item {self.name}'