from django.db import models

# Create your models here.
class weapon(models.Model):
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
    WEAPON_TYPES = [
        (AMMUNITION, 'Ammo'),
        (FINESSE, 'Fin'),
        (HEAVY, 'Heavy'),
        (IMPROVISED, 'Improv'),
        (LIGHT, 'Light'),
        (LOADING, 'Load'),
        (MARTIAL, 'Martial'),
        (RANGED, 'Range'),
        (REACH, 'Reach'),
        (SPECIAL, 'Special'),
        (THROWN, 'Thrown'),
        (TWOHANDED, 'TwoHand'),
        (VERSATILE, 'Vers'),
    ]



    weapon_Name = models.CharField(max_length=100)
    weapon_Price = models.DecimalField(max_digits=6, decimal_places=2)
    weapon_Type = models.CharField(max_length=2, choices=WEAPON_TYPES, default=AMMUNITION)
    objects = models.Manager()

    def getName(self):
        return self.weapon_Name
    def getPrice(self):
        return self.weapon_Price
    def getType(self):
        return self.weapon_Type
    def __str__(self):
        return str(self.pk) + ": " + self.weapon_Name

class order(models.Model):
    CASH = 'CH'
    CREDIT = 'CT'
    PAYMENT_TYPE  = [
        (CASH, 'Cash'),
        (CREDIT, 'Credit'),
    ]

    total_amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateField()
    payment_type = models.CharField(max_length=2,choices=PAYMENT_TYPE, default=None)
    objects = models.Manager()

    def getTotalAmt(self):
        return self.total_amount_paid

    def getOrderDate(self):
        return self.order_date
    
    def getPaymentType(self):
        return self.payment_type
    
    def getPK(self):
        return str(self.pk) + ": " + self.order_date + ";\n Amount Paid:" + self.total_amount_paid

    def __str__(self):
        return str(self.pk)

class weapon_order(models.Model):
    weapon_ID = models.ForeignKey('Weapon', on_delete=models.CASCADE)
    order_ID = models.ForeignKey('Order', on_delete=models.CASCADE)
    line_Total = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    objects = models.Manager()

    def getWeaponOrder(self):
        return "Order Number: " + self.order_ID + "\nWeapon Number: " + self.weapon_ID
    
    def getTotalLine(self):
        return "Total Lines: " + self.line_Total

    def getQuantity(self):
        return "Quantity: " + self.quantity

    def __str__(self):
        return "Weapon_Order_ID: " + self.pk + "\nOrder Number: " + self.order_ID + "\nWeapon Number: " + self.weapon_ID