import os;
import json;

def flagError( message ):
    print("CRITICAL ERROR:",message)
    input("!!!!!!!!!!!!!!!!!!!")

def getPath():
    return os.path.dirname(os.path.dirname(__file__))+"\\"+"Equations"

class Equation:
    parentEC = -1;

    name = ""
    eqString = ""
    desc = ""
    variables = []
    path = []

    def __init__(this, parentEC, name, JSONInp):
        this.parentEC = parentEC

        this.variables = JSONInp["vars"]
        this.name = name
        this.eqString = JSONInp["eq"]
        this.desc = JSONInp["desc"]
        return

    
        
  
class EqCatagory:
    parentEF = -1

    topics = {

    }

    desc = ""
    name = ""
    variables = {
        "x": {
            #"name": Equation()
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

    
    def loadTopic(this, name, JSONInp):
        if name in this.topics:
            flagError( name + " already exists warning!" )
        
        eqs = {};

        for eq in JSONInp:
            eqs[ eq ] = Equation( this, eq, JSONInp[eq] )


        this.topics[ name ] = eqs

    def construct( this ):

        return;




class EquationFetcher:
    rootJSON = ""

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
        locations = this.rootJSON["locations"]

        for i in range(0, len(locations)):
            location = locations[i]
            if ( location["dir"] in this.eqCatagorys ):
                flagError( location["dir"] + " is a duplicate topic name!")

            this.eqCatagorys[ location["dir"] ] = EqCatagory( this, location ); 

        for catagory in this.eqCatagorys:
            this.eqCatagorys[catagory].construct()
        

        



def count_sub_in_file( filename, s ):
    return open( os.path.dirname(__file__) + "\\" +filename, "r" ).read().count( s );



tmp = EquationFetcher();

print(getPath());