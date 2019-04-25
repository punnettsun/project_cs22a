from bs4 import BeautifulSoup as bs
import requests
import csv


url = 'http://pages.mtu.edu/~suits/notefreqs.html'
r = requests.get(url)

soup = bs(r.text, 'html.parser')
table = soup.select('center center table')[0]
rows = table.select('tr')

fieldnames = ['note', 'frequency', 'wavelength']

with open('./note_frequency.csv', mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
        note = row.td.text.strip().split('/')[0]
        frequency = row.select('td')[1].text.strip()
        wavelength = row.select('td')[2].text.strip()
        writer.writerow({'note': note, 'frequency': frequency, 'wavelength': wavelength})
