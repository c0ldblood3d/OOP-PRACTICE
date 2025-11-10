from Appliance import Appliance, Blender, Toaster, Kettle

kitchen = []
kitchen.append(Blender(800, "SuperBlend", "Philips", 2022))
kitchen.append(Toaster("Deluxe Toaster", "Bosch", 2021))
kitchen.append(Kettle("Electric Kettle", "Tefal", 2023))
kitchen.append(Blender(1200, "ProMix", "Moulinex", 2022))
kitchen.append(Toaster("Compact Toaster", "Samsung", 2020))
    
for appliance in kitchen:
    print(f"{appliance} - {appliance.operate()}")
    
kitchen = [appliance for appliance in kitchen if not isinstance(appliance, Blender)]
    
for appliance in kitchen:
    print(f"{appliance} - {appliance.operate()}")