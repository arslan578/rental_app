from django.test import TestCase

# Create your tests here.


from django.test import RequestFactory, TestCase
from .views import ReservationView


class ReservationViewTest(TestCase):
    def test_reservation_table_list(self):
        request = RequestFactory().get('/')
        view = ReservationView()
        view.setup(request)
