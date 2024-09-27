coinCrop = 0
coinPet = 0
coinBountiful = 0
armorLoot = 0

print("Welcome to 0b8's Crop Profit Calculator!")

print("\nWhat crop would you like to view your rates for?")
print("List includes: Wheat, Potato, Carrot, Pumpkin, Melon, Cane, Mushroom, Cactus, Cocoa, Wart")

crop = input("\nEnter here: ")

cropPrice = 0
cropDrops = 0
seedPrice = 0
seedDrops = 0
coinSeeds = 0

if crop == "Potato":
    cropPrice = 3
    cropDrops = 3
elif crop == "Wheat":
    cropPrice = 6
    cropDrops = 1
    seedPrice = 3
    seedDrops = 1.5
elif crop == "Carrot":
    cropPrice = 3
    cropDrops = 3
elif crop == "Pumpkin":
    cropPrice = 10
    cropDrops = 1
elif crop == "Melon":
    cropPrice = 2
    cropDrops = 5
elif crop == "Cane":
    cropPrice = 4
    cropDrops = 2
elif crop == "Mushroom":
    cropPrice = 10
    cropDrops = 1
elif crop == "Cactus":
    cropPrice = 3
    cropDrops = 2
elif crop == "Cocoa":
    cropPrice = 3
    cropDrops = 3
elif crop == "Wart":
    cropPrice = 4
    cropDrops = 2.5
else:
    print("Invalid crop.")
    input("Enter again: ")
print("\nGreat choice!")

print("\nWhat is your farming fortune?")
farmFort = float(input("Enter here: "))

print("\nThank you!")

coinPet = 0

print("\nAre you using a Mooshroom Cow?")
pet = input("Yes or no?: ")
if pet == "Yes" and crop in ["Cane", "Cactus"]:
    coinPet = 1440000
elif pet == "Yes":
    coinPet = 720000
else:
    coinPet = 0

print("\nIs your reforge on Bountiful?")
bountiful = input("Yes or no?: ")

if crop in ["Potato", "Wheat", "Carrot"]:
    cropArmor = "or Melon Armor?"
elif crop in ["Pumpkin", "Melon", "Cocoa"]:
    cropArmor = "or Cropie Armor?"
elif crop in ["Cane", "Wart", "Mushroom"]:
    cropArmor = "or Squash Armor?"
else:
    cropArmor = "?" #If crop is not one of those

print("\nAre you wearing 3/4 or 4/4 Fermento", cropArmor)
armorAmount = input("Enter here: ")

armorLoot = 0

if crop in ["Potato", "Wheat", "Carrot"]:
    if armorAmount == "3/4":
        armorLoot = 720000
    elif armorAmount == "4/4":
        armorLoot = 900000
elif crop in ["Pumpkin", "Melon", "Cocoa"]:
    if armorAmount == "3/4":
        armorLoot = 1080000
    elif armorAmount == "4/4":
        armorLoot = 1620000
elif crop in ["Wart", "Mushroom"]:
    if armorAmount == "3/4":
        armorLoot = 1080000
    elif armorAmount == "4/4":
        armorLoot = 1260000
elif crop in ["Cane", "Cactus"]:
    if armorAmount == "3/4":
        armorLoot = 1080000 * 2
    elif armorAmount == "4/4":
        armorLoot = 1260000 * 2
else:
    armorLoot = 0  # Default to 0 if no conditions match


bpSecond = 20
bpMinute = bpSecond * 60
bpHour = bpMinute * 60

formatted_coinCrop = 0

if crop in ["Carrot", "Cocoa", "Wart", "Potato"]:
    coinCrop = round(float(bpHour) * (float(cropDrops) * (float(farmFort) + 100) / 100 - 1) * cropPrice)
    formatted_coinCrop = "{:,}".format(coinCrop)
else:
    pass

if crop in ["Mushroom", "Pumpkin", "Melon", "Cane", "Cactus", "Wheat"]:
    coinCrop = round(float(bpHour) * (float(cropDrops) * (float(farmFort) + 100) / 100) * cropPrice)
    formatted_coinCrop = "{:,}".format(coinCrop)
    if crop == "Wheat":
        coinSeeds = round(float(bpHour) * (float(seedDrops) * (float(farmFort) + 100) / 100 - 1) * seedPrice)
else:
    pass

formatted_coinBountiful = 0
formatted_coinSeedsBountiful = 0

if bountiful == "Yes":
    coinBountiful = round(float(bpHour) * float(cropDrops) * (float(farmFort) + 100) / 100 * 0.2)
    formatted_coinBountiful = "{:,}".format(coinBountiful)
else:
    pass

coinSeedsBountiful = 0

if crop == "Wheat":
    coinSeedsBountiful = round(float(bpHour) * float(seedDrops) * (float(farmFort) + 100) / 100 * 0.2)
    formatted_coinSeedsBountiful = "{:,}".format(coinSeedsBountiful)
else:
    pass

coinDicer = 0

if crop == "Melon":
    print("\nWhat version of Melon Dicer do you use?")
    dicer = input("Enter here (1.0, 2.0, 3.0): ")
    if dicer == "1.0":
        coinDicer = 346722
    elif dicer == "2.0":
        coinDicer = 719655
    elif dicer == "3.0":
        coinDicer = 1117420
    else:
        pass
elif crop == "Pumpkin":
    print("\nWhat version of Pumpkin Dicer do you use?")
    dicer = input("Enter here (1.0, 2.0, 3.0): ")
    if dicer == "1.0":
        coinDicer = 432542
    elif dicer == "2.0":
        coinDicer = 857031
    elif dicer == "3.0":
        coinDicer = 1271170
    else:
        pass
else:
    pass

print("\nYour coins from %s will be:" % crop, formatted_coinCrop)
if crop == "Wheat":
    formatted_coinSeeds = "{:,}".format(int(coinSeeds))
    print("Your coins from Seeds will be:", formatted_coinSeeds)

formatted_coinPet = "{:,}".format(int(coinPet))

if pet == "Yes":
    print("Your coins from your Mooshroom Cow will be:", formatted_coinPet)
else:
    pass

if bountiful == "Yes":
    print("Your coins from Bountiful will be:", formatted_coinBountiful)
else:
    pass

if crop == "Wheat":
    print("Your coins from Bountiful (Seeds) will be:", formatted_coinSeedsBountiful)
else:
    pass


formatted_armorLoot = "{:,}".format(int(armorLoot))
print("Your coins from your armor's drops will be:", formatted_armorLoot)

if crop in ["Melon", "Pumpkin"]:
    formatted_coinDicer = "{:,}".format(int(coinDicer))
    print("Your coins from your tool will be:", formatted_coinDicer)
else:
    pass

coinTotal = round(coinCrop + coinPet + coinBountiful + armorLoot + coinDicer + coinSeeds + coinSeedsBountiful)
formatted_coinTotal = "{:,}".format(coinTotal)
print("\nYour total coins per hour from farming %s will be %s!" % (crop, formatted_coinTotal))
