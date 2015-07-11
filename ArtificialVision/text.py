def creaciontxt():
    archi=open('datos.py','w')
    archi.close()

creaciontxt()

def creartxt():
    archi=open('datos.py','w')
    archi.close()

def grabartxt():
    archi=open('datos.py','a')
    archi.write('print "')
    archi.write('1,2,3,4"\n')
    archi.close()

creartxt()
grabartxt()
