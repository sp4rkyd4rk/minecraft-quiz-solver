# A simple minecraft chat quiz solver. 

Main principle is simple: we scroll Minecraft's _latest.log_ in real-time, search for a specific keyword in a line and then do the calculation. After the calculation's done we get our result from the terminal AND clipboard, so that we can simply paste the answer. 

## to-do: 
- get rid of hard-coded path
- optimize crashing upon completing
- make it reusable