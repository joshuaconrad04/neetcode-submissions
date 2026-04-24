class Singleton:
#underscore is to make it private
#In python, putting it outside methods in the class makes it static
    _instance = None
    _value = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        #CLS corresponds to the class itself
        if cls._instance is None:
            #This mean thats the class = a new instance of itself
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def getValue(self) -> str:
        return self._value

    def setValue(self, value: str):
       self._value = value
