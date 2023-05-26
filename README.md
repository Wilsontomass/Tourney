# Prisoners Dilemma Competition

Hi!

I'm running a little Competition! And there are prizes! Feel free to forward this to anyone at SEB you think would be interested.

The competition will be to write a python program that can play this prisoners dilemma game, and win against everyone elses strategies. Check out this video for context: 

https://www.youtube.com/watch?v=t9Lo2fgxWHw

We will play the game multiple times, allowing you to observe your opponents behaviour and respond to it. You will also play against many opponents, and the strategy that can accrue the most points will win!
You can downlaod this repo to write and test your strategy against the exampleStrats. When the competition time comes, I will gather everyones submissions and run them in one big competition.

How this works:
When you run code/prisonersDilemma.py, it will search through all the Python strategy files in code/exampleStrats. Then, it will simulate many rounds of the Prisoner's Dilemma with every possible pairing. (There are (n choose 2) pairings.) After all simulations are done, it will average each strategies' overall score. It will then produce a leaderboard of strategies based on their average performance, and save it to results.txt.

If you'd like to add your own strategy, all you have to do is create a new .py file in the code/exampleStrats folder that follows the same format as the example, randomStrategy. i.e, make sure your `.py` file contains a `def strategy(history, memory) -> Tuple[int, Any]:` Then, when you run code/prisonersDilemma.py, it should automatically include your strategy into the tournament!

# The competition (SEB employees only!)
You have one month (until 2023/06/26 23:59 Swedish time) to come up with a strategy that can win the tournament! The population in the tournament will
include all of the example strats, as well as everyone elses entries. The example strats aren't allowed to win, and their scores will be removed from the final leaderboard to determine a ranking. However, there is no rule against copying an existing strategy if you think it will win ;) 

This is a game not just of coming up with a good strategy, but also trying to guess what everyone else will do (so don't let anyone know your strategy!).

To enter, we will use a microsoft form. In their infinite wisdom, microsoft decided to only allow file uploads of a small subset of types, not including `.py` files.
So, before you upload your file, rename the file extension from `.py` to `.pdf`. If you cant see the `.py` at the end of the file name, make sure you have "file name extensions" ticked in the "view" tab of file explorer.
The form is here: https://forms.office.com/Pages/ResponsePage.aspx?id=4_mPmjUOIEanJOmDTcULUSj1R0W6m3lEiubaimOCgM5URUZRNzZQU083WFZPQTNJWkc0MEk4WjlONi4u

You can only compete with **one strategy per person** but if you resubmit the form, i will use your last submitted strategy in the tournament

# Prizes!

| Place | Prize |
| ------------- | ------------- |
| First  | 1 000 kr |
| Second  | 500 kr |
| Third  | 300 kr |

# Details
| Payout Chart  | Player A cooperates | Player A defects |
| ------------- | ------------- | ------------- |
| Player B cooperates  | A: +3, B: +3  | A: +5, B: +0  |
| Player B defects  | A: +0, B: +5  | A: +1, B: +1  |

In this code, 0 = 'D' = defecting, and 1 = 'C' = cooperating.

---

Strategy functions take in two parameters, 'history' and 'memory', and output two values: 'moveChoice' and 'memory'. 'history' is a 2\*n numpy array, where n is the number of turns so far. Axis one corresponds to "this player" vs "opponent player", and axis two corresponds to what turn number we're on.
For example, it might have the values
```
 [[0 0 1]       a.k.a.    D D C
  [1 1 1]]      a.k.a.    C C C
```
In this case, there have been 3 turns, we have defected twice then cooperated once, and our opponent has cooperated all three times.

'memory' is a very open-ended parameter that can takes on any information that should be retained, turn-to-turn. Strategies that don't need memory, like randomStrategy, can simply return None for this variable. If you want to keep track of being 'if the opponent defected', you can set memory to True or False. If you have an extremely complicated strategy, you have make 'memory' store a list of arbitrarily many variables!

For the outputs: the first value is just the move your strategy chooses to make, with 0 being defect and 1 being cooperate. The second value is any memory you'd like to retain into the next iteration. This can be 'None'.

The only libraries available to you are the **python standard library and numpy**.

If I have any suspicion that you're trying to break the rules in any way, by using disallowed libraries, or trying to read or write any files, or being intentionally inefficient with loops or sleep() commands, I reserve the right to disqualify you from the tournament.

---

Each pairing simulation runs for this many turns:
```
200-40*np.log(random.random())
```
This means each game is guaranteed to be at least 200 turns long. But then, for every turn after the 200th, there is an equal probability that the game ends. The probability is very low, so there should be no strategizing to defect on the very last turn consequence-free.
