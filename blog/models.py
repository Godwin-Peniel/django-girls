from django.conf import settings
# this import gives me access to the project's settings.py file values.

from django.db import models

# this import gives access to the models.Model class, and all the field types (Charfield, TextField, DateTimeField, etc.) that can be used to define the model's attributes.

from django.utils import timezone

# created a class Post that inherits from models.Model, which means that Post is a Django model and will be treated as a database table.
class Post(models.Model):
   # created attributes for the Post model, which will be represented as columns in the database table. Each attribute is defined as a class variable and is assigned a field type from Django's models module.

   author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   title = models.CharField(max_length=200)
   text = models.TextField()
   created_date = models.DateTimeField(default=timezone.now)
   published_date = models.DateTimeField(blank=True, null=True)

# created a method publish() that sets the published_date attribute to the current date and time (using timezone.now()) and saves the Post instance to the database. self.save() is a method provided by Django's models.Model class that saves the current instance to the database.

   def publish(self):
      self.published_date = timezone.now()
      self.save()

# created a method __str__() that returns a string representation of the Post instance, which will be used when the instance is displayed in the Django admin or other parts of the application.
   def __str__(self):
      return self.title

# use python manage.py makemigrations blog to make Django aware of the changes made in our models.py file.

# use python manage.py migrate blog to apply the migrations and create the corresponding database tables.