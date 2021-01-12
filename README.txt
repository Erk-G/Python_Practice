This is where I am going to store some Python practice for new things that I learn.
StripRegex.py-
This is my practice using Regex, which is creating a strip() function manually. It works with the exception of "\".

steganography.py-
For a final project in a Computer Science course the class chose what to work on, and I chose to make a steganography program. Takes an PNG and a txt, encodes the message within a copy of a PNG and saves it. The program can also read PNGs that were encoded with the same method. One major bug is some PNGs look messed up when encoded, and I think that has to do with how a PNG has transperencies like how a PNG of a character isn't surrounded by white or black color. I never accounted for that when I made this.

Dictionary_Creation_ff14-
This is a small thing I made in order to set up an easy way to find and track my quest progress in Final Fantasy 14. I determined the easiest way was to make a dicitonary in javascript where the keys are the quest names and it returns an array filled with information that I would want, quest number, quest name, how far I am until next dungeon or trial, and if I am on a dungeon or trial quest. 
Ex:"closetohome":["Close to Home (Gridania)","1","23","N"],
"tothebannock":["To the Bannock","2","22","N"],
I would add the small stuff like "let dict={" later since it is not a huge hassle.
The txts are from the source at ffxiv.consolegameswiki.com. I tried to be cool with how I extracted the tables, but the method I used would work on all websites I tested except for that one. Luckily there is a way to view the source of the table and download the txt, though the information isn't presented consistently. For example the only Trials I wanted to keep track of are the ones in the main quest. The source labels them "Main Quest" at first but changes it to "Main Scenario Quest" later. Also, the Trials were presented out of chronological order, which I fixed manually since it was only one thing out of order, but there still might be other problems I missed.
It has some redundent code and there might be a better way to keep track of strings than writing them into new txt files, but it works as intended and I have a better understanding of regular expressions.
