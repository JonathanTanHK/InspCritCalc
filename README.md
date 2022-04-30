# InspCritCalc
calculating the effect of sp crit on inspiration uptime

Inspiration duration is 15s upon a healing spell landing and critting

For the purposes of Patchwerk in Naxx wow classic, priests are effectively spamming Greater Heal which can be specced down to a 2.5s cast time

As such, we can effectively use a markov chain to simulate the uptime of Inspiration on the tank being targetted with 7 states representing the different durations remaining
