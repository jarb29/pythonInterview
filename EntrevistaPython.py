from lib import auth, get
import statistics 



class Dog:
    def __init__(self, id: int, name: str, breed: int):
        self.id = id
        self.name = name
        self.breed = breed




class Breed(object):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.dogs: List[Dog] = []

    def add_dog(self, dog: Dog):
        self.dogs.append(dog)

    def dogs_count(self) -> int:
        return len(self.dogs)






class Doghouse:
    def __init__ (self):
        self.breeds: List[Breed] = []
        self.dogs: List[Dog] = []
            


    def get_data(self, token):
        breeds = get(url='http://dogs.magnet.cl/api/v1/breeds/', token=token)
        self.breeds.append(breeds['results'])

        dogs = get(url='http://dogs.magnet.cl/api/v1/dogs/', token=token)
        self.dogs.append(dogs['results'])


        
        limit = 10
        while limit <= breeds['count']:
            url = 'http://dogs.magnet.cl/api/v1/breeds/?limit={}&offset=10'.format(limit)
            breeds = get(url, token=token)
            self.breeds.append(breeds['results'])
            limit += 10


        b = dogs['count']/len(dogs['results'])


        page = 1
        while page <= b:
            url = 'http://dogs.magnet.cl/api/v1/dogs/?page={}'.format(page)
            dogs = get(url, token=token)
            self.dogs.append(dogs['results'])
            page += 1
        
        return breeds, dogs

    def get_total_breeds(self):
        different_breeds = []
        dog_repetidos = []
        for i in self.breeds:
            for x in i:
                if x['name'] is not different_breeds:
                     different_breeds.append(x['name'])
                else:
                    dog_repetidos.append(x['name'])
                    
        size = len(different_breeds)
        print(size, 'different breeds')
        return size
    

    
    
    def get_total_dogs(self):
        dogs_names = []
        for i in self.dogs:
            for name in i:
                dogs_names.append(name['name'])
        size = len(dogs_names)
        print(size, 'Is the number of total dogs containing in this data')
        return dogs_names

    def get_common_breed(self):
        common_breed = []
        for i in self.dogs:
            for breed in i:
                common_breed.append(breed['breed'])
        res = max(set(common_breed), key = common_breed.count) 

        for breeds in self.breeds:
            for breed in breeds:
                if breed['id'] == res:
                    b = breed['name']
                    print(b, 'is the most most popular breed')
                    break
            return  b
        return b

    def get_common_dog_name(self, names):

        res = max(set(names), key= names.count)
        print(res, 'Is the most popular name')
        return res




       


 


     





def main():
    credentials = {
            'email': 'jarb29@gmail.com',
            'password': 'Alexander29'
        }

    dog_house = Doghouse()
    token = auth(**credentials)
    dog_house.get_data(token=token)
    total_breeds = dog_house.get_total_breeds()
    total_dogs = dog_house.get_total_dogs()
    common_breed = dog_house.get_common_breed()
    common_dog_name = dog_house.get_common_dog_name(total_dogs)

  

main()








    




