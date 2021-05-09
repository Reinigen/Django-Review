from django.shortcuts import render, redirect, get_object_or_404
from .models import weapon, order, weapon_order


# Create your views here.
def home(request):
    all_weapons = weapon.objects.all()
    return render(request, 'Django_Review/Home.html', {'weapons': all_weapons})

def weapons_inv(request):
    weapon_types = getAllWeaponTypes()
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
        weap_Stock = request.POST.get('weap_Stock')
        weapon.objects.create(
            weapon_Name = weap_Name,
            weapon_Price = weap_Price,
            weapon_Type = weap_Type,
            weapon_Stock = weap_Stock,
            )
    return redirect('inventory')

def delete_weapon(request, pk):
    weapon.objects.filter(pk=pk).delete()
    return redirect('inventory')

def edit_weapon(request,pk):
    
    edit = get_object_or_404(weapon, pk=pk)

    e_weapName = request.POST.get('e_weap_Name')
    e_weapPrice = request.POST.get('e_weap_Price')
    e_weapType = request.POST.get('e_weap_Type')
    e_weapStock = request.POST.get('e_weap_Stock')
    print(e_weapName, e_weapPrice, e_weapType, e_weapStock)

    edit.weapon_Name = e_weapName
    edit.weapon_Price = e_weapPrice
    edit.weapon_Type = e_weapType
    edit.weapon_Stock = e_weapStock
    edit.save()
    print(str(edit))
    
    # str_edit = str(edit)
    # edited_weapon = str_edit.split('&')
    # for i in edited_weapon:
    #     raw_data = i.split("=")
    #     FweapName = raw_data[0]
    
    
    return redirect('inventory')

def subtract_Stock(request, pk, x):
    Main_Stock = weapon.objects.get(pk=pk)
    Subtracted = Main_Stock.weapon_Stock - int(x)
    Main_Stock.weapon_Stock = Subtracted
    Main_Stock.save()
    return Subtracted

def confirm_order(request):
    if(request.method == "POST"):
        ptype = request.POST.get("payment_method")
        weaps = request.POST.get("complete_order")
        total_amt = request.POST.get("total_amount")
        weap_ord = order.objects.create(total_amount_paid=total_amt, payment_type=ptype)

        weap_fixed = weaps[:-1]
        stuff = weap_fixed.split("-")
        for it in stuff:
            row_item = it.split(":")
            weap_obj = weapon.objects.get(pk=int(row_item[0]))
            subtract_Stock(request, pk=it[0],x=int(row_item[1]))
            itprice = weap_obj.getPrice()
            lt = itprice * int(row_item[1])
            weapon_order.objects.create(weapon_ID =weap_obj, order_ID=weap_ord, line_Total=lt, quantity=row_item[1])
        return redirect('home')
