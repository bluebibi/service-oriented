import requests

if __name__ == "__main__":
    res1 = requests.get(
        url='http://127.0.0.1:8080/resource/t2'
    )
    temperature1 = float(res1.json()["temperature"])

    res2 = requests.get(
        url='http://127.0.0.1:8080/resource/t3'
    )
    temperature2 = float(res2.json()["temperature"])

    print((temperature1 + temperature2) / 2)

