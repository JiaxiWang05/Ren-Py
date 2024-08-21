# Define the characters
define s = Character("System", color="#FFFFFF")
define y = Character("You", color="#FFD700")

image bg_voids_system:
    "images/bg_voids_system.png" 
    size (1920, 1080)# Start of the game script


label start:
    # Play background music
    play music "Teardrop.mp3" 
    # Display the background scene
    scene bg_voids_system

    # Start the scene with narration
    y "(In this endless void, data streams sparkle like the Milky Way, and I, a mysterious humanoid figure, am floating in this strange space.)"
    y "(My head feels a bit dizzy, as if I’ve just been through some kind of accident, and my memory is somewhat fuzzy.)"
    y "(At this moment, the system’s cold and mechanical voice echoes through the void.)"

    # System dialogue
    s "A new mission has been generated. Target: Antigone, currently residing in Thebes, Ancient Greece. Your task is to guide her to sign a contract, become a magical girl, and create energy field fluctuations through her magical activities."

    # Show 'You' character confused
    show y confused at center with dissolve

    y "(Somewhat confused, you raise a hand to touch your forehead)"
    y "\"Uh... wait a minute, System, I think something just happened... Antigone? Energy field fluctuations? Did I remember something wrong? Why am I here?\""

    # System repeats the mission details
    s "Antigone, currently residing in Thebes, Ancient Greece. She is the daughter of Oedipus, burdened with a heavy family curse. You need to guide her to sign a contract with us, become a magical girl. Through her magical actions, strong energy field fluctuations will be generated, allowing us to collect the necessary energy."

    # Show 'You' character in fox form realization
    show y fox_form at center with dissolve

    y "(Trying to clear your thoughts, your tail swaying gently, realizing you are still in fox form)"
    y "\"Oh... sign a contract, then create energy field fluctuations, right? That way, the system can collect energy... but why me for this mission? Did I remember something wrong? Why am I a fox?\""

    # System confirms the mission
    s "Your task is to ensure that Antigone signs the contract. Upon completing the mission, you will receive a points reward and can return to the real world. The current form is the optimal choice for task execution."

    # Show 'You' accepting the mission
    show y accepting at center with dissolve

    y "(Blinking in confusion, slowly accepting the reality of the mission)"
    y "\"Okay... so I turned into a fox for this mission? If I complete it, I can return to the real world? Well, I guess I’ll give it a try... I hope I can figure out what's going on.\""

    # System initiates the task
    s "Task initiation."

    # Transition to the next scene or label
    return
