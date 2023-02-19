import numpy as np
import math

ability_modifiers = {3:-3, 4:-2, 5:-2, 6:-1, 7:-1, 8:-1,
                     9:0 , 10:0, 11:0, 12:0, 13:1, 14:1,
                     15:1, 16:2, 17:2, 18:3}

# Minimum of 1 spell
wizard_spells_known = {3:"No spellcasting possible", 4:"-2 spells",
                       5:"-2 spells", 6:"-1 spells", 7:"-1 spells",
                       8:"No adjustment", 9:"No adjustment",
                       10:"No adjustment", 11:"No adjustment",
                       12:"No adjustment", 13:"No adjustment",
                       14:"+1 spell", 15:"+1 spell", 16:"+1 spell",
                       17:"+2 spells", 18:"+2 spells"}   

# Bassed on Intelligence for wizards and Personality for Clerics
max_spell_level = {3:0, 4:1, 5:1, 6:1, 7:1, 8:2, 9:2, 10:3,
                   11:3, 12:4, 13:4, 14:4, 15:5, 16:5, 17:5,
                   18:5}

lucky_signs = {1: "Harsh winter: All attack rolls",
2: "The bull: Melee attack rolls",
3: "Fortunate date: Missile fire attack rolls",
4: "Raised by wolves: Unarmed attack rolls",
5: "Conceived on horseback: Mounted attack rolls",
6: "Born on the battlefield: Damage rolls",
7: "Path of the bear: Melee damage rolls",
8: "Hawkeye: Missile fire damage rolls",
9: "Pack hunter: Attack and damage rolls for 0-level starting weapon",
10: "Born under the loom: Skill checks (including thief skills)",
11: "Fox’s cunning: Find/disable traps",
12: "Four-leafed clover: Find secret doors",
13: "Seventh son: Spell checks",
14: "The raging storm: Spell damage",
15: "Righteous heart: Turn unholy checks",
16: "Survived the plague: Magical healing*",
17: "Lucky sign: Saving throws",
18: "Guardian angel: Savings throws to escape traps",
19: "Survived a spider bite: Saving throws against poison",
20: "Struck by lightning: Reflex saving throws",
21: "Lived through famine: Fortitude saving throws",
22: "Resisted temptation: Willpower saving throws",
23: "Charmed house: Armor Class",
24: "Speed of the cobra: Initiative",
25: "Bountiful harvest: Hit points (applies at each level)",
26: "Warrior’s arm: Critical hit tables**",
27: "Unholy house: Corruption rolls",
28: "The Broken Star: Fumbles**",
29: "Birdsong: Number of languages",
30: "Wild child: Speed (each +1/-1 = +5’/-5’ speed)}"}  

occupations = {
1:["Alchemist", "Staff", "Oil (1 flask)"],
2:["Animal Trainer", "Club", "Pony"],
3:["Armorer", "Hammer (as club)", "Iron Helmet"],
4:["Astrologer", "Dagger", "Spyglass"],
5:["Barber", "Razor (as dagger)", "Scissors"],
6:["Beadle", "Staff", "Holy Symbol"],
7:["Beekeeper", "Staff", "Jar of Honey"],
8:["Blacksmith", "Hammer (as club)", "Steel tongs"],
9:["Butcher", "Cleaver (as axe)", "Side of beef"],
10:["Caravan guard", "Short sword", "Linen (1 yard)"],
11:["Cheesemaker", "Cudgel (as staff)", "Stinky cheese"],
12:["Cobbler", "Awl (as dagger)", "Shoehorn"],
13:["Confidence artist", "Dagger", "Quality Cloak"],
14:["Cooper", "Crowbar (as club)", "Barrel"],
15:["Costermonger", "Knife (as dagger)", "Fruit"],
16:["Cutpurse", "Dagger", "Small chest"],
17:["Ditch digger", "Shovel (as staff)", "1lb Fine dirt"],
18:["Dock worker", "Pole (as staff)", "1 late RPG book"],
19:["Dwarven apothecarist", "Cudgel (as staff)", "Steel vial"],
20:["Dwarven blacksmith", "Hammer (as club)", "1 oz. Mithril"],
21:["Dwarven chest-maker", "Chisel (as dagger)", "10 lbs. Wood"],
22:["Dwarven herder", "Staff", "Sow"],
23:["Dwarven miner", "Pick (as club)", "Lantern"],
24:["Dwarven miner", "Pick (as club)", "Lantern"],
25:["Dwarven mushroom-farmer", "Shovel (as staff)", "Sack"],
26:["Dwarven rat-catcher", "Club", "Net"],
27:["Dwarven stonemason", "Hammer", "10lbs. Fine stone"],
28:["Dwarven stonemason", "Hammer", "10lbs. Fine stone"],
29:["Elven artisan", "Staff", "1lb. Clay"],
30:["Elven barrister", "Quill (as dart)", "Book"],
31:["Elven chandler", "Scissors (as dagger)", "20 Candles"],
32:["Elven falconer", "Dagger", "Falcon"],
33:["Elven forester", "Staff", "1lb. Herbs"],
34:["Elven forester", "Staff", "1lb. Herbs"],
35:["Elven glassblower", "Hammer (as club)", "Glass beads"],
36:["Elven navigator", "Shortbow", "Spyglass"],
37:["Elven sage", "Dagger", "Parchement and quill"],
38:["Elven sage", "Dagger", "Parchement and quill"],
39:["Farmer", "Pitchfork (as spear)", "Hen"],
40:["Farmer", "Pitchfork (as spear)", "Hen"],
41:["Farmer", "Pitchfork (as spear)", "Hen"],
42:["Farmer", "Pitchfork (as spear)", "Hen"],
43:["Farmer", "Pitchfork (as spear)", "Hen"],
44:["Farmer", "Pitchfork (as spear)", "Hen"],
45:["Farmer", "Pitchfork (as spear)", "Hen"],
46:["Farmer", "Pitchfork (as spear)", "Hen"],
47:["Farmer", "Pitchfork (as spear)", "Hen"],
48:["Fortune-teller", "Dagger", "Tarot deck"],
49:["Gambler", "Club", "Dice"],
50:["Gongfarmer", "Trowel (as dagger)", "Sack of night soil"],
51:["Grave digger", "Shovel (as staff)", "Trowel"],
52:["Grave digger", "Shovel (as staff)", "Trowel"],
53:["Guild beggar", "Sling", "Crutches"],
54:["Guild beggar", "Sling", "Crutches"],
55:["Halfling chicken butcher", "Hand axe", "5lbs. Chicken meat"],
56:["Halfling dyer", "Staff", "3 yds. fabric"],
57:["Halfling dyer", "Staff", "3 yds. fabric"],
58:["Halfling glovemaker", "Awl (as dagger)", "4 pairs Gloves"],
59:["Halfling gypsy", "Sling", "Hex doll"],
60:["Halfling haberdasher", "Scissors (as dagger)", "3 Fine suits"],
61:["Halfling mariner", "Knife (as dagger)", "2 yds. Sailcloth"],
62:["Halfling moneylender", "Short sword", "5gp., 10sp., 200cp."],
63:["Halfling trader", "Short sword", "20sp."],
64:["Halfling vagrant", "Club", "Begging bowl"],
65:["Healer", "Club", "1 vial Holy water"],
66:["Herbalist", "Club", "1lb. Herbs"],
67:["Herder", "Staff", "Herding dog"],
68:["Hunter", "Shortbow", "Deer pelt"],
69:["Hunter", "Shortbow", "Deer pelt"],
70:["Indentured servant", "Staff", "Locket"],
71:["Jester", "Dart", "Silk clothes"],
72:["Jeweler", "Dagger", "Gem worth 20gp."],
73:["Locksmith", "Dagger", "Fine tools"],
74:["Mendicant", "Club", "Cheese dip"],
75:["Mercenary", "Longsword", "Hide armor"],
76:["Merchant", "Dagger", "4gp., 14sp., 27cp."],
77:["Miller/baker", "Club", "1 lb. Flour"],
78:["Minstrel", "Dagger", "Ukulele"],
79:["Noble", "Longsword", "GOld ring worth 10gp."],
80:["Orphan", "Club", "Rag doll"],
81:["Ostler", "Staff", "Bridle"],
82:["Outlaw", "Short sword", "Leather armor"],
83:["Rope Maker", "Knife (as dagger)", "100' Rope"],
84:["Scribe", "Dart", "10 sheets Parchment"],
85:["Shaman", "Feathered bone club", "Corn badge"],
86:["Slave", "Club", "Strange-looking rock"],
87:["Smuggler", "Sling", "Waterproof sack"],
88:["Soldier", "Spear", "Shield"],
89:["Squire", "Longsword", "Steel helmer"],
90:["Squire", "Longsword", "Steel helmer"],
91:['Tax collector", "Longsword", "100 cp.'],
92:["Trapper", "Sling", "Badger pelt"],
93:["Trapper", "Sling", "Badger pelt"],
94:["Urchin", "Stick (as club)", "Begging bowl"],
95:["Wainwright", "Club", "Pushcart"],
96:["Weaver", "Dagger", "Fine suit of clothes"],
97:["Wizard's apprentice", "Dagger", "Black grimoire"],
98:["Woodcutter", "Handaxe", "Bundle of wood"],
99:["Woodcutter", "Handaxe", "Bundle of wood"],
100:["Woodcutter", "Handaxe", "Bundle of wood"]
}

equipment_rolled = {
1:"Backpack",
2:"Candle",
3:"10' Chain",
4:"1 pc. Chalk",
5:"Empty chest",
6:"Crowbar",
7:"Empty flask",
8:"Flint & steel",
9:"Grappling hook",
10:"Small hammer",
11:"Holy symbol",
12:"1 vial Holy water",
13:"Iron spike",
14:"Lantern",
15:"Hand-sized mirror",
16:"1 flask oil",
17:"10' pole",
18:"1 day rations",
19:"50' rope",
20:"Large sack",
21:"Small sack",
22:"Thieves' tools",
23:"Torch",
24:"Waterskin"
}

equipment= {
"Backpack":2*10*10,
"Candle":1,
"10' Chain":30*10*10,
"1 pc. Chalk":1,
"Empty chest":2*10*10,
"Crowbar":2*10*10,
"Empty flask":3,
"Flint & steel":15,
"Grappling hook":1*10*10,
"Small hammer":5*10,
"Holy symbol":25*10*10,
"1 vial Holy water":25*10*10,
"Iron spike":1*10,
"Lantern":10*10*10,
"Hand-sized mirror":10*10*10,
"1 flask oil":2*10,
"10' pole":15,
"1 day rations":5,
"50' rope":25,
"Large sack":12,
"Small sack":8,
"Thieves' tools":25*10*10,
"Torch":1,
"Waterskin":5*10
}

weapon_damage = {
    "Battleaxe":[1,10],
    "Blackjack":[1,3,2,6],
    "Blowgun":[1,3,1,5],
    "Club":[1,4],
    "Crossbow":[1,6],
    "Dagger":[1,4,1,10],
    "Dart":[1,4],
    "Flail":[1,6],
    "Garrote":[1,1,3,4],
    "Handaxe":[1,6],
    "Javelin":[1,6],
    "Lance":[1,12],
    "Longbow":[1,6],
    "Longsword":[1,8],
    "Mace":[1,6],
    "Polearm":[1,10],
    "Shortbow":[1,6],
    "Short sword":[1,6],
    "Sling":[1,4],
    "Spear":[1,8],
    "Staff":[1,4],
    "Two-handed sword":[1,10],
    "Warhammer":[1,8]
}

weapon_cost = {
    "Battleaxe",
    "Blackjack",
    "Blowgun",
    "Club",
    "Crossbow",
    "Dagger",
    "Dart",
    "Flail",
    "Garrote",
    "Handaxe",
    "Javelin",
    "Lance",
    "Longbow",
    "Longsword",
    "Mace",
    "Polearm",
    "Shortbow",
    "Short sword",
    "Sling",
    "Spear",
    "Staff",
    "Two-handed sword",
    "Warhammer"
}

from urllib.parse import SplitResultBytes
class DCC_Character:
    def __init__(self, name, alignment):
        self.name = name
        print("******************************")
        print("Character:", name)
        print("******************************")
        print()

        dr = DiceRoller()
        # Determine ability scores; 3d6 in order for each. 
        # Note ability modifiers on Table 1-1. The abilities are: 
        # Strength, Agility, Stamina, Intelligence, Personality, Luck.
        self.strength = dr.d6()+dr.d6()+dr.d6()
        self.agility = dr.d6()+dr.d6()+dr.d6()
        self.stamina = dr.d6()+dr.d6()+dr.d6()
        self.intelligence = dr.d6()+dr.d6()+dr.d6()
        self.personality = dr.d6()+dr.d6()+dr.d6()
        self.luck = dr.d6()+dr.d6()+dr.d6()

        self.strength_modifier = ability_modifiers[self.strength]
        self.agility_modifier = ability_modifiers[self.agility]
        self.stamina_modifier = ability_modifiers[self.stamina]
        self.intelligence_modifier = ability_modifiers[self.intelligence]
        self.personality_modifier = ability_modifiers[self.personality]
        self.luck_modifier = ability_modifiers[self.luck]  

        ability_scores = {"strength":[self.strength, self.strength_modifier],
                          "agility":[self.agility, self.agility_modifier],
                          "stamina":[self.stamina, self.stamina_modifier],
                          "intelligence":[self.intelligence, self.intelligence_modifier],
                          "personality":[self.personality, self.personality_modifier],
                          "luck":[self.luck, self.luck_modifier]}
        self.ability_scores = pd.DataFrame(ability_scores)

        print("******************************")
        print("Ability Scores and Modifiers:")
        print("******************************")
        print(self.ability_scores.head())  
        print()

        # Determine hit points; roll 1d4, adjusted by Stamina modifier.
        self.hit_points = dr.d4(self.stamina_modifier)
        print("******************************")
        print("Hit Points:", self.hit_points)
        print("******************************")
        print() 

        # Determine Lucky Sign; roll 1d30, adjusted by Luck modifier on Table 1-2. 
        # The resultant Lucky Roll modifier associated with that Lucky Sign is permanent 
        # and does not change later when Luck is spent.   
        self.lucky_sign = dr.d30()
        self.lucky_sign_text = lucky_signs[self.lucky_sign]
        print("******************************")
        print("Lucky Sign:", self.lucky_sign)
        print(self.lucky_sign_text)
        print("******************************")
        print() 

        # Determine 0-level occupation; roll 1d100 on Table 1-3. This result will 
        # tell include the character’s 0-level start- ing weapon and trade goods.
        occupation_roll = dr.d100() 
        occupation_data = occupations[occupation_roll]
        self.occupation = occupation_data[0]
        self.weapon = occupation_data[1]
        self.inventory = [occupation_data[1], occupation_data[2]]
        self.money = 0
        if occupation_roll == 62:
            self.inventory = [occupation_data[1]]
            self.money = 200 + 10*10 + 5*10*10
        if occupation_roll == 63:
            self.inventory = [occupation_data[1]]
            self.money = 20*10  
        if occupation_roll == 76:
            self.inventory = [occupation_data[1]]  
            self.money = 27 + 14*10 + 4*10*10  
        if occupation_roll == 91:
            self.inventory = [occupation_data[1]]
            self.money = 100                               
        print("******************************")
        print("Occupation:", self.occupation)
        print("Trained Weapon:", self.weapon)
        print("Inventory:", self.inventory)
        print("******************************")
        print()  
        
        self.weapon_damage = 0
        self.equip_weapon(self.weapon, None)
        print("******************************")
        print(self.weapon, "equipped with a damage of", self.weapon_damage)
        print("******************************")
        print() 

        # Choose an alignment.
        self.alignment = alignment
        print("******************************")
        print("Alignment:", self.alignment)
        print("******************************")
        print() 

        # Determine starting money; roll 5d12 copper pieces
        self.money = self.money + dr.d12()+dr.d12()+dr.d12()+dr.d12()+dr.d12()
        print("******************************")
        print("Starting Money:", self.format_money())
        print("******************************")
        print()  

        random_equipment = equipment_rolled[dr.d24()]
        self.inventory.append(random_equipment)
        print("******************************")
        print("Random Starting Item:", random_equipment)
        print("Inventory:", self.inventory)
        print("******************************")
        print()

    def equip_weapon (self, weapon_name, modifier):
        dr = DiceRoller()
        try:
            new_weapon = weapon_name
            self.weapon = weapon_name
            new_weapon_stats = weapon_damage[new_weapon]
            if modifier=="sneak" or modifier=="Sneak":
                self.weapon_damage = new_weapon_stats[2:4]
            else:
                self.weapon_damage = new_weapon_stats[:2]
        except:
            found = False
            for weapon in weapon_damage.keys():
                if weapon in weapon_name or weapon.lower() in weapon_name:
                    new_weapon = weapon
                    self.weapon = weapon
                    new_weapon_stats = weapon_damage[new_weapon]
                    if modifier=="sneak" or modifier=="Sneak":
                        self.weapon_damage = new_weapon_stats[2:4]
                    else:
                        self.weapon_damage = new_weapon_stats[:2]
                    found = True
            if not found:
                print(weapon_name, "is not a valid weapon.")
                print("Valid weapons are:")
                self.print_nice_dict(weapon_damage)
                print()
            
    def change_weapon(self):
        print ("TO BE IMPLEMENTED")

    def attack(self, mod):
        dr = DiceRoller()
        damage = dr.roll(self.weapon_damage[1],mod,self.weapon_damage[0])
        print("******************************")
        print("Weapon:", self.weapon)
        print("Damage:", damage)
        print("******************************")


    def update_hit_points(self, change):
        self.hit_points = self.hit_points + change
        print()
        print("New Hit Points:", self.hit_points)

    def buy_equipment(self, item):
        try:
            cost = equipment[item]
            if cost <= self.money:
                self.inventory.append(item)
                self.money = self.money - cost
                print()
                print("Purchased", item)
                print("Money Remaining:", self.format_money())
                print()
            else:
                print()
                print("Not enough money to purchase", item)
                print("Cost:", cost)
                print("Current Money:", self.format_money())
                print()
    
        except KeyError:
            print()
            print("Item is Not Avaliable for Sale.")
            print("Items Avaliable Are:")
            self.print_dict_nice(equipment)
            print("If trying to buy a weapon, use \"buy_weapon\".")
            print()

    def buy_weapon(self, item):
        try:
            cost = weapon_cost[item]
            if cost <= self.money:
                self.inventory.append(item)
                self.money = self.money - cost
                print()
                print("Purchased", item)
                print("Money Remaining:", self.format_money())
                print()
            else:
                print()
                print("Not enough money to purchase", item)
                print("Cost:", cost)
                print("Current Money:", self.format_money())
                print()
    
        except KeyError:
            print()
            print("Item is Not Avaliable for Sale.")
            print("Items Avaliable Are:")
            self.print_dict_nice(weapon_cost)
            print("If trying to buy a equipment use \"buy_equipment\".")
            print()

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def check_inventory(self):
        self.print_list_nice(self.inventory)

    def check_money(self):
        return self.format_money()

    def format_money(self):
        money = self.money
        gp = 0
        sp = 0
        cp = 0
        while money >= 100:
            gp = gp + 1
            money = money - 100
        while money >= 10:
            sp = sp + 1
            money = money - 10
        cp = money
        return "GP: "+str(gp)+" SP: "+str(sp)+" CP: "+str(cp)

    def print_dict_nice (self, adict):
        keys = list(adict.keys())
        for i in range(0,len(keys),3):
            if len(keys) - i <= 3:
                if len(keys) - i == 2:
                    print(keys[i], ",", keys[i+1])
                elif len(keys) - i == 1:
                    print(keys[i])
                else:
                    print(keys[i], ",", keys[i+1], ",", keys[i+2])
            else:
                print(keys[i], ",", keys[i+1], ",", keys[i+2], ",")

    def print_list_nice(self, alist):
        for i in range(0,len(alist),3):
            if len(alist) - i <= 3:
                if len(alist) - i == 2:
                    print(alist[i], ",", alist[i+1])
                elif len(alist) - i == 1:
                    print(alist[i])
                else:
                    print(alist[i], ",", alist[i+1], ",", alist[i+2])
            else:
                print(alist[i], ",", alist[i+1], ",", alist[i+2], ",")

