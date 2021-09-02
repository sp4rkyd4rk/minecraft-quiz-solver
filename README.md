# A simple minecraft chat quiz solver. 

Main principle is simple: we scroll Minecraft's _latest.log_ in real-time, search for a specific keyword in a line and then do the calculation. After the calculation's done we get our result from the terminal AND clipboard, so that we can simply paste the answer. 


## Changelogs: 

_2sep2021_: hard-coded path is now gone, it uses either ENVVAR like "%AppData%" or expands home path. 
_2sep2021_: script got a better way to scan for math expressions, uses regex, thanks, @Wirtos! 
_2sep2021_: we finally got a cross-platform way of simulating keystrokes. a bit wancky but works. gotta clean up later. 