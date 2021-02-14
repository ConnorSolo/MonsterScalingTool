# MonsterScalingTool
Scale a monster's stats to fit any CR while keeping the overall feel the same! For DnD 5E only.

Sometimes when coming up with encounters for Dungeons and Dragons 5th edition, you might come across a monster that looks really fun and interesting but realize that it is way too weak or strong for your party. Maybe you just want to adjust it a bit to be a more appropriate challenge? Or, maybe you want to run a published adventure for 5th level players but you just reached 10th level with your buddies? Or, maybe you just want to give the BBEG a bit of a buff to make the fight really memorable.

It was with those question in mind that I made the [Monster Scaling Tool for DnD 5e](https://drive.google.com/file/d/1N2xVWmhLIpdgbgI-csafY56uD2tjUDmn/view?usp=sharing). This was largely inspired by u/LockeAndKeyes on reddit who created the java based Monster Calculator in 2019. I created this version using python partly as a programming exercise, while also trying to update the tool and make it slightly easier to use. And so that nobody thinks I'm trying to hack their system with a mystery .exe file, here is a github link for the python [source code](https://github.com/ConnorSolo/MonsterScalingTool).

On page 274 of the DMG is a table that lists the typical values of the following stats for a monster of any given Challenge Rating (CR).

Proficiency Bonus\
Armor Class\
Hit Points\
Attack Bonus\
Damage/Round\
Save DC

This tool works by looking at the stats entered for a certain monster and comparing them to the average values in the table for a monster of the same CR, calculating a ratio for each one. The tool then looks at the average stat values for a monster of the CR you want to scale it to and multiples them by that ratio. This has the effect of increasing or decreasing the stats to levels appropriate for the new CR in a proportionate way, keeping the general "feel" of the monster intact. If the starting monster did 50% more damage than most monsters of the same CR, it will do 50% more damage than most monsters of the target CR.

What this basically means is that after you increase or decrease their CR, glass cannon monsters will still be glassy and beefy tanks will still be beefy. However, this tool only adjusts the broadest of stats. It doesn't necessarily take into account more complex monster featues such as recharging abilities, spellcasting and spell slots, or action economy. It's a good idea to double check the results and decide how to incorporate the suggested values. 

For example, if you scale up a monster so that it is doing twice as much damage as the original version, you will need to decide whether it's best to give them twice as many attacks or to simply double the damage die for their existing attacks. In general, I would recommend the route of giving them more attacks as four low power attacks are a more stable source of damage than two high power attacks that can suddenly and abrubtly change the course of a fight. However, if the starting monster already made four attacks, you probably don't want to increase that even higher and spend ten minutes every single round rolling his new total of eight separate attacks. Perhaps consider a new damage source, like a reaction ability or even legendary actions!

Overall, the tool works best with simple monsters that don't do a lot of crazy things, but if you are willing to put in the time it can help you adjust or create a monster of just about any CR and complexity.
