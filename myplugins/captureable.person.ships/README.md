### capturable.person.ships
<br>
<br>
Makes person ships captureable.<br> 
<br>
<br>
Well, technically this plugin disables the person ships, and creates new ones which are captureable (with changed names to "<name> (disable me)", due to limitations of changing parts of the originals). Also adds all of them to the author government, adjusts some personalities and sets all frequencies to 1000. Changed "Tranquility" to have a weapon, so it doesn't flee. And changed "Zitchas" personality to "decloaked", so it doesn't flee and regenerate while cloaked.<br>
Attacking one of them makes all your enemies, they all try to disable instead of destroying, and they all have the same spawn chance which is in average within 10 minutes.<br>
<br>
At Earth's job board you can find a repeatable job that displays which persons you have already killed, which are alive, and where to find them.<br>
After you've killed them all, you receive a small unique gift.<br>
<br>
I tested this plugin with 10x KIV349, all equipped with Mereti beam weapons, was probably an overkill on most. Boarding "Zitchas"(1000 crew) needed an Echo-Galleon, and I tried it with hand2hand outfits plugin. Maybe it works with nerve gas too.<br>
In cap_persons.txt you find the following line under gamerules: "#	"person spawn period" 2000". If you remove the "#" the spawning speed is increased to one spawn in max a minute.<br>
<ul>
<li>"vyu-Ir" (not a person ship, but unique | found south-western of Gegno)</li>
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
<li>"Patrol Team" (found everywhere | 6x Waverider)</li>
<li>"Danau" (found in human space | 1x mod. Hauler IV, 2x Hauler III, 2x Hauler II, 2x Hauler)</li>
</ul>
<br>
<br>
Changelog:<br>
<br>
2025-06-05<br>
colored the job<br>
added outfit series<br>
<br>
2025-05-19<br>
typo fixes by snoogles<br>
icon@2x, plugintxt changes<br>
<br>
2025-01-27<br>
added 0.10.11 person "Danau"<br>
<br>
2024-11-11<br>
made vyu-Ir captureable (unique, but no person ship)<br>
normalized the spawn speed<br>
<br>
2024-10-08<br>
proofreading and minor text changes (Vemenous-Repentile)<br>
changed status mission to fail on daily<br>
changed subsidural (1 outfit space, keystone and 300 fuel)<br>
<br>
2024-07-14<br>
fixed tranquility weapon space error<br>
removed fines from author government<br>
<br>
2024-06-07<br>
text corrections (thx to TheGiraffe3)<br>
<br>
2024-05-28<br>
adjusted mass and drag to be like in 0.10.7<br>
removed staying personality ftom Tranquility<br>
renamed persons to "name (C)", was "name (Capture me)"<br>
<br>
2024-04-06<br>
set person killed job back to earth only, less annoying when you are done<br>
added a mission with unique reward, after killing all person ships<br>
<br>
2024-03-23<br>
set "no person spawn weight" to 0<br>
added person destroyed check job to every planet with a job board<br>
added a gun to Tranquility so that it stays for fighting<br>
changed Zitchas personality, so that it doesn't cloak<br>
<br>
2024-03-14<br>
bugfixes<br>
added person destroyed check on Earth job board<br>
<br>
2024-02-02<br>
added 0.10.5 person "Patrol Team"<br>
<br>
2023-10-17<br>
added plugin.txt<br>
<br>
2023-09-15<br>
changed gamerules back, because it caused mass spawning<br>
changed some personalities<br>
<br>
2023-09-09<br>
changed all frequencies to 1000<br>
changed gamerules to prevent no spawning chance<br>
<br>
2023-09-08<br>
initial release<br>
