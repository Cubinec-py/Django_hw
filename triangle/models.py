from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name


class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.city_name)


class Product(models.Model):
    product_name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.product_name)


class Purveyor(models.Model):
    city_name = models.OneToOneField(
        City,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    purveyor_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.purveyor_name)


class Client(models.Model):
    city_name = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )

    product_name = models.ManyToManyField(Product)

    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=100)

    def __str__(self):
        return str(self.client_name)
