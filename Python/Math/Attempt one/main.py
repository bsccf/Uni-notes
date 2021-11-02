import os;
import json;

def getPath():
    return os.path.dirname(os.path.dirname(__file__))+"\\"+"Equations"

class equation:
    name = ""
    eq = ""
    desc = ""
    variables = ""
    path = []

    def __init__(this):
        return this
    
class topic:
    equations = {}

    desc = ""
    name = ""

    def __init__(this):
        return this

class equationFetcher:
    rootJSON = ""
    subDirs = []

    def __init__(this):
        print("init")
        this.getRootJson();
        print( this.rootJSON );
        this.getSubs()
    
    def getRootJson(this):
        rFile = open( 
            getPath() + "\\Equations.json"
        )
        this.rootJSON = json.loads( rFile.read() )
        rFile.close();

    def getSubs(this):
        subDirs = []
        locations = this.rootJSON["locations"]

        for i in range(0, len(locations)):
            location = locations[i]
            subDirs
        



def count_sub_in_file( filename, s ):
    return open( os.path.dirname(__file__) + "\\" +filename, "r" ).read().count( s );



tmp = equationFetcher();

print(getPath());