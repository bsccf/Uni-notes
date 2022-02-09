from calendar import c
import matplotlib.pyplot as plt

import math

class Graphboi:
    x = []
    y = []
    
    def addPoint(this, nX, nY):
        this.x.append( nX );
        this.y.append( nY )

    def addPoints(this, nX, nY):
        if ( len( nX ) != len( nY ) ):
            print("bad")
            return;
        
        for cNX in nX:
            this.x.append( cNX );
        
        for cNY in nY:
            this.y.append( cNY );

    def render(this):
        plt.plot( this.x, this.y );
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    
    def genPointsFromFunc( this, function, minX = 0, maxX = 10, increment = 0.025 ):
        i = minX
        while (i<maxX):
            this.addPoint( i, function( i ) )

            i += increment

    def __init__(this):

        print(this)


def basicPoly( x ):

    return x**2 + 2*x + 1

class BezCurve:
    points = []
    weights = []
    pointCount = 0
        
    graphXs = []
    graphYs = []

    maxX = 0
    maxY = 0
    minX = 0
    minY = 0

    def C( this, n, i ):
        return math.factorial( n )/( math.factorial(i) * math.factorial(n-i) )

    def __init__(this, pointCount = 3):
        this.pointCount = pointCount

        for i in range(0, pointCount):
            this.points.append( [ i, i%2 ] )
            this.weights.append( 1 )

    def setPoint( this, n, x, y, weight = -1 ):
        this.points[n][0] = x
        this.points[n][1] = y
        if ( weight > 0 ):
            this.weights[n] = weight
        
        

    def setWeight( this, n, weight ):
        this.weights[n] = weight

    def updateRange( this ):
        this.maxX = this.points[0][0]
        this.minX = this.points[0][0]
        this.maxY = this.points[0][1]
        this.minY = this.points[0][1]

        for point in this.points:
            if ( point[0] > this.maxX ):
                this.maxX = point[0]
            elif ( point[0] < this.minX ):
                this.minX = point[0]

            if ( point[1] > this.maxY ):
                this.maxY = point[1]
            elif ( point[1] < this.minY ):
                this.minY = point[1]
        return


    def genGraphPoints( this ):
        this.graphXs = []
        this.graphYs = []

        this.updateRange()

        SAMPLES = 500
        increment = (this.maxX-this.minX)/SAMPLES
        
        t = 0

        pWM = []
        #for weight in this.weights:
        #    pWM.append( weight *  )

        while ( t <= 1 ):
            x = 0
            y = 0

            for i in range(0, this.pointCount ):
                cWFuncOup = ( this.C( this.pointCount-1, i ) * ( t**(i) ) * ( ( 1-t )**(this.pointCount-(i+1)) ) ) 

                x += this.points[i][0] * cWFuncOup
                y += this.points[i][1] * cWFuncOup

            this.graphXs.append( x )
            this.graphYs.append( y )

            t += 1/SAMPLES

        return 

    def render(this):
        graph = Graphboi()

        this.genGraphPoints()

        graph.addPoints( this.graphXs, this.graphYs )

        graph.render()

        

tmp = BezCurve( 25 )

tmp.setPoint( 0, 6, 4 )

tmp.setWeight( 1, 2 )

tmp.setPoint( 1, 6, 2 )
tmp.setPoint( 2, 4, 2 )
tmp.setPoint( 3, 2, 2 )
tmp.setPoint( 4, 2, 4 )
tmp.setPoint( 5, 2, 6)
tmp.setPoint( 6, 4, 6)
tmp.setPoint( 7, 6, 6)
tmp.setPoint( 8, 6, 4)

tmp.setPoint( 9, 7, 4)
tmp.setPoint( 10, 8, 4)
tmp.setPoint( 11, 9, 1)
tmp.setPoint( 12, 10, 4)
tmp.setPoint( 13, 11, 1)
tmp.setPoint( 14, 12, 4)
tmp.setPoint( 15, 13, 4)
tmp.setPoint( 16, 14, 4)
tmp.setPoint( 17, 14, 6)
tmp.setPoint( 18, 16, 6)
tmp.setPoint( 19, 18, 6)
tmp.setPoint( 20, 18, 4)
tmp.setPoint( 21, 18, 2)
tmp.setPoint( 22, 16, 2)
tmp.setPoint( 23, 14, 2)
tmp.setPoint( 24, 14, 4)

""""""

tmp.render()

print("")
