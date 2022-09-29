import requests
from tqdm import tqdm

url = input("Введите адрес ресурса")

for i in tqdm(range(1000)):
    requests.get(url)