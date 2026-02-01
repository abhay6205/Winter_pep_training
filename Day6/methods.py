
"""
class Animals:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'
        
    def type(self, t=None):
        if t: self._type = t
        return self._type
    
    def name(self,n=None):
        if n: self._name = n
        return self._name
    
    def sound(self, s=None):
        if s: self._sound = s
        return self._sound
    
    def __str__(self):
        return f'The {self.type()} is named {self.name()} and says {self.sound()}'
    
    
def main():
    a0 = Animals(type = 'Kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animals(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)
    
if __name__ == '__main__': main()
"""


class Car:
    def __init__(self, **kwargs):
        self._color = kwargs['color'] if 'color' in kwargs else 'Blue'
        self._tyre = kwargs['tyre'] if 'tyre' in kwargs else '4'
        self._model = kwargs['model'] if 'model' in kwargs else 'B340'
        
    def color(self, c=None):
        if c: self._color = c
        return self._color
    
    def tyre(self, t=None):
        if t: self._tyre = t
        return self._tyre
    
    def model(self, m=None):
        if m:self._model = m
        return self._model
    
    def __str__(self):
        return f'The car color is {self.color()} and model number {self.model()} with {self.tyre()} number of tyre'
    
def main():
    a0 = Car(color = 'Red', model = 'B546', tyre = '4+1')
    a1 = Car(color = 'duck', model = 'C853', tyre = '4+2')
    print(a0)
    print(a1)
    
if __name__ == '__main__': main()