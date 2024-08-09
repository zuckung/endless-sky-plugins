### landing.images.android 
<br>
<br>
Moves the landing image above the textbox, instead of behind the textbox (for ES mobile).<br>
<br>
In case parts of the UI/the buttons are outside the screen, try rescaling your UI in the ES options<br>
If that doesn't help, open the zip, edit 'landing.images.android/data/interface.txt' and change line 2 to 7 to:<br>
	image "land"
		center -60 -150
		dimensions 250 135
	sprite "ui/frame"
		center -60 -150
		dimensions 265 150
That resizes the landing image and the frame to their half.<br>
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
2024-08-09<br>
minor text changes (thx to TheGiraffe3)<br>
<br>
2024-08-07<br>
added a frame for the image<br>
finetuned position<br>
<br>
2024-08-03<br>
added hire all/fire all buttons which were missing (thx timeout.fu)<br>
added guide to resize the image (thx Pyrrha of simpleplanes)
<br>
2024-08-02<br>
initial release<br>

