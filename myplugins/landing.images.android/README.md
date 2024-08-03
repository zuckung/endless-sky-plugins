### landing.images.android 
<br>
<br>
Moves the landing image above the textbox, instead of behind the textbox (for ES mobile).<br>
<br>
In case parts if the UI/the buttons are outside the screen, try rescaling your UI in the ES options<br>
If that doesnt help, open the zip, edit 'landing.images.android/data/interface.txt' and change line 3 and 4 to:<br>
		center -60 -150<br>
		dimensions 250 135<br>
that resizes the landing image to it's half<br>
<br>
Before:<br>
<img src='https://raw.githubusercontent.com/zuckung/endless-sky-plugins/master/screenshots/landing.images.android01.jpg' width='400'>
<br>
After:<br>
<img src='https://raw.githubusercontent.com/zuckung/endless-sky-plugins/master/screenshots/landing.images.android02.jpg' width='400'>
<br>
<br>
Changelog:<br>
<br>
2024-08-03<br>
added hire all/fire all buttons which were missing (thx timeout.fu)<br>
added guide to resize the image (thx Pyrrha of simpleplanes)
<br>
2024-08-02<br>
initial release<br>

