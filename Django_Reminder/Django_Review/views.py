from django.shortcuts import render, redirect, get_object_or_404
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

def add_weapon(request):
    if(request.method == "POST"):
        weap_Name = request.POST.get('weap_Name')
        weap_Price = request.POST.get('weap_Price')
        weap_Type = request.POST.get('weap_Type')
        weapon.objects.create(
            weapon_Name = weap_Name,
            weapon_Price = weap_Price,
            weapon_Type = weap_Type,
            )
    return redirect('inventory')

def delete_weapon(request, pk):
    weapon.objects.filter(pk=pk).delete()
    return redirect('inventory')

def edit_weapon(request,pk):
    e_weapon = weapon.get_object_or_404(pk=pk)
    e_weapon.weap_Name = request.POST.get('weap_Name')
    e_weapon.weap_Price = request.POST.get('weap_Price')
    e_weapon.weap_Type = request.POST.get('weap_Type')
    e_weapon.save()
    
    return redirect('inventory')