from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Donor, Sample, Deadline, Price

@login_required  # Ensure only logged-in users can access this view
def donor_dashboard(request):
    donor = Donor.objects.get(user=request.user)  # Get the donor associated with the logged-in user
    samples = Sample.objects.filter(donor=donor)  # Get all samples for the donor
    deadlines = Deadline.objects.filter(sample__donor=donor)  # Get deadlines for the donor's samples
    prices = Price.objects.filter(donor=donor)  # Get payment information for the donor

    context = {
        'donor': donor,
        'samples': samples,
        'deadlines': deadlines,
        'prices': prices,
    }

    return render(request, 'donors/dashboard.html', context)  # Render the dashboard template with the context