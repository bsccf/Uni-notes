import os;
import json;

def flagError( message ):
    print("CRITICAL ERROR:",message)
    input("!!!!!!!!!!!!!!!!!!!")

def getPath():
    return os.path.dirname(os.path.dirname(__file__))+"\\"+"Equations"

class equation:
    name = ""
    eq = ""
    desc = ""
    variables = ""
    path = []

    def __init__(this):
        return
        


  
class topic:
    parentEF = -1

    equations = {}

    desc = ""
    name = ""
    variables = {
        "x": {
            "name": equation()
        }
    }

    def __init__(this, parentEF, JSONInp ):
        this.parentEF = parentEF;
        this.name = JSONInp["dir"];
        
        
        return this



class equationFetcher:
    rootJSON = ""
    subDirs = []

    topics = {}

    def __init__(this):
        print("init")
        this.getRootJson();
        print( this.rootJSON );
        this.generateTopics()
    
    def getRootJson(this):
        rFile = open( 
            getPath() + "\\Equations.json"
        )
        this.rootJSON = json.loads( rFile.read() )
        rFile.close();

    def generateTopics(this):
        subDirs = []
        locations = this.rootJSON["locations"]

        for i in range(0, len(locations)):
            location = locations[i]
            if ( location["dir"] in this.topics ):
                flagError( location["dir"] + " is a duplicate topic name!")

            this.topics[ location["dir"] ] = topic( this, location ); 
        



def count_sub_in_file( filename, s ):
    return open( os.path.dirname(__file__) + "\\" +filename, "r" ).read().count( s );



tmp = equationFetcher();

print(getPath());