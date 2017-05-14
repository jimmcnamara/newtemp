import random

def asker():
    questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
    }   
    responses={}
    attr=list(questions.keys())
    n=0
    for i in attr:
      res=str(input(questions[i]))
      if res == "yes" or res == "y" or res == "Yes":
          res=True
      else:
          res=False
      responses[attr[n]]=res
      n=n+1
    return responses

def bartender():
    ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }
    opinions=asker()
#    opinions={"strong":True,"salty":True,"bitter":True,"sweet":False,"fruity":True}
    recipe=[]
    for i in opinions:
        if opinions[i] == True:
            items=ingredients[i]
            itemtoadd=random.choice(items)
            recipe.append(itemtoadd)
    return recipe            
                


def another():
    yes=['yes','y','sure','yeah','okay']
    keepgoing=False
    while keepgoing==False:
        y_n=str(input("would you like another? "))
        y_n.lower()
        if y_n in yes:
            return True
        else:
            return False
                      
def acceptable_answers():
    yes=['yes','y','sure','yeah','okay']
    return yes

def main():
    round1=True
    while round1==True:
        order=bartender()
        adjectives=["fluffy","Salty","Panicked","Sad", "Lonely",]
        nouns=["sea-dog","water bottle","rock","salad",]
        name=(random.choice(adjectives)+" "+random.choice(nouns))
        print("you ordered: ",name)
        print("which contains",order)
        round2=another()
        if round2==False:
            round1=False
            print("that'll be... ")
            print("tip please? ")
            
if __name__== "__main__":
    main()