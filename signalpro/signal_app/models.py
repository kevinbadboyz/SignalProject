from django.db import models

fruits = {
    ('Apple', 'Apple'),
    ('Banana', 'Banana'),
    ('Mango', 'Mango'),
    ('Orange', 'Orange'),
}

class Purchase(models.Model):
    item = models.CharField(max_length = 50, choices = fruits)
    quantity = models.IntegerField(default = 0)

    def __str__(self):
        return self.item


class Stock(models.Model):
    available_item = models.CharField(max_length = 50, choices = fruits)
    available_quantity = models.IntegerField(default = 0)

    def __str__(self):
        return self.available_item