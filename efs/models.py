from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import requests
# Create your models here.


class User(AbstractUser):
    @property
    def is_manager(self):
        if hasattr(self, 'manager'):
            return True
        return False

    @property
    def is_customer(self):
        if hasattr(self, 'customer'):
            return True
        return False


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    manager_id = models.AutoField(auto_created=True, primary_key=True, max_length=6, blank = True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    customer_id = models.AutoField(auto_created=True, primary_key=True, max_length=6, blank = True)
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='manid', blank = True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    cust_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)


class Investment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='investments')
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    acquired_value = models.DecimalField(max_digits=10, decimal_places=2)
    acquired_date = models.DateField(default=timezone.now)
    recent_value = models.DecimalField(max_digits=10, decimal_places=2)
    recent_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.investment_id)

    def results_by_investment(self):
        return self.recent_value - self.acquired_value


class Stock(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='stocks')
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    shares = models.DecimalField (max_digits=10, decimal_places=1)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer)

    def initial_stock_value(self):
        return self.shares * self.purchase_price

    def current_stock_price(self):
        symbol_f = str(self.symbol)
        main_api = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols='
        api_key = '&apikey= OJNKQE323LF34BH3'
        url = main_api + symbol_f + api_key
        json_data = requests.get(url).json()
        open_price = float(json_data["Stock Quotes"][0]["2. price"])
        share_value = open_price
        return share_value

    def current_stock_value(self):
        return float(self.current_stock_price()) * float(self.shares)


class Mutualfund(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, related_name='mutualfunds',on_delete=models.DO_NOTHING)
    bondtype = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    acquired_value = models.DecimalField(max_digits=10, decimal_places=2)
    acquired_date = models.DateField(default=timezone.now)
    recent_value = models.DecimalField(max_digits=10, decimal_places=2)
    recent_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer)

    def results_by_mutualfund(self):
        return self.recent_value - self.acquired_value
