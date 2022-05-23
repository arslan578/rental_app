from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from reservation.models import Reservation
from reservation.utils import get_previous_rental_id


class ReservationView(ListView):
    template_name = 'index.html'
    model = Reservation

    def get(self, request, *args, **kwargs):
        try:

            reservations = self.model.objects.alll()
            reservation_list = []
            for res in reservations:
                tmp = {}
                tmp = {
                    'rental_name': 'rental-{}'.format(res.rental.id),
                    'id': 'Res-{}'.format(res.id),
                    'checkin': str(res.checkin),
                    'checkout': str(res.checkout),
                    'previous_reservation': get_previous_rental_id(res.id)

                }
                reservation_list.append(tmp)

            context = {
                'data': reservation_list
            }
            return render(request, 'index.html', context=context)
        except Exception as e:
            return render(request, 'error.html')


