
# Reference
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

class SingleTone(object):
    __instance = None
    
    def __new__(cls, val):
        if SingleTone.__instance is None:
            SingleTone.__instance = object.__new__(cls)
        SingleTone.__instance.val = val
        return SingleTone.__instance
    

if __name__ == '__main__':
    x = SingleTone(7)
    y = SingleTone(5)
    print(x.val)
    print(x is y)
