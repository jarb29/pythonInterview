import requests

BASE_URL = "https://dogs.magnet.cl"

def auth(email, password):
    data = {
        'email': email,
        'password': password,
    }
    error_message = 'Invalid credentials'

    response_data = requests.post(
        BASE_URL + '/api/v1/auth/',
        data=data,
    )
    res = response_data.json()
    print(res)

    if 'token' not in res:
        if 'nonFieldErrors' in res:
            raise ValueError(res['nonFieldErrors'])
        raise ValueError(error_message)
    return res['token']




class Doghouse:
    def __init__ (self):
        self.breeds: List[Breed] = []
        self.dogs: List[Dog] = []

        

    def get_data(self, token):
        print(token)
        headers = {
        'content-type': 'application/json',
        'Authorization': 'JWT' + token
        }
   

        data_breeds = requests.get("https://dogs.magnet.cl/api/v1/breeds/?limit=20&offset=10", headers=headers)
        data_dogs = requests.get("https://dogs.magnet.cl/api/v1/dogs/", token, headers=headers)
        print(data_breeds)
        print(data_dogs)

        return data_breeds.json(), data_dogs.json()



def main():
    credentials = {
        'email': 'jarb29@gmail.com',
        'password': 'Alexander29'
    }

    token = auth(**credentials)

    dog_house = Doghouse()
    dog_house.get_data(token=token)
   

main()








    




