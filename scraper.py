from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

class Oseba:
    def __init__(self, name, surname, gender, age, city, email):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.city = city
        self.email = email



MAIN_URL = "https://scrapebook22.appspot.com/"

webpage = urlopen(MAIN_URL).read()

nice_webpage = BeautifulSoup(webpage)


#print nice_webpage.html.head.title.string


osebe = []

linki = nice_webpage.findAll("a")

for link in linki:
    if link.string == "See full profile":
        personal_page = BeautifulSoup(urlopen(MAIN_URL + link["href"]).read())

        personal_name = personal_page.findAll("h1")[-1].string
        name, surname =  personal_name.split(" ")
        print surname + "; " + name

        #<li>Gender: <span data-gender="male">male</span></li>
        personal_gender = personal_page.find("span", attrs={"data-gender": True}).string
        print personal_gender

        personal_age = personal_page('li')[1].string[5:]
        print personal_age

        personal_city = personal_page.find("span", attrs={"data-city": True}).string
        print personal_city

        personal_email = personal_page.find("span", {"class": "email"}).string
        print personal_email

        person = Oseba(name, surname, personal_gender, personal_age, personal_city, personal_email)

        osebe.append(person)

print osebe

csv_file = open("osebe.csv", "w")

for person in osebe:
    csv_file.write(person.name + ", " + person.surname + ", " + person.gender + ", " + person.age + ", " + person.city + ", " + person.email + "\n")

csv_file.close()


