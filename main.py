import requests
from bs4 import BeautifulSoup as bs
import csv

# Constants
BASE_URL = "https://oneonco.co.id/direktori-dokter"
TIMEOUT = 30
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

# Function to extract and clean text from an element
def extract_text(element):
    return element.text.strip() if element else ''

def fetch_doctor_details(url, session):
    doctor_data = {
        'Nama': '',
        'URL': url,
        'Spesialisasi': '',
        'Subspesialisasi': '',
        'RS': '',
        'Alamat': '',
        'Jadwal': '',
        'Map': '',
        'Telepon': '',
        'Website': '',
        'Detail': '',
    }

    html = session.get(url, timeout=TIMEOUT, headers=HEADERS).content
    soup = bs(html, 'html.parser')

    doctor_data['Nama'] = extract_text(soup.find('h1'))
    
    spes_subspes = soup.find_all('span', class_='ml-2')
    if len(spes_subspes) >= 2:
        doctor_data['Spesialisasi'] = extract_text(spes_subspes[0])
        doctor_data['Subspesialisasi'] = extract_text(spes_subspes[1])

    doctor_data['RS'] = extract_text(soup.find('h4'))

    ul_element = soup.find('ul', class_='flex-grow-1 px-3')
    if ul_element:
        items = ul_element.find_all('li')
        if len(items) >= 2:
            doctor_data['Alamat'], doctor_data['Jadwal'] = [extract_text(item).split(':')[1].strip() for item in items]

    rs_details = soup.find('div', class_='card-body d-flex flex-column')
    if rs_details:
        links = rs_details.find_all('a', href=True)
        if len(links) >= 4:
            doctor_data['Map'], doctor_data['Telepon'], doctor_data['Website'], doctor_data['Detail'] = [link['href'].strip() for link in links]

    return doctor_data

def main():
    session = requests.Session()
    html = session.get(BASE_URL, timeout=TIMEOUT, headers=HEADERS).content
    soup = bs(html, 'html.parser')
    last_page_num = int(soup.find_all('li', class_='page-item')[-2].text)

    with open('data_dokter_oneonco.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Nama', 'URL', 'Spesialisasi', 'Subspesialisasi', 'RS', 'Alamat', 'Jadwal', 'Map', 'Telepon', 'Website', 'Detail'])
        writer.writeheader()

        for i in range(1, last_page_num + 1):
            url = f"https://oneonco.co.id/direktori-dokter?page={i}"
            html = session.get(url, timeout=TIMEOUT, headers=HEADERS).content
            soup = bs(html, 'html.parser')

            for row in soup.find('div', class_='row listDokter').find_all('div', class_='col-12 col-lg-6 d-flex'):
                url_ = row.find('a', href=True)['href']
                doctor_data = fetch_doctor_details(url_, session)
                writer.writerow(doctor_data)
                f.flush()

if __name__ == '__main__':
    main()
