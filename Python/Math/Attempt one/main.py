import os;
import json;

def flagError( message ):
    print("CRITICAL ERROR:",message)
    input("!!!!!!!!!!!!!!!!!!!")

def getPath():
    return os.path.dirname(os.path.dirname(__file__))+"\\"+"Equations"

class Equation:
    parentEC = -1;
    rawJSON = -1;

    name = ""
    eqString = ""
    desc = ""
    variableSymbols = []
    path = []

    variables = []

    def __init__(this, parentEC, name, JSONInp):
        this.rawJSON = JSONInp
        this.parentEC = parentEC

        this.variableSymbols = JSONInp["vars"]
        this.name = name
        this.eqString = JSONInp["eq"]
        this.desc = JSONInp["desc"]

        if name in parentEC.parentEF.allEquations:
            flagError( "duplicate of '"+name+"' equation!" )
        
        parentEC.parentEF.allEquations[ name ] = ( this )

        return

    def genHash(this):
        return hash(  this.name + this.eqString + "- -".join(str(x) for x in this.variableSymbols) )
    
    def checkConfigured(this):
        if "hash" in this.rawJSON:
            cHash = this.rawJSON["hash"];

            nHash = this.genHash();

            if ( cHash != nHash ):
                print("change detected in:",this.name)
                this.getConfiguration()

        else:
            this.getConfiguration()
    
    def getConfiguration(this):
        print( "\n\n'"+this.name+"' is not set up properly, equation:"+this.eqString )
        print("Description:",this.desc)
        print("Link it's variables.\n")

        for variable in this.variableSymbols:
            this.parentEC.parentEF.findVarSymbMatch( variable );
        

        return;

    def construct(this):
        
        this.checkConfigured();



        return;
        

class Variable:
    parentEC = -1;

    name = ""
    symbol = ""
    isConstant = False
    constValue = 0
    desc = ""
    path = []

    equations = []

    def __init__(this, parentEC, name, JSONInp):
        this.parentEC = parentEC;

        this.name = name;
        this.symbol = JSONInp["symbol"]
        this.desc = JSONInp["desc"]

        if ( "value" in JSONInp ):
            this.isConstant = True
            this.constValue = JSONInp["value"]

        this.addToMainThing();

    def stringInfo( this, indent ):
        return(
            indent + "name: "+ this.name + "\n"+
            indent + "desc: "+ this.desc + "\n"+
            indent + "path: "+ this.path
        )

    def addToMainThing(this):
        if this.name in this.parentEC.parentEF.allVarnames:
            flagError(this.name,"has a duplicate variable name!")
        else:
            this.parentEC.parentEF.allVarnames.append( this.name )


        if not this.symbol in this.parentEC.parentEF.allVariables:
            this.parentEC.parentEF.allVariables[this.symbol] = []
        
        this.parentEC.parentEF.allVariables[this.symbol].append( this )

        if ( this.isConstant ):
            if not this.symbol in this.parentEC.parentEF.allConstants:
                this.parentEC.parentEF.allConstants[this.symbol] = []
            
            this.parentEC.parentEF.allConstants[this.symbol].append( this )

    
        
  
class EqCatagory:
    parentEF = -1

    topics = {

    }

    desc = ""
    name = ""
    variables = []

    def __init__(this, parentEF, JSONInp ):
        this.parentEF = parentEF;
        this.name = JSONInp["dir"];

        path = getPath() + "\\" + this.name + "\\"
        
        for i in range(0, len( JSONInp["subs"] ) ):
            sub = JSONInp["subs"][i]
            fContents = open( path + sub + ".json" , "r").read() 
            tmp = json.loads( fContents )

            this.loadVars( tmp["variables"] )
            this.loadTopic( sub, tmp["equations"] )

    def loadVars( this, JSONinp ):
        
        for varName in JSONinp:
            this.variables.append( Variable( this, varName, JSONinp[varName] ) )

        return;

    
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

    allEquations = {}
    allVariables = {}
    allConstants = {}

    allVarnames = []

    eqCatagorys = {}

    def findVarSymbMatch( this, symbol ):
        if ( symbol in this.allVariables ):
            matches = this.allVariables[symbol];

            for i in range(0, len(matches) ):
                print(i,":")
                print( matches[i].stringInfo("\\ "),"\n" )
            
            return;
        else:

            return;

    def createVariable( this, symbol ):
        print("the symbol '"+symbol+"' has no variables assosiated with it.")

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

        print("all vars:", this.allVariables.keys() )

        for catagory in this.eqCatagorys:
            this.eqCatagorys[catagory].construct()

        for equation in this.allEquations:
            this.allEquations[equation].construct()
        

        



def count_sub_in_file( filename, s ):
    return open( os.path.dirname(__file__) + "\\" +filename, "r" ).read().count( s );



tmp = EquationFetcher();

print(getPath());