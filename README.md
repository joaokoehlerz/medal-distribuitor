# medal-distribuitor
Python script I made ages ago as a kid to help distributing TF2 tournament medals.
It's not the best the way to distribute medals but it gets the job done. 

# Prerequisites
Before running this project, make sure the `requests` library is installed.

You can install it using pip: `pip install requests`

# Usage
Create a txt file that has all the steamids separated by newlines related to the promoID of the medal you wanna send. Put this txt file in the same folder as the script.

If you have a file named `medals.txt` with the following content:
<pre>123456789
987654321 </pre>
And you set your `promoID` to `123`, the script will send medals with promoID `123` to the SteamIDs listed in the file (`123456789` and `987654321` in this example).

Again, make sure each SteamID is on a separate line in the `medals.txt` file.
