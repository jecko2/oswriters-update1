from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class FirstOrder(models.Model):
    COMPLEXITY_CHOICES = (
        ('HG', 'High School'),
        ('CL', 'College'),
        ('UG', 'Undergraduate'),
        ('MS', 'Masters'),
        ('PHD', 'PhD')
    )
    TYPE_OF_WORK = (
        ('AE', 'Admission Essay'),
        ('Bio', 'Biographies'),
        ('BP', 'Business Plan'),
        ('BR', 'Book Review')
    )
    DEADLINE = (
        ('14D', '14 Days'),
        ('10D', '10 Days'),
        ('7D', '7 Days'),
        ('6D', '6 Days'),
        ('5D', '5 Days'),
        ('4D', '4 Days'),
        ('3D', '3 Days'),
        ('2D', '2 Days'),
        ('1D', '1 Days'),
        ('20H', '20 Hours'),
        ('16H', '16 Hours'),
        ('12H', '12 Hours'),
        ('8H', '8 Hours'),
        ('6H', '6 Hours'),
        ('5H', '5 Hours'),
        ('3H', '3 Hours'),
        ('2H', '2 Hours'),
    )
    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    complexity = models.CharField(max_length=100, choices=COMPLEXITY_CHOICES)
    type_of_work = models.CharField(max_length=100, choices=TYPE_OF_WORK)
    deadline = models.CharField(max_length=100, choices=DEADLINE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.complexity


class SecondOrder(models.Model):
    SUBJECT = (
        ('OT', 'Other'),
        ('ACC', 'Account'),
        ('CL', 'Criminal Law')
    )
    REFERENCE_STYLE = (
        ('H', 'Harvard'),
        ('A', 'APA'),
        ('M', 'MLA'),
        ('C', 'Chicago'),
        ('V', 'Vancouver')
    )
    order_form = models.ForeignKey(FirstOrder, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, choices=SUBJECT)
    number_of_pages = models.CharField(max_length=300)
    double_spaced = models.BooleanField(default=False)
    reference_style = models.CharField(max_length=100, choices=REFERENCE_STYLE)
    reference_total = models.IntegerField(default=1)
    order_instruction = models.TextField(blank=True, null=True)
    additional_materials = models.FileField(upload_to='media/', blank=True, null=True)
    pricing = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.subject


class ExtraServices(models.Model):
    EXTRA_TASK = (
        ('PPT', 'PowerPoint'),
        ('PS', 'PhotoShop'),
        ('IG', 'InfoGraph'),
        ('WB', 'Web Design')
    )
    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    extra_task = models.CharField(max_length=100, choices=EXTRA_TASK)
    pricing = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.extra_task



