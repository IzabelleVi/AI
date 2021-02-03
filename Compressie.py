ch = [1,0,1,1,1,0,0]

def verschuiving(ch, n):

    print( ch[n:] + ch[:n] )

verschuiving(ch, -4)