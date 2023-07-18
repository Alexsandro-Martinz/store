from faker import Faker
from django.contrib.auth.models import User
import pytest
from api_profile.serializers import UserSerializer


fake = Faker()