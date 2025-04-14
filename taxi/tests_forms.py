from django.urls import reverse
from taxi.models import Driver, Car, Manufacturer


def test_driver_search(self):
    Driver.objects.create_user(username="testuser1", password="12345")
    Driver.objects.create_user(username="driver2", password="12345")

    response = self.client.get(reverse("taxi:driver-list") + "?username=test")

    self.assertContains(response, "testuser1")
    self.assertNotContains(response, "driver2")


def test_car_search(self):
    Car.objects.create(model="Tesla")
    Car.objects.create(model="BMW")

    response = self.client.get(reverse("taxi:car-list") + "?model=tesla")

    self.assertContains(response, "Tesla")
    self.assertNotContains(response, "BMW")


def test_manufacturer_search(self):
    Manufacturer.objects.create(name="Toyota")
    Manufacturer.objects.create(name="Ford")

    response = self.client.get(reverse("taxi:manufacturer-list") + "?name=toy")

    self.assertContains(response, "Toyota")
    self.assertNotContains(response, "Ford")
