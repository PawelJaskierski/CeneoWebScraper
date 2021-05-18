from typing_extensions import ParamSpecArgs
import requests
from bs4 import BeautifulSoup
from app.utils import get_component
class Product():
    def __init__(self,product_id,product_name = None,opinions = [],
    opinions_count=None,pros_count=None,cons_count=None,average_score=None):
        self.product_id = product_id
        self.product_name = product_name
        self.opinions = opinions
        self.opinons_count = opinions_count
        self.pros_count = pros_count
        self.cons_count = cons_count
        self.average_score = average_score
    
    def extract_opinions(self):
        page = 1
        while True:
            respons = requests.get(f"https://www.ceneo.pl/{self.product_id}/opinie-{page}", allow_redirects=False)
            if respons.status_code==200:
                page_dom = BeautifulSoup(respons.text,'html.parser')
                opinions = page_dom.select("div.js_product-review")
                
                for opinion in opinions:
                    single_opinion={key:get_component(opinion,*value)
                                    for key,value in selectors.items()
                    }
                    
                    single_opinion["uselessness"]=int(single_opinion["uselessness"])
                    single_opinion["usefulness"]=int(single_opinion["usefulness"])
                    single_opinion["verified"]=bool(single_opinion["verified"])
                    single_opinion["recomendation"] = True if single_opinion["recomendation"]=="Polecam" else False if single_opinion["recomendation"] == "Nie polecam" else None
                    single_opinion["stars"] = float(single_opinion["stars"].split("/")[0].replace(",","."))
                    single_opinion["content"] = re.sub("\\s"," ",single_opinion["content"])
                    self.opinions.append(single_opinion)
                page +=1
            else: break
    def load_opinions(self):
        pass
    def analyse(self):
        pass
    def get_pie(self):
        pass
    def get_bar(self):
        pass
    def save_csv(self):
        pass
    def save_xlsx(self):
        pass
    def save_json(self):
        pass
    def __dict__(self):
        pass
    #reprezentacja słownikowa
    def __str__(self):
        pass
    def __repr__(self):
        pass
class Opinion():
    selectors={
    "author":["span.user-post__author-name"],
    "recomendation":["span.user-post__author-recomendation > em"],
    "stars":["span.user-post__score-count"],
    "content":["div.user-post__text"],
    "pros":["div.review-feature__col:has(> div[class$=\"positives\"]) > div.review-feature__item", None, True],
    "cons":["div.review-feature__col:has(> div[class$=\"negatives\"]) > div.review-feature__item", None,True],
    "verified":["div.review-pz"],
    "post_date":["span.user-post__published > time:nth-child(1)","datetime", None],
    "purchase_date":["span.user-post__published > time:nth-child(2)","datetime", None],
    "usefulness":["span[id^=\"votes-yes\"]"],
    "uselessness":["span[id^=\"votes-no\"]"]
}
    def __init__(self,opinion_id=None,author=None,recommendation=None,stars=None,verified=None,post_date=None,
    purchase_date=None,usefulness=None,uselessness=None,pros=None,cons=None) -> None:
        self.opinon_id = opinion_id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.verfified = verified
        self.post_date = post_date
        self.purchase_date = purchase_date
        self.usefulness = usefulness
        self.uselessness = uselessness
        self.pros = pros
        self.cons = cons
    def extract_components(self):
        pass
    def __dict__(self):
        pass
    #reprezentacja słownikowa
    def __str__(self):
        pass
    def __repr__(self):
        pass
