class Item():
    #uj instance pl item = Item("xyz",(str,int,2),'image path?')
    def __init__(self,name, attributes, image):
        self.__name = name
        self.__first_attribute = attributes[0]
        self.__second_attribute = attributes[1]
        self.__value = attributes[2]
        self.image = image

    def get_first_attribute(self):
        return self.__first_attribute
    
    def get_second_attribute(self):
        return self.__second_attribute
    
    def get_value(self):
        return self.__value

    def __eq__(self, other):
        if isinstance(other, Item):
            return (self.__name == other.__name and self.__first_attribute == other.__first_attribute and self.__second_attribute == other.__second_attribute 
                    and self.__value == other.__value and self.image == other.image)
        return False
