﻿from shutil import move


image bg_outdoor:
    "images/bg_outdoor.png"
    size (1920, 1080)

image ki smile:
    "images/ki smile.png"
    size (700,900)

image system:
    "images/system.png"
    size (700,900)

show character 

label start:
   
    # Scene setup
    scene bg_outdoor

    
    # Play background music
    play music "audio/Tears Fall Silent.mp3" loop

    # Character setup
    define ki_akira = Character("Ki Akira", color="#999999")
    define system = Character("System", color="#00FFFF") # Define the system character with a distinct color
 

  
    "In the silence, suddenly, a cold prompt echoes deep within consciousness."

    $ system_voice = Character("System", color="#A9A9A9")
    $ you = Character("You", color="#FFFFFF")
    $ ki_akira = Character("Ki Akira", color="#FF4500")
    show system
   
    system_voice "Host, please be aware. Human vows are often fragile, unable to withstand the pressures of reality. Your plan is deviating."
    system_voice "Although the host typically wouldn't return here, the changes in the current environment have triggered an emergency response, forcing the system to bring you back into mission status."
    
    "The system's voice continues to resonate in the mind, as if scrutinizing every decision, devoid of any emotion."
    
    system_voice "The target, Ki Akira, is secretly attempting a forbidden soul-consciousness link with a rebel's corpse. According to the system's preset logic, any act of disobedience will be met with severe punishment."
    system_voice "The host now faces a choice: immediately terminate Ki Akira's actions or allow them to continue, risking the triggering of a system alarm. The mission's completion will be significantly impacted."
    hide system
    show ki smile at left with move
    "Ki Akira's eyes remain downcast, yet a turbulent undercurrent of emotion can be felt within him. The system's prompt mercilessly continues to guide each choice, as if forcing a decision."
      # Show Ki Akira's image in the top-left corner with a smaller size
 
    hide ki smile at left with move
    you "System, tell me, how did you find him? And how did you capture him at the critical moment?"
    show system
    system_voice "Host, here is the sequence of events: As per your command, the system activated the all-dimensional perception network, clearing the dust that covered the Forbidden Grounds, exposing the sealed body within the perception range. "
    system_voice "Then, the system activated the spatial distortion device, adjusting all perception nodes to their optimal positions, avoiding energy interference and the invasion of foul odors. Every perception point operated perfectly, ensuring any anomaly would be instantly captured."
   
    system_voice "Time passed until the sun's rays became as intense as fire, and the aura in the environment began to stir. At that moment, the system detected a powerful whirlwind suddenly rising from the depths of the earth, sand and dust shrouding the sky, forming a brief spiritual storm."
    system_voice "This storm not only tore through the surface vegetation but also disturbed the surrounding energy field."
    system_voice "The system automatically adjusted the perception frequency, maintaining the lock on the target."

    system_voice "When the storm subsided, the system recaptured the target's movements. At that time, the target was in the Forbidden Grounds. Upon discovering the exposed body, the target displayed intense emotional fluctuations."

    system_voice "Next, the system monitored him picking up a handful of spiritual sand, using an ancient bronze urn to perform three spiritual offerings. This ritual activated the forbidden power within the corpse, attempting to summon the lost soul consciousness."
    system_voice "At the moment he completed this forbidden act, the system triggered a spatial locking array, instantly halting his actions."
    hide system
    show ki smile at left with move
    "The system's voice echoes through the air, seemingly intertwined with the energy of the Forbidden Grounds, cold and merciless, yet carrying the oppressive force of an ancient power."

    you "Tell me—keep it brief and to the point—are you aware of the fate that is forbidden to be buried?"

    ki_akira "I know."
    
    
    "His voice remains calm, without a trace of emotional fluctuation."

    ki_akira "Of course I know. How could I not? It is a declaration from heaven and earth."

    you "Oh? Such boldness, daring to speak arrogantly and defy the gods?"

    ki_akira "I will not violate the Heavenly Dao out of mere mortal anger. Under the watchful eyes of the countless stars, I must be true to my conscience. "
    ki_akira "My fate has long been sealed—death is the ultimate destination for all living beings—even if you had not cast that curse. To be freed early from this endless cosmic catastrophe would be a blessing to me. For someone like me, who has struggled and drifted in the river of destiny, death is merely a peaceful end."

    "You coldly stare at Ki Akira, your voice carrying an icy chill, your eyes glinting with a mysterious light."

    you "You should know that an overly strong will is like a branch in a storm; it seems resilient but is, in fact, fragile. A strong enough wind can easily snap it. The soft vines, however, can bend with the storm and escape unscathed. "
    you "You must also understand that once a wild beast has been chained, it has no choice but to bow its head and obey."

    ki_akira "You are absolutely right. However, if a beast refuses to wear the chains, even if trapped in a cage, it will struggle with all its might to break free. Even when imprisoned in endless darkness, it will still roar in defiance."
    ki_akira "Even if it means being shattered to pieces, it will not give up."

    "Ki Akira gazes directly at you, his tone laced with disdain and calmness."

    ki_akira "What else can you do, aside from capturing me and putting me to death? What else can you do?"

    you "I don't need to do anything else. Killing you will be enough."

    return




