import groupy
from groupy.client import Client

messenger = Client.from_token('vqCQ3p7KD4jC467sj1IrbISwDAHGCMXTVhcWuKNI')

chatName = 'Business'
business = None

for group in messenger.groups.list_all():
    if group.name == chatName:
        business = group
        break

if business is None:
    print("Group doesn't exist.")



def sendList(list):
    message  = '\n'.join([' '.join([str(item) for item in row]) for row in list])
    business.post(message)

def getBrother(name :str):
    chatNames = {
    'A J Alexander': 'Aj Alexander',
    'Albert Diaz': 'Albert Diaz',
    'Allen Butler': 'Allen Butler',
    'Anthony S’Chevalier': 'Anthony S’Chevalier',
    'Ben Jaimes': 'Benjamin Jaimes',
    'Blake Rodgers': 'Blake Rodgers',
    'Bobby Gang': 'Bobby Gang',
    'Brandon Shelton': 'Brandon Shelton',
    'Brant Kimberling': 'Brant Kimberling',
    'Brock Simsek': 'Brock',
    'Brody Mcnett': 'Brody Mcnett',
    'Carlin Livermore': 'Carlin Livermore',
    'C J Gonzales': 'Christian Gonzales',
    'Christian Rives': 'Christian Rives',
    'Christian Villarreal': 'Christian Villarreal',
    'Cooper Maxwell': 'Cooper Maxwell',
    'Daniel Avitia': 'Daniel Avitia',
    'David Carroll': 'David Carroll',
    'David Wilkins': 'David  Wilkins',
    'Dillon Cullor': 'Dillon Cullor',
    'Dillon Zimmer': 'Dillon Zimmer',
    'Dylan Hinkle': 'Dylan Hudson',
    'Eli Mitchell': 'Eli Mitchell',
    'Erik Trevino': 'Erik Trevino',
    'Ethan Wintill': 'Ethan Wintill',
    'Garrett Godfredson': 'Garrett Godfredson',
    'Grant Poss': 'Grant Poss',
    'Hayden Selby': 'Hayden Selby',
    'Jay Wright': 'J Wright',
    'Jacob Robinson': 'Jake Robinson',
    'Jarod Maxson': 'Jarod Maxson',
    'Jaxson Gonzales': 'jaxson gonzalez',
    'Jaylen Stewart': 'Jaylen Stewart',
    'Jerry Garza': 'Jerry  Garza',
    'Josh P': 'Josh P',
    'Josh Andrews': 'Joshua Andrews',
    'Kyle Mote': 'Kyle Mote',
    'Landen Charles': 'Landen Charles',
    'Landen Johnson': 'Landen johnson',
    'Lucas McCrum': 'Lucas McCrum',
    'Mathew Madrid': 'Mathew Madrid',
    'Matt Shaw': 'Matt Shaw',
    'Matt Cameron': 'Matthew Cameron',
    'Milton Cerda': 'Milton Cerda',
    'Morgan Haught': 'Morgan Haught',
    'Nick Henry': 'Nick Henry',
    'Petey Fuentes': 'Petey Fuentes',
    'Pierce Stratton': 'Pierce',
    'Roberto Garcia': 'Roberto Garcia',
    'Ryan Lothschutz': 'Ryan Lothschutz',
    'Sam Bryant': 'Sam Bryant',
    'Seth Hussey': 'Seth Hussey',
    'Stephan Nunez': 'Stephan Nunez',
    'TJ Godfredson': 'Trevor Godfrenson',
    'Trey Lucero': 'Trey Lucero',
    'Tristan Garcia': 'Tristan Garcia',
    'Turner Colley': 'Turner Colley',
    'Ty McBride': 'Ty McBride',
    'Tyler Martinez': 'Tyler Martinez',
    'Zach Coady': 'Zach Coady'
    }
    nameInChat = chatNames.get(name)

    if nameInChat is None:
        print(name + " not found in dictionary! groupmeManager.getBrother()")
        return None
    
    result = [brother for brother in business.members if brother.name == nameInChat]
    if(len(result)==0):
        print(name + " not found in groupme! groupmeManager.getBrother()")
        return None
    
    return result[0]





