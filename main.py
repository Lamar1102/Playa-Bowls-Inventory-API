from order_request import OrderRequest
from adding_bowls import AddingBowls
from inventory import Inventory
from inventory import Mods


order_request = OrderRequest()
# NEWARK INFO
newark_dictionaries = order_request.newark_report
newark_inventory_sold = newark_dictionaries[0]
newark_mod_sold = newark_dictionaries[1]



newark_inventory = Inventory(newark_inventory_sold)
newark_bowls_sold = newark_inventory.bowl_dictionary
print(newark_bowls_sold)

newark_mods_sold = Mods(newark_mod_sold,newark_inventory_sold)
newark_total_used = newark_mods_sold.inventory_used
print(newark_total_used)


# RUTHERFORD INFO
rutherford_dictionaries = order_request.rutherford_report
rutherford_inventory_sold = rutherford_dictionaries[0]
rutherford_mod_sold = rutherford_dictionaries[1]

rutherford_inventory = Inventory(rutherford_inventory_sold)
rutherford_bowls_sold = rutherford_inventory.bowl_dictionary
print(rutherford_bowls_sold)

rutherford_mods_sold = Mods(rutherford_mod_sold,rutherford_inventory_sold)
rutherford_total_used = rutherford_mods_sold.inventory_used
print(rutherford_total_used)

# Watchung Info
watchung_dictionaries = order_request.watchung_report
watchung_inventory_sold = watchung_dictionaries[0]
watchung_mod_sold = watchung_dictionaries[1]


watchung_inventory = Inventory(watchung_inventory_sold)
watchung_bowls_sold = watchung_inventory.bowl_dictionary
print(watchung_bowls_sold)

watchung_mods_sold = Mods(watchung_mod_sold,watchung_inventory_sold)
watchung_total_used = watchung_mods_sold.inventory_used
print(watchung_total_used)

# Union City Info
uc_dictionaries = order_request.uc_report
uc_inventory_sold = uc_dictionaries[0]
uc_mod_sold = uc_dictionaries[1]

uc_inventory = Inventory(uc_inventory_sold)
uc_bowls_sold = uc_inventory.bowl_dictionary
print(uc_bowls_sold)

uc_mods_sold = Mods(uc_mod_sold,uc_inventory_sold)
uc_total_used = uc_mods_sold.inventory_used
print(uc_total_used)

# Hoboken Info
hoboken_dictionaries = order_request.hoboken_report
hoboken_inventory_sold = hoboken_dictionaries[0]
hoboken_mod_sold = hoboken_dictionaries[1]

hoboken_inventory = Inventory(hoboken_inventory_sold)
hoboken_bowls_sold = hoboken_inventory.bowl_dictionary
print(hoboken_bowls_sold)

hoboken_mods_sold = Mods(hoboken_mod_sold,hoboken_inventory_sold)
hoboken_total_used = hoboken_mods_sold.inventory_used
print(hoboken_total_used)

# Elizabeth Info
elizabeth_dictionaries = order_request.elizabeth_report
elizabeth_inventory_sold = elizabeth_dictionaries[0]
elizabeth_mod_sold = elizabeth_dictionaries[1]

elizabeth_inventory = Inventory(elizabeth_inventory_sold)
elizabeth_bowls_sold = elizabeth_inventory.bowl_dictionary
print(elizabeth_bowls_sold)

elizabeth_mods_sold = Mods(elizabeth_mod_sold,elizabeth_inventory_sold)
elizabeth_total_used = elizabeth_mods_sold.inventory_used
print(elizabeth_mod_sold)
print(elizabeth_total_used)



