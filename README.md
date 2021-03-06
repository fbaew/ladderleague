# ladderleague
Score tracking for the ol' gnip gnop table

See it online at http://pong.gregglewis.net

Version 0.2
===========

This is a little app designed to track statistics about the various 
ping pong games played in my house. We record every game (regulation 
and casual) and tabulate statistics for each player. Eventually, we will
show how each player stacks up against each other player, as well as how 
each player ranks on the overall ladder.

Features
========
* Load historical data from a csv (we keep score in a Google doc for now)
* Calculate win/loss ratio for each player, display players in order of this value
* View individual player profiles
    * Show all sets the user has played in
    * Show the outcome of those sets
* View the details of a specific set
    * Show the score for each game in the set

Roadmap
=======
* Views for Mobile
* Online score entry
* More stats
   * Ladder rank as a time series
   * "Grudge" view, showing stats for a particular matchup
* Challenge Scheduling
   * Email integration

After an initial free-for-all seeding period, regulation games will be 
restricted to official ladder league challenge rules, those being:
  * Any player may challenge any player within 2 ladder ranks of themselves
  * A challenged player has 1 month to respond to a challenge
  * If a challenge is not accepted, the declining party will be "skipped" for the purpose of counting ladder spots until such a time as they answer a challenge.
  
  Challenges will be issued and tracked through the web page.
