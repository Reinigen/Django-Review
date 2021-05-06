from django.shortcuts import render
from .models import weapon, order, weapon_order


# Create your views here.
def home(request):
    return render(request, 'Django_Review/Home.html')

def weapons_inv(request):
    weapon_types = getAllWeaponTypes()
    print(weapon_types["AN"])
    all_weapons = weapon.objects.all()
    return render(request, 'Django_Review/Inventory.html', {'weapons': all_weapons, 'weapon_types': weapon_types})

def getAllWeaponTypes():

    AMMUNITION = "AN"
    FINESSE = "FE"
    HEAVY = "HY"
    IMPROVISED = "ID"
    LIGHT = "LT"
    LOADING = "LG"
    MARTIAL = "ML"
    RANGED = "RD"
    REACH = "RH"
    SPECIAL = "SL"
    THROWN = "TN"
    TWOHANDED = "TD"
    VERSATILE = "VE"

    WEAPON_TYPES = {
        "AN": 'Ammo',
        "FE": 'Fin',
        "HY": 'Heavy',
        "ID": 'Improv',
        "LT": 'Light',
        "LG": 'Load',
        "ML": 'Martial',
        "RD": 'Range',
        "RH": 'Reach',
        "SL": 'Special',
        "TN": 'Thrown',
        "TD": 'TwoHand',
        "VE": 'Vers'
        }
    
    return WEAPON_TYPES