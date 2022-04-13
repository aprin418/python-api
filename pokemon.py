from math import radians
import requests
import json
import random

randomOne = random.randint(1, 151)
randomTwo = random.randint(1, 151)


def main():
    reqOne = requests.get(f'https://pokeapi.co/api/v2/pokemon/{randomOne}')
    reqTwo = requests.get(f'https://pokeapi.co/api/v2/pokemon/{randomTwo}')
    print("HTTP status code: " + str(reqOne.status_code))
    # print(req.headers)
    responseOne = json.loads(reqOne.content)
    pokeOne = responseOne["name"]
    powerOne = responseOne['stats'][0]['base_stat']
    responseTwo = json.loads(reqTwo.content)
    pokeTwo = responseTwo["name"]
    powerTwo = responseTwo['stats'][0]['base_stat']

    if(powerOne > powerTwo):
        print(f'{pokeOne} is stronger than {pokeTwo}')
    elif(powerTwo > powerOne):
        print(f'{pokeTwo} is stronger than {pokeOne}')
    else:
        print(f'{pokeOne} and {pokeTwo} are equally matched')


if __name__ == '__main__':
    main()
