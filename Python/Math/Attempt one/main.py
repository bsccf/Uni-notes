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
        
  
class eqCatagory:
    parentEF = -1

    topics = {

    }

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

        path = getPath() + "\\" + this.name + "\\"
        
        for i in range(0, len( JSONInp["subs"] ) ):
            sub = JSONInp["subs"][i]
            fContents = open( path + sub + ".json" , "r").read() 
            topicJSON = json.loads( fContents )

            this.loadTopic( sub, topicJSON )

            
        
        return this
    
    def loadTopic(this, name, JSONInp):
        if name in this.topics:
            flagError( name + " already exists warning!" )
        
        this.topics[ name ] = JSONInp




class equationFetcher:
    rootJSON = ""
    subDirs = []

    eqCatagorys = {}

    def __init__(this):
        print("init")
        this.getRootJson();
        print( this.rootJSON );
        this.generateEqCatagorys()
    
    def getRootJson(this):
        rFile = open( 
            getPath() + "\\Equations.json"
        )
        this.rootJSON = json.loads( rFile.read() )
        rFile.close();

    def generateEqCatagorys(this):
        subDirs = []
        locations = this.rootJSON["locations"]

        for i in range(0, len(locations)):
            location = locations[i]
            if ( location["dir"] in this.eqCatagorys ):
                flagError( location["dir"] + " is a duplicate topic name!")

            this.eqCatagorys[ location["dir"] ] = eqCatagory( this, location ); 
        



def count_sub_in_file( filename, s ):
    return open( os.path.dirname(__file__) + "\\" +filename, "r" ).read().count( s );



tmp = equationFetcher();

print(getPath());