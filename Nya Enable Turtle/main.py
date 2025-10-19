from ModEntry import ModEntry
from StardewValley import Manifest

manifest=Manifest(
    Name="Nya_Enable_Turtle",
    Author="alichan",
    Version="0.2",
    Description="Nyan Enable Turtle.",
    UniqueID="alichan.Nya_Enable_Turtle"
)
mod=ModEntry(manifest=manifest)

mod.write()
