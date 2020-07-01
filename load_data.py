from webapp import create_app
from webapp.model import db, Arenas
import json

app = create_app()
db.init_app(app)

with open("data_file.json", "rb") as read_file:
    data = json.load(read_file)
    properties = data['features']

def import_data(name, adress, website, phones, hours24):
    arena=Arenas(name=name,
                adress=adress,
                website = website,
                phones=phones,
                hours24=hours24,
                description="Test Descrption",
                image="image.jpg",
                metro="111")
    db.session.add(arena)
    db.session.commit()

def get_phones(prop):
    phones = prop.get("properties", {}).get("CompanyMetaData", {}).get("Phones")
    if isinstance(phones, list):
        return ", ".join([phone.get("formatted") for phone in phones])

def get_is_24(prop):
    hours24 = prop.get("properties", {}).get("CompanyMetaData", {}).get("Hours", {}).get('Availabilities',{})
    if isinstance(hours24, list):
        return hours24[0].get("TwentyFourHours", False)
    return False


with app.app_context():
    for prop in properties:
        name = prop.get("properties", {}).get("CompanyMetaData", {}).get("name", {})
        adress = prop.get("properties", {}).get("description", {})
        website = prop.get("properties", {}).get("CompanyMetaData", {}).get('url', {})
        phones = get_phones(prop)
        hours24 = get_is_24(prop)
    import_data(name, adress, website, phones, hours24)





# цикл in обходит файл с импортированными аренами и записывает их в базу данных
