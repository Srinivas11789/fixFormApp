import requests,time
#r = requests.get('http://172.30.2.33:8080/getData')
#print r.status_code
#print r.json()
r = requests.get('http://172.30.2.33:8080/sessionCreate?sType=squat')
print r.status_code
#print r.json()
time.sleep(10)
r = requests.get('http://172.30.2.33:8080/getData')
print r.status_code
#print r.content
print r.json()
#r = requests.get('http://172.30.2.33:8080/sessionClose')
#print r.status_code
#print r.json()
r = requests.get('http://172.30.2.33:8080/getbackcurvature')
print r.status_code
print r.json()
r = requests.get('http://172.30.2.33:8080/getAllData')
print r.status_code
#print r.content
print r.json()


