from StardewValley import Helper
from StardewValley.Data import EventData, Eventscripts, Precondition, CharacterID
from StardewValley.Data.GameData import Direction

class TranslateDialog:
    languages={
        "default": {
            "Dialogue_1": "Hello @!$h#$b#You see this turtle here?",
            "Dialogue_2": "I found it at the entrance to your farm! I think she's lost..$s",
            "Dialogue_3": "Hey, it seems to like this place! Hey, um.... Don't you think this farm could use a good turtle?",
            "Dialogue_4": "Well,  %pet... Be a good turtle now... ok?"
        }
    }

class Turtle(EventData):
    def __init__(self, mod:Helper):
        for language in TranslateDialog.languages:
            for dialogue in TranslateDialog.languages[language]:
                mod.translation(language, dialogue, TranslateDialog.languages[language][dialogue])

        #self.language=language
        self.key=Precondition(
            ID=f"{mod.content.Manifest.UniqueID}_TurtlePetStart",
            EarnedMoney=1000,
            Time=(600, 930),
            DayOfWeek="Mon Tue Thu Sat Sun",
            Weather="sunny",
            MissingPet="Turtle",
            IsHost=True
        )
        self.value=Eventscripts(
            music="continue",
            coordinates=(64, 15),
            characterID=[
                CharacterID("farmer", 64, 15, Direction.Down),
                CharacterID("Marnie", 65, 16, Direction.Up),
                CharacterID("pet", 64, 15, Direction.Down)
            ]
        )
        
        


        self.value.skippable()
        self.value.faceDirection(actor="PetActor", direction=Direction.Right)
        self.value.pause(480)
        self.value.animate("PetActor", False, False, 120, 20,21,22,23,23)
        self.value.pause(480)
        self.value.animate("PetActor", False, True, 120, 23)
        self.value.pause(2000)
        self.value.speak("Marnie", "{{i18n: Dialogue_1}}")
        self.value.faceDirection(actor="Marnie", direction=Direction.Left)
        self.value.pause(400)
        self.value.showFrame("PetActor", 26)
        self.value.playPetSound("turtle_pet")
        self.value.pause(200)
        self.value.showFrame("PetActor", 23)
        self.value.pause(600)
        self.value.showFrame("PetActor", 26)
        self.value.playPetSound("turtle_pet")
        self.value.pause(200)
        self.value.showFrame("PetActor", 23)
        self.value.pause(1000)
        self.value.animate("PetActor", False, True, 200, 24, 25)
        self.value.playPetSound("turtle_pet")
        self.value.pause(400)
        self.value.playPetSound("turtle_pet")
        self.value.pause(400)
        self.value.playPetSound("turtle_pet")
        self.value.faceDirection(actor="Marnie", direction=Direction.Up)
        self.value.speak("Marnie", "{{i18n: Dialogue_2}}")
        self.value.pause(500)
        self.value.animate("PetActor", False, True, 400, 23, 31)
        self.value.pause(1500)
        self.value.speak("Marnie", "{{i18n: Dialogue_3}}")
        self.value.commands.append("catQuestion")
        self.value.pause(1000)
        self.value.faceDirection("Marnie", Direction.Left)
        self.value.speak("Marnie", "{{i18n: Dialogue_4}}")
        self.value.pause(500)
        self.value.commands.append("stopAnimation PetActor")
        self.value.showFrame("PetActor", 26)
        self.value.playPetSound("turtle_pet")
        self.value.pause(200)
        self.value.showFrame("PetActor", 23)
        self.value.pause(1000)
        self.value.globalFade()
        self.value.viewport(-1000, -1000)
        self.value.end()

        self.location="Farm"

