### gegno.pirates
<br>
<br>
Adds a new faction of Gegno pirates which lets you capture Gegno ships without ruining your reputation. Also increases Gegno/Scin/Vi reputation by killing Gegno pirates.<br>
<br>
The new government "Gegno Pirates" inhabit the new System "Zaron"(between Huud, Vesvii and Cotpoxi). The surrounding systems, up to 3 jumps away, have new pirate fleets.<br>
Killing pirates and assisting Gegno/Scin/Vi gives reputation now. The needed reputation to land on the Gegno planets got changed to higher values. Killing like 80 Gegno pirates should allow you to land on all Gegno planets and use their shipyards and outfitters.<br>
Boarding Gegno Pirates gives you a 5% chance to obtain one of the 8 Gegno licenses.<br> 
<br>
Warning: As soon as new Gegno story content is added to the base game, it is highly advised to remove this plugin and/or do a new playthrough. If not, the new story missions, which are probably based on reputation, won't appear in the planned order. If you want to keep your save you have to remove this plugin and edit your savegame. To do so ... open your savegame and find the lines with the different Gegno reputations looking like the following lines and change the values to 0.	<br>
<code>	
	Gegno 5544.86
	"Gegno Pirates" -4871.9
	"Gegno Scin" 517.5
	"Gegno Scin (Neutral)" 517.5
	"Gegno Vi" 517.5
	"Gegno Vi (Duelist A)" 0
	"Gegno Vi (Duelist B)" 0
	"Gegno Vi (Neutral)" 517.5
</code>
then find the position where the licenses are saved, looking like this:<br>
<code>
licenses
	City-Ship
	Coalition
	"Gegno Civilian"
	"Gegno Driller"
	Heliarch
	...
<code>
Remove the 8 lines containing: "Gegno Civilian" "Gegno Driller"	 "Scin Adjutant" "Scin Architect 	"Scin Hoplologist" "Vi Centurion" "Vi Evocati" 	"Vi Lord". Save it and then you are ready to start the new Gegno storylines as planned.<br>
<br>
<br>
Changelog:<br>
<br>
2024-03-08<br>
adjustments and fixes<br>
added plugin removal guide to the readme<br>
added several missions<br>
added new planet with all outfits/ships for easier browsing<br>
<br>
2024-03-07<br>
adjustments and fixes<br>
added different license pngs<br>
added missing outfits and ships<br>
<br>
2024-03-05<br>
initial release<br>




