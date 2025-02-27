import random
from .models import User, City 
def create_super_user():
    cities = City.objects.all()  
    random_city = random.choice(cities)
    
    user = User.objects.create(
        username='Laith',
        phone_number='0950501220',
        password='12345678',
        user_type='admin',
        city=random_city, 
        is_superuser=True,
        is_active = True
    )
    user.set_password(user.password)
    user.save()
