from adding_bowls import AddingBowls
from order_request import OrderRequest

class Inventory(AddingBowls):
    def __init__(self,dictionary):
        super().__init__()


        self.ave = self.total("8th Ave- Acai Bowl","8th Ave- Acai Bowl TPD", dictionary)
        self.pura_vida = self.total("Pura Vida- Acai Bowl","Pura Vida- Acai Bowl TPD", dictionary)
        self.nutella = self.total("Nutella- Acai Bowl","Nutella- Acai Bowl TPD", dictionary)
        self.tropical = self.total("Tropical- Acai Bowl","Tropical- Acai Bowl TPD", dictionary)
        self.custom_acai = self.total("Custom Acai Bowl- Includes Granola","Custom Acai Bowl- Includes Granola TPD", dictionary)
        self.power = self.total("Power- Acai Bowl","Power- Acai Bowl TPD", dictionary)
        self.acai_bowls = self.pura_vida+self.nutella+self.tropical+self.custom_acai+self.power+self.ave

        self.pink_flamingo = self.total("Pink Flamingo- Pitaya Bowl","Pink Flamingo- Pitaya Bowl TPD", dictionary)
        self.dragonberry = self.total("Dragonberry- Pitaya Bowl","Dragonberry- Pitaya Bowl TPD", dictionary)
        self.electric_mermaid = self.total("Electric Mermaid- Pitaya Bowl","Electric Mermaid- Pitaya Bowl TPD", dictionary)
        self. nutaya = self.total("Nutaya- Pitaya Bowl","Nutaya- Pitaya Bowl TPD", dictionary)
        self.goji = self.total("Goji- Pitaya Bowl","Goji- Pitaya Bowl TPD", dictionary)
        self.pink_power = self.total("Pink Power- Pitaya Bowl","Pink Power- Pitaya Bowl TPD", dictionary)
        self.custom_pitaya = self.total("Custom Pitaya Bowl- Includes Granola","Custom Pitaya Bowl- Includes Granola TPD", dictionary)
        self.pitaya_bowls = self.pink_flamingo+self.dragonberry+self.electric_mermaid+self.nutaya+self.goji+self.pink_power+self.custom_pitaya

        self.the_jetty = self.total("The Jetty- Chia Pudding Bowl","The Jetty- Chia Pudding Bowl TPD", dictionary)
        self.almond_joy = self.total("Almond Joy- Chia Pudding Bowl","Almond Joy- Chia Pudding Bowl TPD", dictionary)
        self.trailblazer = self.total("Trailblazer- Chia Pudding Bowl","Trailblazer- Chia Pudding Bowl TPD", dictionary)
        self.chiatella = self.total("Chia Tella- Chia Pudding Bowl","Chia Tella- Chia Pudding Bowl TPD", dictionary)
        self.oh_mega = self.total("Oh Mega- Chia Pudding Bowl","Oh Mega- Chia Pudding Bowl TPD", dictionary)
        self.custom_chia = self.total("Custom Chia Bowl- Includes Granola","Custom Chia Bowl- Includes Granola TPD", dictionary)
        self.chia_bowls = self.the_jetty+self.almond_joy+self.trailblazer+self.chiatella+self.oh_mega+self.custom_chia

        self.ocean = self.total("Ocean Ave- Green Bowl","Ocean Ave- Green Bowl TPD", dictionary)
        self.lola = self.total("Lola- Green Bowl","Lola- Green Bowl TPD", dictionary)
        self.pacific = self.total("Pacific- Green Bowl","Pacific- Green Bowl TPD", dictionary)
        self.hemp = self.total("Hemp- Green Bowl","Hemp- Green Bowl TPD", dictionary)
        self.green_power = self.total("Green Power- Green Bowl","Green Power- Green Bowl TPD", dictionary)
        self.custom_green = self.total("Custom Green Bowl- Includes Granola","Custom Green Bowl- Includes Granola TPD", dictionary)
        self.green_bowls = self.ocean+self.lola+self.pacific+self.hemp+self.green_power+self.custom_green

        self.coco_bowl = self.total("Coco- Coconut Bowl","Coco- Coconut Bowl TPD", dictionary)
        self.coco_berry = self.total("Coco Berry- Coconut Bowl","Coco Berry- Coconut Bowl TPD", dictionary)
        self.coco_craze = self.total("Coco Craze- Coconut Bowl","Coco Craze- Coconut Bowl TPD", dictionary)
        self.nutelloco = self.total("Nutelloco- Coconut Bowl","Nutelloco- Coconut Bowl TPD", dictionary)
        self.coco_power = self.total("Coco Power- Coconut Bowl","Coco Power- Coconut Bowl TPD", dictionary)
        self.custom_coco = self.total("Custom Coconut Bowl- Includes Granola","Custom Coconut Bowl- Includes Granola TPD", dictionary)
        self.coco_bowls = self.coco_power+self.coco_bowl+self.coco_craze+self.coco_berry+self.nutelloco+self.custom_coco

        self.tide = self.total("Tide- Banana Bowl","Tide- Banana Bowl TPD", dictionary)
        self.nica = self.total("Nica- Banana Bowl","Nica- Banana Bowl TPD", dictionary)
        self.olas = self.total("Olas- Banana Bowl","Olas- Banana Bowl TPD", dictionary)
        self.costa = self.total("Costa- Banana Bowl","Costa- Banana Bowl TPD", dictionary)
        self.custom_banana = self.total("Custom Banana Bowl- Includes Granola","Custom Banana Bowl- Includes Granola TPD", dictionary)
        self.banana_bowls = self.tide+self.olas+self.nica+self.costa+self.custom_banana

        self.stupid_cupid = self.total("Stupid Cupid- Special Bowl","Stupid Cupid- Special Bowl TPD", dictionary)
        self.custom_stupid_cupid = self.total("Custom Stupid Cupid Bowl- Includes Granola","Custom Stupid Cupid Bowl- Includes Granola TPD", dictionary)
        self.booster = self.total("Booster Bowl- Special Bowl","Booster Bowl- Special Bowl TPD", dictionary)
        self.custom_booster = self.total("Custom Booster Bowl- Includes Granola","Custom Booster Bowl- Includes Granola TPD", dictionary)
        self.special_bowls = self.stupid_cupid + self.booster + self.custom_stupid_cupid + self.custom_booster



        self.bowl_dictionary = {
        "Acai Bowls":{
            "8th Ave":self.ave,
            "Pura Vida":self.pura_vida,
            "Nutella":self.nutella,
            "Tropical":self.tropical,
            "Power":self.power,
            "Custom Acai":self.custom_acai,
            "Total Acai Bowls":self.acai_bowls
        },
        "Pitaya Bowls":{
            "Pink Flamingo":self.pink_flamingo,
            "Dragonberry":self.dragonberry,
            "Electric Mermaid":self.electric_mermaid,
            "Nutaya":self.nutaya,
            "Goji":self.goji,
            "Pink Power":self.pink_power,
            "Custom Pitaya":self.custom_pitaya,
            "Total Pitaya Bowls":self.pitaya_bowls
        },
        "Chia Bowls":{
            "The Jetty":self.the_jetty,
            "Almond Joy":self.almond_joy,
            "Trailblazer":self.trailblazer,
            "Chia Tella":self.chiatella,
            "Oh Mega":self.oh_mega,
            "Custom Chia":self.custom_chia,
            "Total Chia Bowls":self.chia_bowls
        },
        "Green Bowls":{
            "Ocean":self.ocean,
            "Lola":self.lola,
            "Pacific":self.pacific,
            "Hemp":self.hemp,
            "Green Power":self.green_power,
            "Custom Green":self.custom_green,
            "Total Green Bowls":self.green_bowls
        },
        "Coconut Bowls":{
            "Coco Bowl":self.coco_bowl,
            "Coco Berry":self.coco_berry,
            "Coco Craze":self.coco_craze,
            "Nutelloco":self.nutelloco,
            "Coco Power":self.coco_power,
            "Custom Coconut":self.custom_coco,
            "Total Coconut Bowls":self.coco_bowls
        },
        "Banana Bowls":{
            "Tide":self.tide,
            "Nica":self.nica,
            "Olas":self.olas,
            "Costa":self.costa,
            "Custom Banana Bowls":self.custom_banana,
            "Total Banana Bowls":self.banana_bowls
        },
        "Special Bowls":{
            "Stupid Cupid":self.stupid_cupid + self.custom_stupid_cupid,
            "Booster":self.booster + self.custom_booster ,
            "Total Special Bowls":self.special_bowls
        }
        }

class Mods(Inventory):
    def __init__(self, dict,dictionary):
        super().__init__(dictionary)

        self.add_strawberry = self.total2("Add Strawberry",dict)
        self.sub_strawberry = self.total2("Sub Strawberry",dict)
        self.remove_strawberry = self.total2("Remove Strawberry",dict)

        self.add_blueberry = self.total2("Add Blueberry", dict)
        self.sub_blueberry = self.total2("Sub Blueberry", dict)
        self.remove_blueberry = self.total2("Remove Blueberry", dict)

        self.add_pineapple = self.total2("Add Pineapple", dict)
        self.sub_pineapple = self.total2("Sub Pineapple", dict)
        self.remove_pineapple = self.total2("Remove Pineapple", dict)

        self.add_mango = self.total2("Add Mango", dict)
        self.sub_mango = self.total2("Sub Mango", dict)
        self.remove_mango = self.total2("Remove Mango", dict)

        self.add_banana = self.total2("Add Banana", dict)
        self.sub_banana = self.total2("Sub Banana", dict)
        self.remove_banana = self.total2("Remove Banana", dict)

        self.add_kiwi = self.total2("Add Kiwi", dict)
        self.sub_kiwi = self.total2("Sub Kiwi", dict)
        self.remove_kiwi = self.total2("Remove Kiwi", dict)

        self.add_nutella = self.total2("Add Nutella", dict)
        self.sub_nutella = self.total2("Sub Nutella", dict)
        self.remove_nutella = self.total2("Remove Nutella", dict)

        self.add_peanutbutter = self.total2("Add Peanut Butter", dict)
        self.sub_peanutbutter = self.total2("Sub Peanut Butter", dict)
        self.remove_peanutbutter = self.total2("Remove Peanut Butter", dict)

        self.add_honey = self.total2("Add Honey", dict)
        self.sub_honey = self.total2("Sub Honey", dict)
        self.remove_honey = self.total2("Remove Honey", dict)

        self.add_granola = self.total2("Add Granola", dict)
        self.sub_granola = self.total2("Sub Granola", dict)
        self.remove_granola = self.total2("Remove Granola", dict)

        self.add_coco_flakes = self.total2("Add Coconut Flakes", dict)
        self.sub_coco_flakes = self.total2("Sub Coconut Flakes", dict)
        self.remove_coco_flakes = self.total2("Remove Coconut Flakes", dict)

        self.mods_dictionary = {
            "Strawberry Used":(self.add_strawberry + self.sub_strawberry - self.remove_strawberry)*2,
            "Blueberry Used":(self.add_blueberry + self.sub_blueberry - self.remove_blueberry)*2,
            "Pineapple Used":(self.add_pineapple + self.sub_pineapple - self.remove_pineapple)*2,
            "Mango Used":(self.add_mango + self.sub_mango - self.remove_mango)*2,
            "Banana Used":(self.add_banana + self.sub_banana - self.remove_banana)*2,
            "Kiwi Used":(self.add_kiwi + self.sub_kiwi - self.remove_kiwi)*2,
            "Nutella Used":(self.add_nutella + self.sub_nutella - self.remove_nutella)*2,
            "Peanut Butter Used":(self.add_peanutbutter + self.sub_peanutbutter - self.remove_peanutbutter)*2,
            "Honey Used":(self.add_honey + self.sub_honey - self.remove_honey)*2,
            "Granola Used":(self.add_granola + self.sub_granola - self.remove_granola)*2
        }

        self.inventory_used = {
            "Strawberry Used":(self.pura_vida+self.nutella+self.add_strawberry+self.sub_strawberry-self.remove_strawberry+self.dragonberry+self.the_jetty+self.chiatella+self.pacific+self.coco_berry+self.nutelloco+self.nica)*2,
            "Blueberry Used": (self.pura_vida+self.add_blueberry+self.sub_blueberry-self.remove_blueberry+self.dragonberry+self.nutaya+self.the_jetty+self.almond_joy+self.hemp+self.coco_berry+self.olas)*2.5,
            "Pineapple Used": (self.tropical+self.add_pineapple+self.sub_pineapple-self.remove_pineapple+self.goji+self.electric_mermaid+self.lola+self.coco_craze+self.tide)*2,
            "Mango Used": (self.electric_mermaid+self.coco_craze+self.lola+self.tide+self.add_mango+self.sub_mango-self.remove_mango)*2,
            "Banana Used": (self.nutella+self.tropical+self.add_banana+self.sub_banana-self.remove_banana+self.nutaya+self.chiatella+self.oh_mega+self.goji+self.hemp+self.pacific+self.coco_craze+self.nutelloco+self.nica+self.olas+((self.costa+self.coco_power+self.coco_bowl+self.power+self.ave+self.pink_flamingo+self.pink_power+self.trailblazer+self.ocean+self.green_power)*2))/2,
            "Kiwi Used": (self.electric_mermaid+self.tide+self.add_kiwi+self.sub_kiwi-self.remove_kiwi)/2,
            "Nutella Used": (self.nutella+self.add_nutella+self.sub_nutella-self.remove_nutella+self.nutaya+self.chiatella+self.nutelloco+self.costa)*2,
            "Peanut Butter Used": (self.nica+self.power+self.add_peanutbutter+self.sub_peanutbutter-self.remove_peanutbutter+self.trailblazer)*2,
            "Honey Used": (self.tide+self.coco_craze+self.coco_bowl+self.coco_berry+self.pura_vida+self.tropical+self.add_honey+self.sub_honey-self.remove_honey+self.almond_joy+self.the_jetty+self.electric_mermaid+self.dragonberry+self.goji+self.pink_flamingo+self.lola+self.pacific+self.ocean),
            "Granola Used": ((self.bowl_dictionary["Acai Bowls"]["Total Acai Bowls"] + self.bowl_dictionary["Pitaya Bowls"]["Total Pitaya Bowls"] + self.bowl_dictionary["Chia Bowls"]["Total Chia Bowls"] + self.bowl_dictionary["Green Bowls"]["Total Green Bowls"] + self.bowl_dictionary["Coconut Bowls"]["Total Coconut Bowls"] + self.bowl_dictionary["Banana Bowls"]["Total Banana Bowls"] + self.bowl_dictionary["Special Bowls"]["Total Special Bowls"] - self.remove_granola)*3) + ((self.add_granola +self.sub_granola)*2),
            "Coconut Flakes Used":(self.nutella+self.chiatella+self.goji+self.nutaya+self.electric_mermaid+self.tropical+self.lola+self.add_coco_flakes+self.sub_coco_flakes-self.remove_coco_flakes+self.nutelloco+self.coco_craze+self.coco_power)*1.2,
        }

