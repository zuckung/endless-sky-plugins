### additional.command.buttons <br>
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
<img src='https://raw.githubusercontent.com/zuckung/endless-sky-plugins/master/screenshots/additional.command.buttons01.jpg' width='400'>
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
Changelog:<br>
<br>
2024-06-07<br>
text corrections (thx to TheGiraffe3)<br>
<br>
2024-02-20<br>
re-added the ammo box to main buttons (latest mobile game version needed)<br>
<br>
2023-10-17<br>
added plugin.txt<br>
<br>
2023-08-24<br>
fixed non-firing attack button<br>
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
