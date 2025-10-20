from StardewValley.Data.SVModels import EventsModel
from turtle import Turtle
from StardewValley import Manifest, Helper, ContentPatcher, Include, EditData

import Events as Events_list
from StardewValley.Data.SVModels.Events import Events



class ModEntry(Helper):
    def __init__(self, manifest:Manifest):
        super().__init__(
            manifest=manifest, modFramework=ContentPatcher(manifest=manifest)
        )
        self.autoTranslate=True
        self.contents()
    
    def contents(self):
        self.content.registryContentData(
            Include(
                FromFile="Turtle"
            )
        )
        
        self.translation("default", "Turtle", "Turtle")
        self.translation("pt", "Turtle", "Tartaruga")

        self.content.registryContentData(
            EditData(
                LogName="Edit Display Pet",
                Target="Data/Pets",
                Fields={
                    "Turtle": {
                        "DisplayName": "{{i18n: Turtle}}"
                    }
                }
            ),
            contentFile="Turtle"
        )
        
        for i in range(0,2):
            self.content.registryContentData(
                EditData(
                    LogName="Enable Turtle", # Nome para o log do Content Patcher
                    Target="Data/Pets", # O arquivo de dados a ser modificado
                    TargetField=["Turtle", "Breeds", i],
                    Entries={
                        "CanBeChosenAtStart":True
                    }
                ),
                contentFile="Turtle"
            )

        Events(
            mod=self,
            Events_List=[
                Events_list.Turtle(self)
            ]
        )