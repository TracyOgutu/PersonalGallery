from django.test import TestCase
import datetime as dt
from . models import Category,Location,Image

# Create your tests here.
class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.travel=Category(category_name='plane')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))

    def test_save_category(self):
        self.travel.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_get_category(self):
        self.travel.save_category()
        category = Category.get_category
        self.assertTrue(category is not None)

class LocationTestClass(TestCase):
     
    def setUp(self):
        self.nairobi=Location(location_name='kilimani')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def test_save_location(self):
        self.nairobi.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    
    def test_get_location(self):
        self.nairobi.save_location()
        location = Location.get_location
        self.assertTrue(location is not None)


class ImageTestClass(TestCase):

    def setUp(self):    
        self.nairobi=Location(location_name='kilimani')
        self.travel=Category(category_name='plane')
        self.nairobi.save_location()
        self.travel.save_category()

        self.img=Image(photo_image='shoe.jpg',image_name='shoe',description='shoe game lit',category=self.travel,location=self.nairobi)

    def test_instance(self):
        self.assertTrue(isinstance(self.img,Image))

    def test_save_photo(self):
        self.img.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

