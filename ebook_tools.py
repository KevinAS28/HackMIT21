import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re
import copy

def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters

blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script',   ]
# there may be more elements you don't want, such as "style", etc.

def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output

def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    return ttext

def split_paragrahps(text_list):

    paragraphs = []
    for text in text_list:
        paragraphs.extend(re.split('. \n ', text))
    return paragraphs

def isparagraph(text: str):
    return True if text.count('\n') >= 3 else False

def paragraphs_for_emotion_analysis(paragraph_list):
    
    if len(paragraph_list) <= 3:
        return paragraph_list
    else:
        real_paragraphs = []
        temp = []
        real_temp = 0
        for p in paragraph_list:
            if not isparagraph(p):
                temp.append(p)
            else:
                if real_temp >= 2:
                    real_paragraphs.append(copy.deepcopy(temp))
                    real_temp = 0
                    temp = []

                temp.append(p)
                real_temp += 1
        return real_paragraphs

def epub2pea(epub_path='0.epub'):
    out=epub2text(epub_path)
    all_chapters = [i for i in out if len(i)>=5000]
    chapters_result = []
    for chapter in all_chapters:
        paragraphs = re.split(r'(\n(\s)){2,}', chapter)
        paragraphs = [i for i in paragraphs if len(i) > 25]
        paragraph_list = split_paragrahps(paragraphs)
        pfea = paragraphs_for_emotion_analysis(paragraph_list)
        chapters_result.append(pfea)
    
    return chapters_result

if __name__=='__main__':
    results = epub2pea()
    for chapter in results[:3]:
        for paragraph in chapter:
            print(paragraph)
            print('+'*10)
        print('=='*10,'\n')
    print()