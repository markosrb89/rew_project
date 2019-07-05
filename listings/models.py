from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
  # Reference to 'Realtor' table, it's foreign key of another table so we can reference to it.
  # If realtor is deleted, do not delete listing
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  # blank=True -> Optional field
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  # For the argument it's needed to define where the image is uploaded to
  # In 'media' folder is stored everything that is uploaded from the admin area (images/files)
  # Here it's defined the folder (photos) which is created inside that 'media' folder where those photos will be stored,
  # and every photo which is uploaded will go to another folder with the name of the date when it's uploaded
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  # To be able to display in the admin area each listing, 'title' is picked to be 'main' field to display
  def __str__(self):
    return self.title