class Animals:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']
        
    def type(self, t=None):
        if t: self._type = t
        try: return self._type
        except AttributeError: return None
    
    def name(self,n=None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None
    
    def sound(self, s=None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return None
    
    # def __str__(self):
    #     return f'The {self.type()} is named {self.name()} and says {self.sound()}'
    
class Duck(Animals):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)
        
class Kitten(Animals):
    def __init__(self, **kwargs):
        self._type = 'Kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)
    
def print_animal(O):
    if not isinstance(O,Animals):
        raise TypeError('Print_animal(): requires an animals')
    print(f'The {O.type()} is named {O.name()} and says {O.sound()}')

def main():
    a0 = Animals(type = 'Kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animals(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)
    
if __name__ == '__main__': main()