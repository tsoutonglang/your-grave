# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character('The Riddler', color="#037e37")
image bg grave = "graveyard.jpg"
image riddler = "riddler.png"

# The game starts here.

label start:
    scene bg grave
    
    "You wake up strapped to a chair at the bottom of a grave. Your arms are tied behind your back,
    and your feet are tied to the chair."
    "You look up and see The Riddler standing over you with a shovel in his hand."
    
    show riddler
    
    r "You have to play my game to live. The lives of 5 people are in your hands. It's game over once you get a riddle wrong or you're too slow!"
    r "Get all three right then everyone lives! Get the first two right, you and one other person dies.
    If you answer the second one wrong, you and three people die!"
    r "Everyone dies if you're wrong from the start! You have 3 seconds to answer each question."
    
    "He stabbed the shovel into the ground and rubbed his hands together."

    r "Let's begin."

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown():
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

# var
init:
    $ timer_range = 0
    $ timer_jump = 0

label first:
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'too_slow'
    $ hostages = 5
    
    r "What can you catch but can not throw?"

    show screen countdown

    menu:
        "A tennis ball.":
            hide screen countdown
            jump wrong
        "A cold.":
            hide screen countdown
            jump second
        "Your toys.":
            hide screen countdown
            jump wrong
        "A boomerang.":
            hide screen countdown
            jump wrong

label second:
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'too_slow'
    $ hostages = 3

    r "Good job! Now let's make sure you can still keep up."
    r "I can be broken without being touched or even being seen. What am I?"

    show screen countdown

    menu:
        "Glass.":
            hide screen countdown
            jump wrong
        "Tension.":
            hide screen countdown
            jump wrong
        "A promise.":
            hide screen countdown
            jump third
        "Ice.":
            hide screen countdown
            jump wrong

label third:
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'too_slow'
    $ hostages = 1

    r "I'm surprised you made it this far. Lets see if you have any braincells left."
    r "The person who made it doesn't want it, the person who paid for it doesn't need it,
    and the person who needs it doesn't know it. What is it?"
    
    show screen countdown

    menu:
        "A gift.":
            hide screen countdown
            jump wrong
        "A car.":
            hide screen countdown
            jump wrong
        "A meal.":
            hide screen countdown
            jump wrong
        "A coffin.":
            hide screen countdown
            jump correct

label too_slow:
    r "Aww you thought too long. Time to die."

    hide riddler
    scene black

    "{b}Hostages killed: [hostages]{/b}"

    return

label wrong:
    r "You little idiot."

    "He takes the shovel and begins to bury you with dirt."

    r "I hope your guilty conscience can live with killing people... Oh wait,"
    r "You're dead too!"

    hide riddler
    scene black

    "{b}Hostages killed: [hostages]{/b}"

    return

label correct:
    r "Congratulations, you got all my questions correct."
    r "As promised, you and the hostages will live another day."

    hide riddler

    "The Riddler walks away from the grave, leaving you tied to the chair six feet below."

    return