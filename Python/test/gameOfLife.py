import random
import math

# the only comment in this file

def geometric_mean(a,b):
    return pow(a*b, 0.5)

def distance(a,b):
    return abs( a-b )

def pyramid_volume(A,h):
    return A*h*1/3

print( distance( 3, 4 ) )
print( distance( 3, 1 ) )

print( geometric_mean( 2, 2 ) )
print( geometric_mean( 2, 8 ) )
print( geometric_mean( 2, 1 ) )

print( pyramid_volume( 1, 2 ) )

class Map:
    def __init__(this, width, height):
        this.width = width;
        this.height = height;
        this.grid = [];
        
        this.generateMap();


    def generateMap( this ):
        this.grid = [];
        for x in range(0, this.width):
            this.grid.append( [] )
            for y in range(0, this.height):
                this.grid[x].append(0)
    
    def printMap( this ):
        oup = "";
        for x in range(0, this.width):
            oup += "\n" + str( x ) + "\t| "
            for y in range(0, this.height):
                oup += str( this.grid[x][y] ) + " "
        print( oup );
    
    def getTile( this, x, y ):
        x = x%this.width
        y = y%this.height

        while ( x<0 ): x += this.width
        while ( y<0 ): x += this.height

        return this.grid[x][y]

    def setTile( this, x, y, value ):
        x = math.floor( x%this.width - 0.5 )
        y = math.floor( y%this.height - 0.5)

        while ( x<0 ): x += this.width
        while ( y<0 ): x += this.height

        this.grid[x][y] = value

class CGL:
    def __init__(this, width, height):
        this.width = width;
        this.height = height;
        this.map = Map( width, height )
        this.nextMap = Map( width, height )

    def randomize( this, prob ):
        for x in range(0, this.width):
            for y in range(0, this.height):
                if ( ( random.uniform(0, 1) ) < ( prob ) ):
                    this.map.grid[x][y] = 1
                else:
                    this.map.grid[x][y] = 0
    
    def nextGeneration( this ):
        for x in range(0, this.width):
            for y in range(0, this.height):
                this.processTile( x, y )

        this.map = this.nextMap
        this.nextMap = Map( this.width, this.height )
    
    def genPatternCircle( this, size ):
        grid = this.map.grid;

        cX = int(this.width/2)
        cY = int(this.height/2)

        for i in range(0, 2000):
            xA = math.sin( i/133 ) * size
            yA = math.cos( i/133 ) * size
            this.map.setTile( cX+xA, cY+yA, 1 )

    
    def processTile( this, x, y ):
        grid = this.map.grid;
        neighbours = 0
        
        for xAdj in range( 0, 3 ):
            for yAdj in range( 0,3 ):
                if ( this.map.getTile( x+xAdj-1, y+yAdj-1 ) == 1 ): neighbours+=1;

        if ( grid[x][y] == 0 ):
            this.nextMap.grid[x][y] = [ 0, 0, 0, 1, 0, 0, 0, 0, 0 ][neighbours]
        else:
            this.nextMap.grid[x][y] = [ 0, 0, 1, 1, 0, 0, 0, 0, 0 ][neighbours-1]
    
    def print( this, liveCell, deadCell ):
        grid = this.map.grid;
        oup = "";
        for x in range(0, this.width):
            oup += "\n" + str( x ) + "\t| "
            for y in range(0, this.height):
                if( grid[x][y] == 1 ): oup += liveCell + " "
                else:oup += deadCell + " "
        print( oup );

def floatInp( message ):
    while (True):
        try:
            inp = input( message )
            if ( inp == "" ):
                return 0
            return float( inp )
        except:
            print("invalid input")


lt = "O"
dt = " "

tmp = CGL( 40, 80 )
tmp.print(lt, dt);
tmp.randomize( float( floatInp("prob: ") ) );
"""tmp.genPatternCircle( 4 );
tmp.genPatternCircle( 7 );
tmp.genPatternCircle( 10 );
tmp.genPatternCircle( 2 );
tmp.genPatternCircle( 50 );"""
tmp.print(lt, dt);

skip = 0
inp = 0

for i in range(0, 100000):
    skip -= 1

    tmp.nextGeneration();
    
    if ( skip <= 0 ):
        inp = int( floatInp("generation: "+ str(i) + "   skip:" ) );
        tmp.print(lt, dt);

    if ( inp != 0 ):
        skip = int( inp )
        inp = 0
    






