from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger


# Create your views here.
def index(request):
    return render(request,
                  "flights/index.html",
                  {"flights": Flight.objects.all()
                   })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request,
                  "flights/flight.html",
                  {"flight": flight,
                   "passengers": flight.passengers.all(),
                   "non_passengers":Passenger.objects.exclude(flights=flight).all()})

# 與 models.py 對應
# flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

def book(request, flight_id):
        # For a post request, add a new flight
    if request.method == "POST":
        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])

        # Finding the passenger based on the id
        passenger = Passenger.objects.get(pk=passenger_id)

        # Add passenger to the flight
        passenger.flights.add(flight)

        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))