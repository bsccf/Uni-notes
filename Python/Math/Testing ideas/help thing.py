import os

def count_sub_in_file( filename, s ):
    return open( os.path.dirname(__file__) + "\\" +filename, "r" ).read().count( s );

print( count_sub_in_file( "lmao.txt", "awd" ) )

