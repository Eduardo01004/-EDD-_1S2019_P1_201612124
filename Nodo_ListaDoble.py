class NodoDoble(object):

    def __init__(self, coorx=None, coory=None, siguiente=None, atras=None):
        self.coorx=corrx
        self.coory=coory
        self.siguiente=siguiente
        self.atras=atras

    def __str__(self):
        return "%s %s" %(self.coorx, self.coory)
