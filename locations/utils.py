from faker import Faker
from .models import Governorate,City

fake = Faker()
def generate_governorates(num):
    for _ in range(num):
        governorate = Governorate.objects.create(
            name = fake.city()
        )
        governorate.save()
        for _ in range(num):
            city = City.objects.create(
                name = fake.city(),
                governorate_id = governorate.id
            )
            city.save()

def generate_syria_governorates_and_cities():
    governorates_with_cities = {
        "Aleppo": ["Aleppo", "Manbij", "A'zaz", "Al-Bab", "Jarablus"],
        "Raqqa": ["Raqqa", "Tabaqa", "Tal Abyad", "Ain Issa", "Suluk"],
        "As-Suwayda": ["As-Suwayda", "Salkhad", "Shahba", "Qurayya", "Mushannaf"],
        "Damascus": ["Damascus", "Jobar", "Bab Tuma", "Al-Midan", "Barzeh"],
        "Daraa": ["Daraa", "Nawa", "Jasim", "Inkhil", "Al-Harra"],
        "Deir ez-Zor": ["Deir ez-Zor", "Al Mayadin", "Al Bukamal", "Tabni", "Al-Quriyah"],
        "Hama": ["Hama", "Salamiyah", "Masyaf", "Suran", "Taybat al-Imam"],
        "Al-Hasakah": ["Al-Hasakah", "Qamishli", "Ras al-Ayn", "Al-Malikiyah", "Amuda"],
        "Homs": ["Homs", "Tadmur", "Al-Rastan", "Talbiseh", "Qusayr"],
        "Idlib": ["Idlib", "Maarat al-Numan", "Jisr al-Shughur", "Saraqib", "Ariha"],
        "Latakia": ["Latakia", "Jableh", "Qardaha", "Haffah", "Kasab"],
        "Quneitra": ["Quneitra", "Khan Arnabah", "Baath City", "Jubata al-Khashab", "Trinjeh"],
        "Rif Dimashq": ["Douma", "Harasta", "Al-Tall", "Zabadani", "Darayya"],
        "Tartus": ["Tartus", "Baniyas", "Safita", "Dreikish", "Sheikh Badr"]
    }

    for governorate_name, cities in governorates_with_cities.items():
        governorate, created = Governorate.objects.get_or_create(
            name=governorate_name
        )
        if created:
            print(f"Generated governorate: {governorate.name}")
        else:
            print(f"Governorate {governorate.name} already exists")

        for city_name in cities:
            city, city_created = City.objects.get_or_create(
                name=city_name,
                governorate=governorate
            )
            if city_created:
                print(f"Generated city: {city.name} in {governorate.name}")
            else:
                print(f"City {city.name} in {governorate.name} already exists")

# Call the function to generate the data
generate_syria_governorates_and_cities()

