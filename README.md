![img](https://github.com/zuckung/test/blob/main/res/icon.png)
# **my endless-sky-plugins**
I aim at developing small, modular and maximal compatible plugins that don't break vanilla lore too much. <br>
Please excuse bad english, spelling, grammar, etc... english isn't my mother tongue. Feel free to correct me.<br><br>
Speaking of that, I'm looking for someone with great english knowledge(preferable native english speaking), for correcting and rephrasing some of my more text-intense plugins(better.starts, bunrodea.missions, galactic.capital.investment and snowfeather.robotics).<br><br>
Furthermore i'd like to present <a href="https://zuckung.github.io/ES-DataParser/">https://zuckung.github.io/ES-DataParser/</a> to other plugin creators or people who seek informations inside the data folder. Basically it is a very fast way to view everything out of the data folder, especially when you don't know where to find something.<br>
<br>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fzuckung%2Fendless-sky-plugins&count_bg=%2395c20e&title_bg=%235a5a5a&icon=&icon_color=%235A5A5A&title=hits&edge_flat=false"/></a>
<a href="https://github.com/zuckung/endless-sky-plugins/blob/main/license"><img src="https://img.shields.io/github/license/zuckung/endless-sky-plugins"></a>
<a href="https://github.com/zuckung/endless-sky-plugins/commits/main"><img src="https://img.shields.io/github/last-commit/zuckung/endless-sky-plugins/main"></a>
<a href="https://github.com/zuckung/endless-sky-plugins/commits/main"><img src="https://img.shields.io/github/commit-activity/t/zuckung/endless-sky-plugins"></a>
<a href="https://github.com/zuckung/endless-sky-plugins/archive/refs/heads/main.zip"><img src="https://img.shields.io/github/repo-size/zuckung/endless-sky-plugins"></a>
<a href="https://img.shields.io/"><img src="https://img.shields.io/github/languages/code-size/zuckung/endless-sky-plugins"></a>
<a href="https://img.shields.io/"><img src="https://img.shields.io/github/languages/top/zuckung/endless-sky-plugins"></a>
<br>

## Latest News:
<table><tr><td><img width="882" height="1"><br>2023-09-09 | update: captureable.person.ships<br>
2023-09-08 | update: captureable.person.ships<br>
2023-09-07 | repo update<br>
2023-09-07 | removed the other 3 automata.destruction<br>
2023-09-07 | update: automata.destruction.0percent<br>
2023-09-04 | update: more.boarding.missions<br>
2023-09-04 | badges!<br>
2023-09-03 | update: disable.spaceport.repeatables<br>
2023-09-03 | update: better.starts<br>
2023-09-03 | news system added<br>
<img width="882" height="1"><br></td></tr></table>

## Plugin List:<br>
<table><tr valign="top"><td><img width="294" height="1"><br>
<a href="README.md#additionalcommandbuttons">additional.command.buttons</a><br>
<a href="README.md#automatadestruction0percent">automata.destruction.0percent</a><br>
<a href="README.md#automatainhumanspace">automata.in.human.space</a><br>
<a href="README.md#betterstarts">better.starts</a><br>
<a href="README.md#bunrodeamissions">bunrodea.missions</a><br>
<a href="README.md#captureablepersonships">captureable.person.ships</a><br>
<img width="294" height="1"><br></td><td><img width="294" height="1"><br>
<a href="README.md#devil-rununhidden">devil-run.unhidden</a><br>
<a href="README.md#disablepersonships">disable.person.ships</a><br>
<a href="README.md#disablespaceportrepeatables">disable.spaceport.repeatables</a><br>
<a href="README.md#freeworlds5yearslater">free.worlds.5.years.later</a><br>
<a href="README.md#galacticcapitalinvestment">galactic.capital.investment</a><br>
<a href="README.md#korefretshipyard">kor.efret.shipyard</a><br>
<img width="294" height="1"><br></td><td><img width="294" height="1"><br>
<a href="README.md#morearfectas">more.arfectas</a><br>
<a href="README.md#moreboardingmissions">more.boarding.missions</a><br>
<a href="README.md#snowfeatherrobotics">snowfeather.robotics</a><br>
<a href="README.md#toomanyasteroids">too.many.asteroids</a><br>
<a href="README.md#uniquefix">unique.fix</a><br>
<img width="294" height="1"><br></td></tr></table>





---

### additional.command.buttons

<img src="myplugins/additional.command.buttons/icon.png" height="100">

[additional.command.buttons.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/additional.command.buttons.zip) | 160.13 kb | 2023-08-24 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/additional.command.buttons/) <br>
<br>
>Made for the mobile version and adds several new buttons to the lower right corner. See the readme for details.
>(inspired by theweirednut)

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### additional command buttons <br>

<br>

Made for the mobile version and changes the interface by adding the following 10 buttons: <br> 

<ul>

<li>full stop</li>

<li>board ship</li>

<li>land on planet</li>

<li>fleet: harvest flotsam</li>

<li>fleet: hold position</li>

<li>fleet: gather around me</li>

<li>fleet: attack my target</li>

<li>fleet: toggle ammo usage</li>

<li>view player info</li>

<li>fast forward</li>

</ul>

and

<ul>

<li>adjusts the message box to not overlap</li>

<li>moved the hidden ammo box to a visible place</li>

</ul>

<br>

(inspired by theweirednut) <br>

<br>

<img src='https://github.com/zuckung/endless-sky-plugins/blob/main/myplugins/additional.command.buttons/screenshot.jpg' width='400'>

<br>

Allthough most of these commands are now implemented in other parts to the original mobile user interface or can be accessed by gestures, I personally prefer these buttons on the lower right corner.<br>

<br>

Additional there are some functions in this plugin that the original mobile ui can't do at the moment:<br>

- board button cycles through the possibilities <br>

- fleet commands can be used for single ships when selected <br>

<br>

This plugin overwrites `interface "main buttons"` and `interface "hud"`, so it isn't compatible with other plugins modifying these.<br>

<br>

<br>

Chancelog:<br>

<br>

2023-08-24<br>

fixed non-fireing attack button<br>

<br>

2023-08-05<br>

moved the hidden ammo box to a visible place<br>

<br>

2023-08-02<br>

added new icon and reworked readme<br>

<br>

2023-07-26<br>

added 3 more buttons to a total of 10<br>

added descriptions inside script to exchange buttons functions<br>

<br>

2023-07-06<br>

changed 'fire afterburner' to new 'fleet: harvest flotsam', because afterburner can easily toggled by double tapping<br>
</blockquote>
</details>
<br>


---

### automata.destruction.0percent

<img src="myplugins/automata.destruction.0percent/icon.png" height="100">

[automata.destruction.0percent.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/automata.destruction.0percent.zip) | 43.71 kb | 2023-09-07 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/automata.destruction.0percent/) <br>
<br>
>Modifies the self destruction chance of Sestor and Mereti ships to a value of 0.0 (0%). See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### automata destruction 0percent

<br>

<br>

Modifies the self destruction chance of Sestor and Mereti ships to a value of 0.0 (0%).<br>

<br>

Sestor 349/109/78/71/53/40/27 and Mereti 512/256/128/64/32/16/8 ships have a self destruction value of 0.0 (0%) now.<br>

You can easily change the values in automata.txt for each ship ('"self destruct" .0') to a value of your choice. I.e. 0.12 is 23%, 0.3 is 51%, 0.5 is 75%. Its calculated twice, first the chance for self destruction on boarding(i.e. 0.3) is 30%, then of the remaining 70% again 30% chance for self destruction on capturing. That makes 30% + 21% = 51% overall chance for self destruction on a capturing try.<br>

<br>

<br>

2023-09-07<br>

changed icon<br>

changed about.txt<br>

changed readme<br>

















</blockquote>
</details>
<br>


---

### automata.in.human.space

<img src="myplugins/automata.in.human.space/icon.png" height="100">

[automata.in.human.space.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/automata.in.human.space.zip) | 35.39 kb | 2023-09-01 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/automata.in.human.space/) <br>
<br>
>Brings jump drive equipped automata into human space after the wanderer campaign. See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### automata in human space

<br>

<br>

Brings jump drive equipped automata into human space after the wanderer campaign. <br>

<br>

You can find them where Korath ships in human space are usually found(ember waste and eastern syndicate). <br>

The chance to encounter previous Korath ships or automata is like 50/50. <br>

<br>

<br>

2023-09-01<br>

added more fleet variants <br>

reworked readme <br>

changed icon.png<br>

</blockquote>
</details>
<br>


---

### better.starts

<img src="myplugins/better.starts/icon.png" height="100">

[better.starts.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/better.starts.zip) | 20.49 kb | 2023-09-03 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/better.starts/) <br>
<br>
>Adds several new start options with different ships, background storys, credits and debts. See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### better.starts <br>

<br>

Adds 8 new start options with different ships, background storys, credits and debts.<br>

<br>

<ul>

<li>Start: Cheater | Leviathan: 100m credits, full visible human space, Jump Drive, in Sol system, no story</li>

<li>Start: Salvager | Shuttle: equipped for boarding, in Aldhibain system</li>

<li>Start: Salvager(big) | Argosy: equipped for boarding, in Aldhibain system</li>

<li>Start: Miner | Clipper: equipped for mining, in Rasalhague system</li>

<li>Start: Trader | Freighter: equipped for cargo transport, in Merak system</li>

<li>Start: Trader (Hai) | Aphid: equipped for cargo transport, in Fah Soom system(Hai space)</li>

<li>Start: Explorer to Remnant | Heavy Shuttle: equipped for exploring the Remnant, in Tania Australis system</li>

<li>Start: Explorer to Automata | Bounder: equipped for exploring the Kor Automata, in Mirfak system(Hai space)</li>

</ul>

<br>

Beside the cheater start option, all others are balanced and lore friendly. A bigger ship means a bigger bank loan. All starts come with 200.000 credits cash and a bank loan between 600.000 and 4,5 million credits. The ships outfits are changed to fit the role.<br>

<br>

<br>

2023-09-03<br>

changed miner start to a system with outfitter<br>

added Start Trader Freighter<br>

added Start Trader (Hai) Aphid<br>

added Start Explorer to Remnant<br>

added Start Explorer to Automata<br>

</blockquote>
</details>
<br>


---

### bunrodea.missions

<img src="myplugins/bunrodea.missions/icon.png" height="100">

[bunrodea.missions.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/bunrodea.missions.zip) | 47.82 kb | 2023-09-02 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/bunrodea.missions/) <br>
<br>
>This plugin adds some missions to destroy Korath ships, which enable job board missions for raising the Bunrodea reputation. The first mission is available after the vanilla first contact mission. Doing more jobs will allow you to get access to all their planets and ships. See the readme for details.
<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### bunrodea.missions

<br>

<br>

This plugin adds some missions to destroy Korath ships, which enable job board missions for raising the Bunrodea reputation. The first mission is available after the vanilla first contact mission. Doing more jobs will allow you to get access to all their planets and ships.<br>

<br>

Unlocking the planet with all ships needs 100 reputation. Unlocking the last of the planets needs 500 reputation.<br>

<br>

10 rep for vanilla first contact mission<br>

20 rep for the first mission which unlocks repeatable jobs.<br>

5-7 rep for repeatable transport jobs<br>

10 rep for Korath ship killing job<br>

At 100 rep the second mission starts, which gives 30 rep and unlocks the second repeatable job which gives 30 rep.<br>

<br>

As a little bonus, the three eastern uninhabited systems spawn jumpdrive equipped "Lor'kas Ik 577" or "Ra'gru Ik 618" or "Ra'at Ik 621".<br>

<br>

<br>

2023-09-02<br>

changed fleet missions/jobs to include only Palavret and Rano'erek<br>

added korath fleets to Era Natta, Genta Bo and Eneva Katta<br>

added 6 transport/passenger jobs<br>

<br>

2023-09-01<br>

added a 2nd mission and a 2nd repeatable job<br>

<br>

2023-08-26<br>

intial release<br>



</blockquote>
</details>
<br>


---

### captureable.person.ships

<img src="myplugins/captureable.person.ships/icon.png" height="100">

[captureable.person.ships.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/captureable.person.ships.zip) | 170.95 kb | 2023-09-09 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/captureable.person.ships/) <br>
<br>
>Makes person ships capturable. See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### capturable.person.ships

<br>

<br>

Makes person ships captureable.<br> 

<br>

<br>

Well, technically this plugin disables the person ships, and creates new ones(with a space more in its names) which are captureable(due to the limitations of changing parts of originals). Also adds all of them to the author government, adjusts some personalities, sets all frequencies to 1000 and changes the game rules to prevent that no ship spawns.<br>

So attacking one of them makes all your enemies.<br>

The average spawn time is 10 minutes.<br>

<br>

Tested this plugin with 10x KIV349 and 10x Model512, all equipped with Mereti beam weapons, was probably an overkill on most. Except for "Zitchas" which needed less dmg weapons and max flamethrowers to prevent its cloaking. Also boarding "Zitchas"(1000 crew) needed an Echo-Galleon, and i tried it with hand2hand outfits plugin. Maybe it works with nerve gas too. Another problem is "Tranquility" which has no weapons and therefore avoids fight. Tested different personality settings and best choice was to let it stay in system after spawn(yellow dot on radar).<br>

<br>

<img src='https://github.com/zuckung/endless-sky-plugins/blob/main/myplugins/captureable.person.ships/screenshot.jpg' width='400'>

<ul>

<li>"Michael Zahniser" (found everywhere | Kestrel + Finch)</li>

<li>"Cap'n Pester" (found everywhere | Quarg Wardragon)</li>

<li>"Marauding Max" (found everywhere | Marauder Fury)</li>

<li>"Captain Nate" (found everywhere | Vanguard)</li>

<li>"Tranquility" (found everywhere | Lampyrid)</li>

<li>"Power of the People" (found everywhere | Modified Osprey)</li>

<li>"Local God" (found everywhere | Ursa Polaris)</li>

<li>"Subsidurial" (found in uninhabited | Subsidurial)</li>

<li>"Prototype B3-CC4" (found in Ember Waste | Shooting Star)</li>

<li>"Rais Iris XVIII" (found everywhere | Marauder Bactrian)</li>

<li>"Zitchas" (found in Ember Waste | Heron + Peregrine + 4x Petrel + 32x Tern)</li>

<li>"Brick" (found everywhere | 3x Modified Boxwing)</li>

<li>"Gefullte Taubenbrust" (found everywhere | Modified Battleship)</li>

<li>"MasterOfGrey" (found in Hai space | Modified Ladybug)</li>

</ul>

<br>

<br>

Changelog:<br>

<br>

2023-09-09<br>

changed all frequencies to 1000<br>

changed gamerules to prevent no spawning chance<br>

<br>

2023-09-08<br>

initial release<br>

</blockquote>
</details>
<br>


---

### devil-run.unhidden

<img src="myplugins/devil-run.unhidden/icon.png" height="100">

[devil-run.unhidden.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/devil-run.unhidden.zip) | 39.53 kb | 2023-08-31 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/devil-run.unhidden/) <br>
<br>
>Removes the hidden tag from system Devil-Run. It can be found near the core and opens the path to the Deep Space systems and the Devil-Hide system via wormhole. See the readme for details.
<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### devil-run.unhidden

<br>

<br>

Removes the hidden tag from system Devil-Run. It can be found near the core and opens the path to the Deep Space systems and the Devil-Hide system via wormhole.<br>

<br>

Originally this system opens during hai reveal storyline, which is disabled because of a rework. Unfortunately some Remnant jobs rely on the Deep Space systems hidden behind a wormhole in Devil-Run. This plugin makes this system visible and reachable(by jump drive) in eastern syndicate.<br>

The Devil-Hide system is also a nice system to farm Marauder Leviathans.<br>

<br>

<br>

2023-08-31<br>

added icon.png<br>
</blockquote>
</details>
<br>


---

### disable.person.ships

<img src="myplugins/disable.person.ships/icon.png" height="100">

[disable.person.ships.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/disable.person.ships.zip) | 19.75 kb | 2023-08-31 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/disable.person.ships/) <br>
<br>
>Disables all person ships. See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### disable.person.ships <br>

<br>

<br>

Disables all 14 random spawning person ships.<br>

<br>

<ul>

<li>	"Michael Zahniser" </li>

<li>	"Cap'n Pester" </li>

<li>	"Marauding Max" </li>

<li>	"Captain Nate" </li>

<li>	"Tranquility" </li>

<li>	"Power of the People" </li>

<li>	"Local God" </li>

<li>	"Subsidurial" </li>

<li>	"Prototype B3-CC4" </li>

<li>	"Rais Iris XVIII" </li>

<li>	"Zitchas" </li>

<li>	"Brick" </li>

<li>	"Gefullte Taubenbrust" </li>

<li>	"MasterOfGrey" </li>

</ul>

<br>

<br>

2013-08-31<br>

added icon.png<br>
</blockquote>
</details>
<br>


---

### disable.spaceport.repeatables

<img src="myplugins/disable.spaceport.repeatables/icon.png" height="100">

[disable.spaceport.repeatables.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/disable.spaceport.repeatables.zip) | 19.98 kb | 2023-09-03 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/disable.spaceport.repeatables/) <br>
<br>
>Disables all repeatable spaceport missions. I.e. shady passenger transport, drug smuggling, time critical transport or defend planet. See the readme for details. 

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### disable.spaceport.repeatables

<br>

<br>

Disables all spaceport repeatable missions. These missions annoy me. Removes the 8 dialog repeatables and the 8 defend planet missions.<br>

<br>

<br>

<ul>

<li> "Shady passenger transport 1" </li>

<li> "Shady passenger transport 2" </li>

<li> "Shady passenger transport 3" </li>

<li> "Drug Running 1" </li>

<li> "Drug Running 2" </li>

<li> "Drug Running 3" </li>

<li> "Courier 1" </li>

<li> "Courier 2" </li>

<li> "Southern Pirate Attack" </li>

<li> "Northern Pirate Attack" </li>

<li> "Core Pirate Attack" </li>

<li> "Pirate Occupation [0]" </li>

<li> "Pirate Occupation [1]" </li>

<li> "Pirate Occupation [2]" </li>

<li> "Raider Attack 1" </li>

<li> "Raider Attack 2" </li>

</ul>

<br>

2023-09-03<br>

added the 2 syndicate alien attack missions<br>

<br>

2023-08-31<br>

added the 3 pirate occupation missions<br>

added icon.png<br>
</blockquote>
</details>
<br>


---

### free.worlds.5.years.later

<img src="myplugins/free.worlds.5.years.later/icon.png" height="100">

[free.worlds.5.years.later.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/free.worlds.5.years.later.zip) | 30.28 kb | 2023-08-05 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/free.worlds.5.years.later/) <br>
<br>
>Lets the free world war begin 5 years later. See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### free.worlds.5.years.later <br>

<br>

Lets the free world war begin 5 years later.<br>

<br>

<ul>

<li>changes event "war begins" from 4 7 3014 to 4 7 3019</li>

<li>changes event "initial deployment 1" from 24 7 3014 to 24 7 3019</li>

<li>changes event "initial deployment 2" from 14 8 3014 to 14 8 3019</li>

<li>changes event "initial deployment 3" from 29 8 3014 to 29 8 3019</li>

<li>changes event "initial deployment 4" from 17 9 3014 to 17 9 3019</li>

</ul>

</blockquote>
</details>
<br>


---

### galactic.capital.investment

<img src="myplugins/galactic.capital.investment/icon.png" height="100">

[galactic.capital.investment.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/galactic.capital.investment.zip) | 26.63 kb | 2023-08-25 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/galactic.capital.investment/) <br>
<br>
>Implements a two mission chain that enables repeatable job board investment opportunities which result in small daily income. Available in human, quarg and hai space starting with 2 million credits cash and going up to 100 million credits. See the readme for details.
>(inspired by a-alhusaini's investment bank plugin)

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### galactic capital investment <br>

<br>

Implements a two mission chain that enables repeatable job board investment opportunities which result in small daily income. Available in human, quarg and hai space starting with 2 million credits cash and going up to 100 million credits. <br>

(inspired by a-alhusaini's investment bank plugin) <br>

<br>

There are missions for 1 million, 5 million, 10 million, 50 million and 100 million credits. The chance for the jobs to appear on the job board are 25% for each one. Unfortunately you have to take off and land again on the same planet to clear the mission marker.<br>

1 million = 600 credits daily <br>

5 million = 3.400 credits daily <br>

10 million = 7.200 credits daily <br>

50 million = 37.000 credits daily <br>

100 million = 76.100 credits daily <br>

<br>

These investments pay off after 3,5 to 4,5 years. Higher Investments pay off faster.<br>

<br>

<br>

2023-08-25<br>

added pirate planets as mission source

moved investment missions from spaceport mission to job board
</blockquote>
</details>
<br>


---

### kor.efret.shipyard

<img src="myplugins/kor.efret.shipyard/icon.png" height="100">

[kor.efret.shipyard.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/kor.efret.shipyard.zip) | 29.82 kb | 2023-09-01 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/kor.efret.shipyard/) <br>
<br>
>Adds a shipyard with the three Kor Efret ships to Laki Nemparu(Kashikt) in Kor Efret space. Also adds an outfitter with all outfits of these three ships and some Korath Exiles outfits. See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### kor.efret.shipyard

<br>

<br>

Adds a shipyard with the three Kor Efret ships to Laki Nemparu(Kashikt) in Kor Efret space. Also adds an outfitter with all outfits of these three ships and some Korath Exiles outfits. <br>

<br>

<br>

Available ships:<br>

<ul> 

<li>Arch-Carrack</li>

<li>Charm-Shallop</li>

<li>Echo-Galleon</li>

</ul>

<br>

Available outfits:<br>

<ul>

<li>Digger Mining Beam</li>

<li>Banisher Grav-Turret</li>

<li>Warder Anti-Missile</li>

<li>Grab-Strike Turret</li>

<li>Fuel Processor</li>

<li>Small Heat Shunt</li>

<li>Large Heat Shunt</li>

<li>Liquid Sodium Cooler</li>

<li>Scram Drive</li>

<li>System Core (Large)</li>

<li>System Core (Medium)</li>

<li>System Core (Small)</li>

<li>Plasma Core</li>

<li>Double Plasma Core</li>

<li>Triple Plasma Core</li>

<li>Afterburner (Asteroid Class)</li>

<li>Afterburner (Comet Class)</li>

<li>Afterburner (Lunar Class)</li>

<li>Afterburner (Planetary Class)</li>

<li>Afterburner (Stellar Class)</li>

<li>Generator (Furnace Class)</li>

<li>Generator (Candle Class)</li>

<li>Generator (Inferno Class)</li>

<li>Farves GP Hybrid Thruster</li>

<li>Gaktem GP Hybrid Steering</li>

<li>Gaktem GP Hybrid Thruster</li>

<li>Nelmeb GP Hybrid Steering</li>

<li>Nelmeb GP Hybrid Thruster</li>

<li>Engine (Meteor Class)</li>

<li>Bow Drive (Meteor Class)</li>

<li>Reverser (Asteroid Class)</li>

<li>Reverser (Comet Class)</li>

<li>Reverser (Lunar Class)</li>

<li>Reverser (Planetary Class)</li>

<li>Reverser (Stellar Class)</li>

<li>Thruster (Asteroid Class)</li>

<li>Thruster (Comet Class)</li>

<li>Thruster (Lunar Class)</li>

<li>Thruster (Planetary Class)</li>

<li>Thruster (Stellar Class)</li>

<li>Steering (Asteroid Class)</li>

<li>Steering (Comet Class)</li>

<li>Steering (Lunar Class)</li>

<li>Steering (Planetary Class)</li>

<li>Steering (Stellar Class)</li>

<li>Thermal Repeater Rifle</li>

</ul>

<br>

<br>

2023-xx-xx<br>

added 28 korath outfits(no weapons)<br>

added new icon.png<br>

reworked readme<br>
</blockquote>
</details>
<br>


---

### more.arfectas

<img src="myplugins/more.arfectas/icon.png" height="100">

[more.arfectas.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/more.arfectas.zip) | 30.04 kb | 2023-08-05 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/more.arfectas/) <br>
<br>
>Adds the new system 'Pug Zak', near 'Pug Iyek' in Wanderer space. There you can farm rare spawning Arfectas and other more common Pug ships, without ruining your Pug reputation. See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### more.arfectas <br>

<br>

Adds the new system 'Pug Zak', near 'Pug Iyek' in Wanderer space. There you can farm rare spawning Arfectas and other more common Pug ships, without ruining your Pug reputation.<br>

<br>

Added a new system, with new government "Pug Farm" and 3 new fleets. Two fleets are like the ones in 'Pug Iyek' and the third, rare spawning one, has 1 arfecta. It spawns within 15000 frames(~4 minutes).<br>

</blockquote>
</details>
<br>


---

### more.boarding.missions

<img src="myplugins/more.boarding.missions/icon.png" height="100">

[more.boarding.missions.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/more.boarding.missions.zip) | 15.17 kb | 2023-09-04 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/more.boarding.missions/) <br>
<br>
>Adds lots of repeatable boarding and assisting missions for different factions. Boarding bigger ships give higher rewards or higher chances for credits or special items. See the readme for details.
<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### more boarding missions <br>

<br>

<br>

Adds 53 repeatable boarding and assisting missions. Boarding/assisting Free Worlds, Republic, Syndicate, Militia, Merchant, Independant, Pirates, Korath, Hai, Hai Unfettered, Pug, Pug (Wanderer) and Wanderer can trigger them. Bigger ships give higher rewards.<br>

<br>

<ul>

<li> 7 Human assisting missions (by ship categories, 20% chance, 10.000 to 30.000 credits)</li>

<li> 7 Pirate boarding missions (by ship categories, 20% chance, 5.000 to 25.000 credits)</li>

<li> 4 Pirate boarding missions (by ship categories, 1-4% chance, outfit "NDR-114 Android")</li>

<li> 7 Hai assisting missions (by ship categories, 20% chance, 20.000 to 60.000 credits)</li>

<li> 5 Hai Unfettered assisting missions (by ship categories, 20% chance, 30.000 to 90.000 credits)</li>

<li> 5 Hai Unfettered boarding missions (by ship categories, 10% chance, 30.000 to 90.000 credits)</li>

<li> 3 Hai Unfettered boarding missions (by reward, 3% chance, outfit one of the 3 weapon prototypes)</li>

<li> 2 Korath boarding missions (for the bigger ship categories, 2-3% chance, outfit "Cloaking Device")</li>

<li> 3 Pug boarding missions (by ship categories, 10% chance, 100.000 to 200.000 credits)</li>

<li> 3 Pug boarding missions (by ship categories, 1-3% chance, new outfit "Pug War Staff")</li>

<li> 7 Wanderer assisting missions (by ship categories, 10% chance, 50.000 to 100.000 credits)</li>

</ul>

<br>

<br>

2023-09-04<br>

added 7 wanderer assisting missions (credits)<br>

added 3 pug boarding missions (credits)<br>

added 3 pug boarding missions (outfit)<br>

added new outfit "Pug War Staff"<br>

<br>

2023-09-01<br>

added 5 hai unfettered assisting missions (credits)<br>

added 5 hai unfettered boarding missions (credits)<br>

added 3 hai unfettered boarding missions (outfit)<br>

added "Merchant" and "Independant" to human assisting missions<br>

<br>

2023-08-29<br>

added 2 korath boarding missions (outfit)<br>

added 4 pirate boarding missions (outfit)<br>

added icon and reworked readme<br>

</blockquote>
</details>
<br>


---

### snowfeather.robotics

<img src="myplugins/snowfeather.robotics/icon.png" height="100">

[snowfeather.robotics.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/snowfeather.robotics.zip) | 21.72 kb | 2023-08-28 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/snowfeather.robotics/) <br>
<br>
>Adds three missions that lead to adding androids to the outfitter on Snowfeather(Hai space).
>Starts on Snowfeather(Bore Fah) when having at least one android installed. See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### snowfeather robotics <br>

<br>

<br>

Adds three missions that lead to adding androids to the outfitter on Snowfeather(Hai space). <br>

Starts on Snowfeather(Bore Fah) when having at least one android installed. <br>

<br>

To get an android, which is needed to start this plugin, do the remnant mission 'shattered light 4'. Alternatively my plugin 'more.boarding.missions' give androids as rare reward for boarding pirates.<br>

The new buyable androids are a little bit more expensive than the original ones.<br>

<br>

<br>

2023-08-29<br>

removed remnant mission requirement<br>
</blockquote>
</details>
<br>


---

### too.many.asteroids

<img src="myplugins/too.many.asteroids/icon.png" height="100">

[too.many.asteroids.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/too.many.asteroids.zip) | 17.97 kb | 2023-09-01 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/too.many.asteroids/) <br>
<br>
>Removes all non-mineable asteroids from all systems. Mineable asteroids and asteroid belts are untouched.
>Increases game performance. See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### too many asteroids <br>

<br>

<br>

Removes all non-mineable asteroids from all systems. Mineable asteroids and asteroid belts are untouched. <br>

Increases game performance.<br>

<br>

<br>

Every of the 552 base game systems(0.10.2) is edited via remove command for full compatibility with other system altering plugins. A total of 2654 asteroid entries got removed.<br>

In case i won't update this plugin to the newest game version, a python script for generating an updated plugin can be found <a href="https://github.com/zuckung/endless-sky-plugins/tree/main/tools/too_many_asteroids_plugin_script">here</a>.<br>

<br>

<br>

2023-09-01<br>

added new icon.png<br>

reworked readme<br>

removed py script<br>

<br>

2023-06-17<br>

updated to 0.10.1<br>

added a python script which generates the asteroids.txt(in case I don't update this mod, everyone can do it in no time.)<br>
</blockquote>
</details>
<br>


---

### unique.fix

<img src="myplugins/unique.fix/icon.png" height="100">

[unique.fix.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/unique.fix.zip) | 202.8 kb | 2023-08-31 | [view files](https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/unique.fix/) <br>
<br>
>Removes mass and outfit space from some uniques, puts others into unique category, or gives a png if there isn't one. See the readme for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### unique fix

<br>

<br>

Removes mass and outfit space from some uniques, puts others into unique category, or gives a png if there isn't one. See the readme for details.<br>

<br>

<br>

<ul>

<li> Removes mass and outfit space from the cloaking device. </li>

<li> Removes mass and outfit space from outskirts gauger and puts it in unique category. </li>

<li> Gives outfit '"Puny"' a portrait. </li>

<li> Puts outfit 'Mug' into unique category and gives it a portrait </li>

</ul>

<img src='https://github.com/zuckung/endless-sky-plugins/blob/main/myplugins/unique.fix/screenshot.png' width='400'>

<br>

<br>

2023-8-31<br>

added 'Mug' to unique category and added a portrait<br>

changed puny portrait<br>

changed icon.png<br>
</blockquote>
</details>
<br>
