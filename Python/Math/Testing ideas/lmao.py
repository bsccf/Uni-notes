iText = """Southampton / Weather Centre, United Kingdom (EGHI) 50-54N 001-24W 0M
Nov 04, 2021 - 08:50 AM EDT / 2021.11.04 1250 UTC
Wind: from the N (350 degrees) at 14 MPH (12 KT) (direction variable):0
Visibility: greater than 7 mile(s):0
Sky conditions: mostly cloudy
Temperature: 48 F (9 C)
Dew Point: 39 F (4 C)
Relative Humidity: 70%
Pressure (altimeter): 30.00 in. Hg (1016 hPa)
ob: EGHI 041250Z 35012KT 300V020 9999 BKN023 09/04 Q1016 
cycle: 13"""

def getTemp( inp ):
    x = inp[ inp.index("Temperature:") :][ 0 : inp[ inp.index("Temperature:") :].index("\n") ];
    return int( x[ x.index("(")+1 : x.index("C") ] )

print( getTemp( iText ) )
