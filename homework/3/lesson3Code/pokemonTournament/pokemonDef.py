import collections

Monster = collections.namedtuple('Monster', 'name index attack defense speed hitpoint variety')
#name:the name of the monster
#index: the index of the monster
#attack:value (from 0 to 100) representing attack
#defense:value (from 0 to 100) representing defense
#speed:value (from 0 to 100) representing speed
#hitpoint:a list with two values corrsponding to the hit points that a monster has. 
#variety:the type of the monster

# The following functions codify the case analysis of when one pockemon is a) Very effective b) not very effective c) has absolutely no effect against another
def superEffective(Pokemon1, Pokemon2):
    if 'Fire' in Pokemon1.variety and 'Grass'in Pokemon2.variety :return True
    elif 'Fire' in Pokemon1.variety and 'Ice'in Pokemon2.variety :return True
    elif 'Fire' in Pokemon1.variety and 'Bug'in Pokemon2.variety :return True
    elif 'Fire' in Pokemon1.variety and 'Steel'in Pokemon2.variety :return True
    elif 'Grass' in Pokemon1.variety and 'Water' in Pokemon2.variety :return True
    elif 'Grass' in Pokemon1.variety and 'Ground' in Pokemon2.variety :return True
    elif 'Grass' in Pokemon1.variety and 'Rock' in Pokemon2.variety :return True
    elif 'Water' in Pokemon1.variety and 'Fire' in Pokemon2.variety :return True
    elif 'Water' in Pokemon1.variety and 'Ground' in Pokemon2.variety :return True
    elif 'Water' in Pokemon1.variety and 'Rock' in Pokemon2.variety :return True
    elif 'Ground' in Pokemon1.variety and 'Fire' in Pokemon2.variety :return True
    elif 'Ground' in Pokemon1.variety and 'Electric' in Pokemon2.variety :return True
    elif 'Ground' in Pokemon1.variety and 'Poison' in Pokemon2.variety :return True
    elif 'Ground' in Pokemon1.variety and 'Rock' in Pokemon2.variety :return True
    elif 'Ground' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Electric' in Pokemon1.variety and 'Water' in Pokemon2.variety :return True
    elif 'Electric' in Pokemon1.variety and 'Flying' in Pokemon2.variety :return True
    elif 'Ice' in Pokemon1.variety and 'Grass' in Pokemon2.variety :return True
    elif 'Ice' in Pokemon1.variety and 'Ground' in Pokemon2.variety :return True
    elif 'Ice' in Pokemon1.variety and 'Flying' in Pokemon2.variety :return True
    elif 'Ice' in Pokemon1.variety and 'Dragon' in Pokemon2.variety :return True
    elif 'Fighting' in Pokemon1.variety and 'Normal' in Pokemon2.variety :return True
    elif 'Fighting' in Pokemon1.variety and 'Ice' in Pokemon2.variety :return True
    elif 'Fighting' in Pokemon1.variety and 'Rock' in Pokemon2.variety :return True
    elif 'Fighting' in Pokemon1.variety and 'Dark' in Pokemon2.variety :return True
    elif 'Fighting' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Poison' in Pokemon1.variety and 'Grass' in Pokemon2.variety :return True
    elif 'Poison' in Pokemon1.variety and 'Fairy' in Pokemon2.variety :return True
    elif 'Flying' in Pokemon1.variety and 'Grass' in Pokemon2.variety :return True
    elif 'Flying' in Pokemon1.variety and 'Fighting' in Pokemon2.variety :return True
    elif 'Flying' in Pokemon1.variety and 'Bug' in Pokemon2.variety :return True
    elif 'Psychic' in Pokemon1.variety and 'Fighting' in Pokemon2.variety :return True
    elif 'Psychic' in Pokemon1.variety and 'Poison' in Pokemon2.variety :return True
    elif 'Bug' in Pokemon1.variety and 'Grass' in Pokemon2.variety :return True
    elif 'Bug' in Pokemon1.variety and 'Psychic' in Pokemon2.variety :return True
    elif 'Bug' in Pokemon1.variety and 'Dark' in Pokemon2.variety :return True
    elif 'Rock' in Pokemon1.variety and 'Fire' in Pokemon2.variety :return True
    elif 'Rock' in Pokemon1.variety and 'Ice' in Pokemon2.variety :return True
    elif 'Rock' in Pokemon1.variety and 'Flying' in Pokemon2.variety :return True
    elif 'Rock' in Pokemon1.variety and 'Bug' in Pokemon2.variety :return True
    elif 'Ghost' in Pokemon1.variety and 'Psychic' in Pokemon2.variety :return True
    elif 'Ghost' in Pokemon1.variety and 'Ghost' in Pokemon2.variety :return True
    elif 'Dragon' in Pokemon1.variety and 'Dragon' in Pokemon2.variety :return True
    elif 'Dark' in Pokemon1.variety and 'Psychic' in Pokemon2.variety :return True
    elif 'Dark' in Pokemon1.variety and 'Ghost' in Pokemon2.variety :return True
    elif 'Steel' in Pokemon1.variety and 'Ice' in Pokemon2.variety :return True
    elif 'Steel' in Pokemon1.variety and 'Rock' in Pokemon2.variety :return True
    elif 'Steel' in Pokemon1.variety and 'Fairy' in Pokemon2.variety :return True
    elif 'Fairy' in Pokemon1.variety and 'Fighting' in Pokemon2.variety :return True
    elif 'Fairy' in Pokemon1.variety and 'Dragon' in Pokemon2.variety :return True
    elif 'Fairy' in Pokemon1.variety and 'Dark' in Pokemon2.variety :return True
    else: return False

def notEffective(Pokemon1, Pokemon2):
    if 'Fire' in Pokemon1.variety and 'Fire'in Pokemon2.variety :return True
    elif 'Fire' in Pokemon1.variety and 'Water'in Pokemon2.variety :return True
    elif 'Fire' in Pokemon1.variety and 'Rock'in Pokemon2.variety :return True
    elif 'Fire' in Pokemon1.variety and 'Dragon'in Pokemon2.variety :return True
    elif 'Grass' in Pokemon1.variety and 'Fire' in Pokemon2.variety :return True
    elif 'Grass' in Pokemon1.variety and 'Grass' in Pokemon2.variety :return True
    elif 'Grass' in Pokemon1.variety and 'Poison' in Pokemon2.variety :return True
    elif 'Grass' in Pokemon1.variety and 'Flying' in Pokemon2.variety :return True
    elif 'Grass' in Pokemon1.variety and 'Bug' in Pokemon2.variety :return True
    elif 'Grass' in Pokemon1.variety and 'Dragon' in Pokemon2.variety :return True
    elif 'Grass' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Water' in Pokemon1.variety and 'Water' in Pokemon2.variety :return True
    elif 'Water' in Pokemon1.variety and 'Grass' in Pokemon2.variety :return True
    elif 'Water' in Pokemon1.variety and 'Dragon' in Pokemon2.variety :return True
    elif 'Ground' in Pokemon1.variety and 'Grass' in Pokemon2.variety :return True
    elif 'Ground' in Pokemon1.variety and 'Bug' in Pokemon2.variety :return True
    elif 'Ground' in Pokemon1.variety and 'Flying' in Pokemon2.variety :return True
    elif 'Electric' in Pokemon1.variety and 'Electric' in Pokemon2.variety :return True
    elif 'Electric' in Pokemon1.variety and 'Grass' in Pokemon2.variety :return True
    elif 'Electric' in Pokemon1.variety and 'Dragon' in Pokemon2.variety :return True
    elif 'Electric' in Pokemon1.variety and 'Ground' in Pokemon2.variety :return True
    elif 'Normal' in Pokemon1.variety and 'Rock' in Pokemon2.variety :return True
    elif 'Normal' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Ice' in Pokemon1.variety and 'Fire' in Pokemon2.variety :return True
    elif 'Ice' in Pokemon1.variety and 'Water' in Pokemon2.variety :return True
    elif 'Ice' in Pokemon1.variety and 'Ice' in Pokemon2.variety :return True
    elif 'Ice' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Fighting' in Pokemon1.variety and 'Poison' in Pokemon2.variety :return True
    elif 'Fighting' in Pokemon1.variety and 'Flying' in Pokemon2.variety :return True
    elif 'Fighting' in Pokemon1.variety and 'Psychic' in Pokemon2.variety :return True
    elif 'Fighting' in Pokemon1.variety and 'Bug' in Pokemon2.variety :return True
    elif 'Fighting' in Pokemon1.variety and 'Fairy' in Pokemon2.variety :return True
    elif 'Poison' in Pokemon1.variety and 'Poison' in Pokemon2.variety :return True
    elif 'Poison' in Pokemon1.variety and 'Ground' in Pokemon2.variety :return True
    elif 'Poison' in Pokemon1.variety and 'Rock' in Pokemon2.variety :return True
    elif 'Poison' in Pokemon1.variety and 'Ghost' in Pokemon2.variety :return True
    elif 'Flying' in Pokemon1.variety and 'Electric' in Pokemon2.variety :return True
    elif 'Flying' in Pokemon1.variety and 'Rock' in Pokemon2.variety :return True
    elif 'Flying' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Psychic' in Pokemon1.variety and 'Psychic' in Pokemon2.variety :return True
    elif 'Psychic' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Bug' in Pokemon1.variety and 'Fire' in Pokemon2.variety :return True
    elif 'Bug' in Pokemon1.variety and 'Fighting' in Pokemon2.variety :return True
    elif 'Bug' in Pokemon1.variety and 'Poison' in Pokemon2.variety :return True
    elif 'Bug' in Pokemon1.variety and 'Flying' in Pokemon2.variety :return True
    elif 'Bug' in Pokemon1.variety and 'Ghost' in Pokemon2.variety :return True
    elif 'Bug' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Bug' in Pokemon1.variety and 'Fairy' in Pokemon2.variety :return True
    elif 'Rock' in Pokemon1.variety and 'Fighting' in Pokemon2.variety :return True
    elif 'Rock' in Pokemon1.variety and 'Ground' in Pokemon2.variety :return True
    elif 'Rock' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Ghost' in Pokemon1.variety and 'Dark' in Pokemon2.variety :return True
    elif 'Dragon' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Dark' in Pokemon1.variety and 'Fighting' in Pokemon2.variety :return True
    elif 'Dark' in Pokemon1.variety and 'Dark' in Pokemon2.variety :return True
    elif 'Dark' in Pokemon1.variety and 'Fairy' in Pokemon2.variety :return True
    elif 'Steel' in Pokemon1.variety and 'Fire' in Pokemon2.variety :return True
    elif 'Steel' in Pokemon1.variety and 'Water' in Pokemon2.variety :return True
    elif 'Steel' in Pokemon1.variety and 'Electric' in Pokemon2.variety :return True
    elif 'Steel' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    elif 'Fairy' in Pokemon1.variety and 'Fire' in Pokemon2.variety :return True
    elif 'Fairy' in Pokemon1.variety and 'Poison' in Pokemon2.variety :return True
    elif 'Fairy' in Pokemon1.variety and 'Steel' in Pokemon2.variety :return True
    else: return False

def noEffect(Pokemon1, Pokemon2):
    if 'Ground' in Pokemon1.variety and 'Flying' in Pokemon2.variety :
 #       print "Ground, Flying"
        return True
    elif 'Electric' in Pokemon1.variety and 'Ground' in Pokemon2.variety :
  #      print "Electric, Ground"
        return True
    elif 'Normal' in Pokemon1.variety and 'Ghost' in Pokemon2.variety :
   #     print "NOrmal , Ghost"
        return True
    elif 'Fighting' in Pokemon1.variety and 'Ghost' in Pokemon2.variety :
    #    print "Fighting , Ghost"
        return True
    elif 'Poison' in Pokemon1.variety and 'Steel' in Pokemon2.variety :
     #   print "Poison , Steel"
        return True
    elif 'Psychic' in Pokemon1.variety and 'Dark' in Pokemon2.variety :
      #  print "Psychic , Dark"
        return True
    elif 'Ghost' in Pokemon1.variety and 'Normal' in Pokemon2.variety :
       # print "Ghost, Normal"
        return True
    elif 'Dragon' in Pokemon1.variety and 'Fairy' in Pokemon2.variety :
        #print "Dragon, Fairy"
        return True
    else: return False

