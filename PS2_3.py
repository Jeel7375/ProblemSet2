class Marsupial:

    def __init__(self,name,contents=[]):
        self.name = name
        self.pouch_contents = contents
    
    def __str__(self):
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = ' ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)
    
    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

class Kangaroo(Marsupial):
    def __init__(self, name, contents=[]):
        Marsupial.__init__(self, name, contents)
        
K = Kangaroo('Kanga')
K.put_in_pouch('doll')
K.put_in_pouch('firetruck')
K.put_in_pouch('Kitten')
print(K)