from calendar import c
from matplotlib import bezier
import matplotlib.pyplot as plt

import math

class Graphboi:
    
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
        this.x = []
        this.y = []


def basicPoly( x ):

    return x**2 + 2*x + 1

class BezCurve:

    def C( this, n, i ):
        return math.factorial( n )/( math.factorial(i) * math.factorial(n-i) )

    def __init__(this, pointCount = 3):
        this.points = []
        this.weights = []
        this.pointCount = 0
            
        this.graphXs = []
        this.graphYs = []

        this.maxX = 0
        this.maxY = 0
        this.minX = 0
        this.minY = 0

        this.pointCount = pointCount

        for i in range(0, pointCount):
            this.points.append( [ i, i%2 ] )
            this.weights.append( 1 )


    def setPoint( this, n, x, y, weight = -1 ):
        this.points[n][0] = x
        this.points[n][1] = y
        if ( weight > 0 ):
            this.weights[n] = weight
        
    def addPoint( this, x, y, weight = -1 ):
        this.insertPoint( this.pointCount, x, y, weight )
    
    # inserts point before element at given n value
    def insertPoint( this, n, x, y, weight = -1 ):
        
        if (n == this.pointCount):
            this.points.append([0,0])
        else:
            this.points.insert(n, [0,0])
        
        this.pointCount+=1;

        this.points[n][0] = x
        this.points[n][1] = y

        this

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

        SAMPLES = 300
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

class SplineGroup:

    def __init__(this, startX, startY, endX, endY):
        this.bezCurves = []

        fCurve = BezCurve( 3 );

        fCurve.setPoint( 0, startX, startY )
        fCurve.setPoint( 1, startX, endY)
        fCurve.setPoint(2, endX, endY)

        this.bezCurves.append( fCurve );

    def addSpline(this, inpCurve=-1 ):
        if ( inpCurve == -1 ):
            this.bezCurves.append(BezCurve(3))
        
        else:
            this.bezCurves.append( inpCurve )

        this.connectAllSplines()

    def connectSplines( this, spline1, spline2 ):
        spline2.points[0] = spline1.points[spline1.pointCount-1]

    def connectSplinesCont( this, spline1, spline2 ):
        this.connectSplines( spline1, spline2 )
        
        commonPoint = spline2.points[0]
        spline1RPoint = spline1.points[spline1.pointCount-2]
        gradPoint = spline2.points[1]
        spline2RPoint = spline2.points[2]

        if ( (commonPoint[0]-spline1RPoint[0]) != 0 ):

            m = (commonPoint[1]-spline1RPoint[1])/(commonPoint[0]-spline1RPoint[0])
            c = commonPoint[1] - (m*commonPoint[0])

            gradPoint[0] = (spline2RPoint[0]+(m*(spline2RPoint[1]-c)))/(1+(m**2))
            gradPoint[1] = (gradPoint[0]*m) + c

            #tmp = Graphboi()
            #tmp.addPoints( [ spline1RPoint[0], commonPoint[0], gradPoint[0], spline2RPoint[0],1,0,0 ], [ spline1RPoint[1], commonPoint[1], gradPoint[1], spline2RPoint[1],0,0,1 ] )
            #tmp.render()

        else:
            gradPoint[0] = commonPoint[0]
            gradPoint[1] = spline2RPoint[1]

        return;

    def connectAllSplinesCont(this):
        for i in range(0, len( this.bezCurves ) - 1 ):
            this.connectSplinesCont( this.bezCurves[i], this.bezCurves[i+1] )

    def connectAllSplines(this):
        for i in range(0, len( this.bezCurves ) - 1 ):
            this.connectSplines( this.bezCurves[i], this.bezCurves[i+1] )

    def render(this):
        graph = Graphboi()

        for curve in this.bezCurves:
            curve.genGraphPoints()
            graph.addPoints( curve.graphXs, curve.graphYs )

        graph.render()

class Shape:
    def __init__(this):
        this.points = []

    def addPoint(this, x, y):
        this.points.append( [x, y] )

    def render(this):
        pointCount = len(this.points)

        if ( pointCount <= 2 ):
            return

        sG = SplineGroup( this.points[0][0], this.points[0][1], this.points[1][0], this.points[1][1] )

        for i in range(1, pointCount):
            cSpline = BezCurve(3)

            cPoint = this.points[i]
            nPoint = this.points[(i+1)%pointCount]

            cSpline.setPoint( 0, cPoint[0], cPoint[1] )
            cSpline.setPoint( 2, nPoint[0], nPoint[1] )

            sG.addSpline( cSpline )

        sG.connectAllSplinesCont()

        sG.render()

y = Shape()

y.addPoint(1,1)
y.addPoint(2.2,3)
y.addPoint(3,1)
y.addPoint(5,1)
y.addPoint(2,0)

y.render()
"""

x = SplineGroup( 0, 0, 1, 1 )
x.bezCurves[0].points[1] = [0.3, 0.8]

nCurve = BezCurve();

nCurve.setPoint(2, 2, 1)

x.addSpline( nCurve )

x.connectAllSplinesCont()

x.render()

tmp = BezCurve( 4 )


tmp.setPoint( 0, 6, 4 )

tmp.setPoint( 1, 6, 2 )
tmp.setPoint( 2, 4, 2 )
tmp.setPoint( 3, 3, 6 )



tmp.render()
"""
print("")

