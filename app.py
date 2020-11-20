from flask import Flask
import requests

app = Flask(__name__)
headersUdemy = {
  "Accept": "application/json, text/plain, */*",
  "Authorization": "Basic eHVRS2NWNGVYRTJzSmc3V1Rkem5zdnlGS2kxOGd3UVdZMU1yUmNHQzpjclhkZGZhd0hBQjYyZjVsa05tdVhxS0N6cEg3ME1hMGpPTFNuMEtEakxWeFpxbmxNb0lZM0VyaEIwNjF6MDdCbUxZb3Npc1pMd3ZaWTI5bUJ3dUh4MzN2a2VGMmZtYzVHNTdrTW1WeUdQUHFkVXJmU3R3SGhlQjNVTXVEbUJzTA==",
  "Content-Type": "application/json;charset=utf-8"
}

pathCursos = ""
for x in range(2):
    #request = requests.get('https://www.udemy.com/api-2.0/courses/?language=pt&ordering=relevance&page=100&page_size=100',headers=headersUdemy)
    request = requests.get('https://www.udemy.com/api-2.0/courses/?language=pt&ordering=relevance&page={}&page_size=100'.format(x),headers=headersUdemy)
    response = request.content.decode('utf8')
    pathCursos = pathCursos+response

@app.route("/cursos", methods=['GET', 'POST'])
def UdemyCursos():
    return pathCursos

if __name__ == "__main__":
    app.run()