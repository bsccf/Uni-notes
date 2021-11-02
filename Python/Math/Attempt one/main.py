import os;

def getPath():
    return os.path.dirname(os.path.dirname(__file__))+"Equations"

def count_sub_in_file( filename, s ):
    return open( os.path.dirname(__file__) + "\\" +filename, "r" ).read().count( s );





print(getPath());