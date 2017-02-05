'''
Created on 5 лют. 2017

@author: Valentin
'''

if __name__ != '__main__':
    print("Classes module loaded!") 

class SuperClass():
    '''
    The super class
    '''

    def __init__(self):
        '''
        Constructor
        '''
       
    def func1(self):
        return "function 1 SuperClass called!" 
    
    def func2(self):
        return "function 2 SuperClass called!" 
       

class InheritedClass(SuperClass):
    '''
    The Inherited class
    '''

    def __init__(self):
        '''
        Constructor
        '''
       
    def func1(self):
        print(SuperClass.func1(self))
        return "function 1 InheritedClass called!" 
    
    def func2(self):
        return "function 2 InheritedClass called!" 
              
       