class Maps():
    def __init__(self):
        self.__map = '../data/map1.txt'

    def __get_proper_map(self,index):
        map_arr = ['../data/map2.txt','../data/map3.txt','../data/map4.txt','../data/map5.txt']
        return map_arr[index - 1]

    def get_map(self):
        return self.__map

    def set_map(self, value):
        self.__map = self.__get_proper_map(value)


    def get_player_pos(self, value):
        player_pos = [(0,(30,910)),(1,(30,910)),(2,(140,500)),(3,(100,500)),(4,(100,500)),(5,(400,500))]
        for elem in player_pos:
            if elem[0] == (value + 1):
                return elem[1]

    def get_coins_pos(self, value):
        coins_pos = [(1,(60, 500)), (1,(90, 500)), (2,(50,200)),(2,(80,200))]
        temp_arr = []
        for coin in coins_pos:
            if coin[0] == value:
                temp_arr.append(coin[1])
        return temp_arr

    def load_world_from_file(self):
        with open(self.get_map(), 'r') as file:
            world_data = []
            for line in file:
                world_data.append(list(map(str, line.split())))
        return world_data


