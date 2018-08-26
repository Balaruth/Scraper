from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

# open or create CSV file
csv_file = open("email_list.csv", "w")

url = 'https://scrapebook22.appspot.com'
response = urlopen(url).read()
soup = BeautifulSoup(response)

print soup.html.head.title.string

for link in soup.findAll("a"): # find all anchor tags
    if link.string == "See full profile": # only include anchors with the string "See full profile"
        person_url = "https://scrapebook22.appspot.com" + link["href"] # generate the full links
        person_html = urlopen(person_url).read() # read the content of the full links
        person_soup = BeautifulSoup(person_html)
        name = person_soup.find("div", attrs={"class": "col-md-8"}).h1.string
        email = person_soup.find("span", attrs={"class": "email"}).string
        city = person_soup.find("span", attrs={"data-city": True}).string
        csv_file.write("%s, %s, %s \n" % (name, email, city))  # \n will create a new line

# close CSV file
csv_file.close()