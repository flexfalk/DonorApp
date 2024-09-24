from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User  # Django's built-in user model

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username  # Display donor username in the admin panel

class Sample(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)  # Link each sample to a donor
    sample_date = models.DateField()
    quantity = models.DecimalField(max_digits=5, decimal_places=2)  # Quantity in milliliters
    status = models.CharField(max_length=50)  # Status like 'Pending', 'Approved', 'Rejected'

    def __str__(self):
        return f"Sample from {self.donor.user.username} on {self.sample_date}"

class Deadline(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)  # Each deadline linked to a sample
    deadline_date = models.DateField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Deadline for {self.sample.donor.user.username} on {self.deadline_date}"

class Price(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)  # Payment associated with a donor
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Payment amount
    paid_on = models.DateField(null=True, blank=True)  # Payment date, nullable if not yet paid

    def __str__(self):
        return f"Payment of {self.amount} to {self.donor.user.username}"