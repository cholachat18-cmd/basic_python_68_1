"""
#
# Functions
#
"""
def myfullName(firstName="Unknown", lastName="Forger"):
    return firstName + " " + lastName

print(myfullName("Loid", "Komodo"))
print(myfullName("Hordi"))
print(myfullName())
print(myfullName(lastName="smith"))
print(myfullName("Anna", "Forger"))
print(myfullName("Yorn", "Forger"))
print(myfullName("band", "Forger"))

def redPotion(hp):
    return hp + 50
def bluePotion(mp):
    return mp + 30

current_hp = 70
print("Current HP:", current_hp)
current_hp = redPotion(current_hp)
print("After using Red Potion HP:", current_hp)