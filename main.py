import requests
from bs4 import BeautifulSoup
import json

unable_to_read = []


# URL of the webpage
category_urls_list = [
    {"page_count":8, "link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/iman"},
    {"page_count":25,"link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/allahcc"},
    {"page_count":25,"link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/hz-muhammed-asm"},
    {"page_count":19,"link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/peygamberler"},
    {"page_count":64,"link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/kuran"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/kutsal-kitaplar"},
    {"page_count":22,"link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/olum-ve-sonrasi"},
    {"page_count":10,"link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/kader"},
    {"page_count":7,"link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/melekler"},
    {"page_count":9,"link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/hidayet-dalalet"},
    {"page_count":5,"link":"https://sorularlaislamiyet.com/kategoriler/iman-esaslari/kufur"},
    {"page_count":9,"link":"https://sorularlaislamiyet.com/kategoriler/islam/islam-ve-diger-dinler"},
    {"page_count":8,"link":"https://sorularlaislamiyet.com/kategoriler/islam/vatan-devlet-millet"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/islam/cami-ve-mescid"},
    {"page_count":14,"link":"https://sorularlaislamiyet.com/kategoriler/islam/sahabeler"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/islam/takva"},
    {"page_count":12,"link":"https://sorularlaislamiyet.com/kategoriler/islam/ilim"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/islam/irkcilik"},
    {"page_count":4,"link":"https://sorularlaislamiyet.com/kategoriler/islam/hayat"},
    {"page_count":8,"link":"https://sorularlaislamiyet.com/kategoriler/islam/tasavvuf-ve-tarikat"},
    {"page_count":17,"link":"https://sorularlaislamiyet.com/kategoriler/islam/islam-tarihi"},
    {"page_count":14,"link":"https://sorularlaislamiyet.com/kategoriler/islam/ahlak"},
    {"page_count":20,"link":"https://sorularlaislamiyet.com/kategoriler/islam/aile"},
    {"page_count":13,"link":"https://sorularlaislamiyet.com/kategoriler/islam/ibadet"},
    {"page_count":6,"link":"https://sorularlaislamiyet.com/kategoriler/islam/mezhep-ve-mesrepler"},
    {"page_count":8,"link":"https://sorularlaislamiyet.com/kategoriler/islam/cihad"},
    {"page_count":6,"link":"https://sorularlaislamiyet.com/kategoriler/islam/gunah"},
    {"page_count":6,"link":"https://sorularlaislamiyet.com/kategoriler/islam/tesettur-turban-ortunme"},
    {"page_count":1,"link":"https://sorularlaislamiyet.com/kategoriler/islam/ehl-i-beyt"},
    {"page_count":73,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/namaz"},
    {"page_count":17,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/ramazan-oruc"},
    {"page_count":10,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/zekat"},
    {"page_count":9,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/hacc-umre"},
    {"page_count":21,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/ticaret"},
    {"page_count":6,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/adak-kurban"},
    {"page_count":6,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/faiz"},
    {"page_count":34,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/helaleller-haramlar"},
    {"page_count":21,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/kadin"},
    {"page_count":6,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/ictihad"},
    {"page_count":14,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/evlilik-nikah"}
    {"page_count":12,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/abdest-gusul-teyemmum"},    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/miras"},
    {"page_count":8,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/kul-hakki"},
    {"page_count":4,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/bosanma-talak"},
    {"page_count":5,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/eglence-oyun"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/yemin-kefaret"},
    {"page_count":1,"link":"https://sorularlaislamiyet.com/kategoriler/fikih/kumar-ve-sans-oyunlari"},
    {"page_count":4,"link":"https://sorularlaislamiyet.com/kategoriler/metafizik/ruhlar"},
    {"page_count":3,"link":"https://sorularlaislamiyet.com/kategoriler/metafizik/gayb"},
    {"page_count":4,"link":"https://sorularlaislamiyet.com/kategoriler/metafizik/buyu-fal-kehanet"},
    {"page_count":7,"link":"https://sorularlaislamiyet.com/kategoriler/metafizik/cinler"},
    {"page_count":7,"link":"https://sorularlaislamiyet.com/kategoriler/metafizik/seytan"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/metafizik/vesvese"},
    {"page_count":21,"link":"https://sorularlaislamiyet.com/kategoriler/metafizik/dua"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/metafizik/ilham-vahiy"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/metafizik/mucize-peygamberlerin-mucizeler"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/metafizik/ruya-istihare-tefeul"},
    {"page_count":5,"link":"https://sorularlaislamiyet.com/kategoriler/yaratilis/kainat"},
    {"page_count":9,"link":"https://sorularlaislamiyet.com/kategoriler/yaratilis/evrim"},
    {"page_count":12,"link":"https://sorularlaislamiyet.com/kategoriler/yaratilis/ilim-bilim-teknoloji"},
    {"page_count":3,"link":"https://sorularlaislamiyet.com/kategoriler/yaratilis/sebepler"},
    {"page_count":3,"link":"https://sorularlaislamiyet.com/kategoriler/insan/insan-haklari"},
    {"page_count":11,"link":"https://sorularlaislamiyet.com/kategoriler/insan/duygular"},
    {"page_count":9,"link":"https://sorularlaislamiyet.com/kategoriler/insan/hayat"},
    {"page_count":8,"link":"https://sorularlaislamiyet.com/kategoriler/insan/mahrem-konular"},
    {"page_count":8,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/ahir-zaman"},
    {"page_count":4,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/felsefe"},
    {"page_count":4,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/islamin-tebligi"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/muzik-ve-ilahi"},
    {"page_count":1,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/hurriyet"},
    {"page_count":7,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/bela-ve-musibetler"},
    {"page_count":4,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/dunya"},
    {"page_count":1,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/zaman"},
    {"page_count":8,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/adalet"},
    {"page_count":5,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/hayvanlar"},
    {"page_count":2,"link":"https://sorularlaislamiyet.com/kategoriler/muhtelif/kategorisizler"}
]


def get_content(url):
    global unable_to_read
    # Fetch the webpage content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        unable_to_read.append(url)
        question = "Failed to retrieve"
        answer = "Failed to retrieve"
        return question, answer
    else:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the script tag (adjust the selector as needed)
        script_tag = soup.find('script', string=lambda t: t and 'description' in t)

        if script_tag:
            # Extract the script content
            script_content = script_tag.string

            # Here, you might need to parse or clean the script_content 
            # to properly format it as JSON. This depends on how the data is structured in the script tag.

            # Load JSON data
            data = json.loads(script_content)

            # Extract description and article_body
            question = data['headline']
            answer = data['articleBody']
            unable_to_read = []
            if question != None and answer != None:
                print(url)
                return question, answer
            else:
                print("none item")
                unable_to_read.append(url)
                question = "Unable to get"
                answer = "Unable to get"
                return question, answer
        else:
            unable_to_read.append(url)
            question = "Unable to get"
            answer = "Unable to get"
            return question, answer

# Base URL of the webpage

# Function to fetch and parse a single page
def fetch_links_from_page(base_url,page_num):
    # Construct the URL for the current page
    url = f"{base_url}?page={page_num}"

    # Fetch the webpage content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}. Status code: {response.status_code}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all h3 tags with class 'field-content' and extract hrefs
    links = []
    for h3 in soup.find_all('h3', class_='field-content'):
        a_tag = h3.find('a')
        if a_tag and 'href' in a_tag.attrs:
            links.append(a_tag['href'])

    return links

def get_links_from_category(cat_url, cat_page_count):
    # List to store all the links
    cat_links = []

    # Loop through pages 0 to 8
    for page_num in range(cat_page_count):
        links = fetch_links_from_page(cat_url,page_num)
        cat_links.extend(links)
    
    return cat_links

def cat_crawler(cat_url, cat_page_count):
    link_list= []
    link_list = get_links_from_category(cat_url,cat_page_count)
    return link_list

def main():
    global category_urls_list, unable_to_read
    all_links = []
    for cat in category_urls_list:
        for item in cat_crawler(cat["link"],cat["page_count"]-1):
            all_links.append(item)
    for link in all_links:
        que, ans = get_content(f"https://sorularlaislamiyet.com{link}")
        print(f"Question: {que}  \n Answer: {ans}  \n")

    print(f"Unable to read links are as follows:\n {unable_to_read} ")
main()