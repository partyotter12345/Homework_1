#Amaan Razi HMWK #1
#myMadlib.py

#Story is derived from a MadLibs titled "a letter from George"


print("There will be 18 different input questions, once all are answered your MadLibs will be ready!") 
storyFormat ='''                                        
Hello, my fellow {plural noun} in 2022, it's me, George Washington, the first
{occupation}. I am writing from {place}, where I have been secretly living
for the past {number} years. I am concerned by the {adjective} state of affairs
in America these days. It seems that your politicians are more concerned with
{verb ending in -ing} with one another than with listening to the {plural noun (another)}
of the people. When we declared our independence from {country or place},
we set forth on a/an {adjective (another)} path guided by the voices of the
everyday {one more plural noun}. If we're going to keep {another verb ending in -ing},
then we need to learn how to respect all {another plural noun}. Don't get me wrong; we had
{another adjective} problems in my day, too. Benjamin Franklin once called me a/an
{derogatory slur but not too bad of one} and kicked me in the {body part}. But at the end of the day, we
were able to {one more verb} in harmony. Let us find that {one last adjective} spirit once
again, or else I'm taking my {one more body part} off the quarter!
'''                                                 
def tellStory():                                        
    userPicks = dict()                                  
    addPick('plural noun', userPicks)                        
    addPick('occupation', userPicks)                          
    addPick('place', userPicks)
    addPick('number', userPicks)
    addPick('adjective', userPicks)
    addPick('verb ending in -ing', userPicks)
    addPick('plural noun (another)', userPicks)
    addPick('country or place', userPicks)
    addPick('adjective (another)', userPicks)
    addPick('one more plural noun', userPicks)
    addPick('another verb ending in -ing', userPicks)
    addPick('another plural noun', userPicks)
    addPick('another adjective', userPicks)
    addPick('derogatory slur but not too bad of one', userPicks)
    addPick('body part', userPicks)
    addPick('one more verb', userPicks)
    addPick('one last adjective', userPicks)
    addPick('one more body part', userPicks)
    
    
    story = storyFormat.format(**userPicks)             
    print(story)                                        
                                                    
def addPick(cue, dictionary):                           
    '''Prompt for a user response using the cue string, 
    and place the cue-response pair in the dictionary.  
    '''                                                 
    prompt = 'Enter an example for a/an ' + cue + ': '       
    response = input(prompt)                            
    dictionary[cue] = response                          

                                                       
tellStory()                                             
input('Press Enter to end the program.')      
