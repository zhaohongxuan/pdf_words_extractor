from pdfminer.high_level import extract_text
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
import os
import re
import pandas as pd
from file_utils import read_file_to_list, read_csv_to_map

GRE_words = read_file_to_list('./corpus/vocabulary/WordList_GRE.txt')
TOEFL_words = read_file_to_list('./corpus/vocabulary/WordList_TOEFL.txt')
IELTS_words = read_file_to_list('./corpus/vocabulary/IELTS.txt')
dictionary = read_csv_to_map('./corpus/dictionary/English_to_Chiness_Dict.csv')

def parse_word_in_page(pdf_file):
    text = extract_text(pdf_file=pdf_file)
    tokenizer = RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(text)
    filtered_tokens = list(
        filter(lambda x: not bool(re.search(r'\d', x)), tokens))
    
    fdist = FreqDist(filtered_tokens)

    token_set = list(set(filtered_tokens))
    return token_set,fdist

def get_word_level(word):
    levels = []
    if word in GRE_words:
        levels.append("GRE")
    if word in TOEFL_words:
        levels.append("TOEFL")
    if word in IELTS_words:
        levels.append("IELTS")
    return levels

def main(pdf_file):
    word_set,fdist = parse_word_in_page(pdf_file)
    excel_word_list = []
    excel_level_list = []
    excel_zhword_list = []
    excel_fq_list = []

    for word in word_set:
        levels = ",".join(get_word_level(word))
        if levels:
            zh_word = dictionary.get(word, "Not Found")
            freq = fdist[word]
            line = f"{word}\t{levels}\t{freq}\t{zh_word}"
            print(line)
            excel_word_list.append(word)
            excel_level_list.append(levels)
            excel_zhword_list.append(zh_word)
            excel_fq_list.append(freq)
    df = pd.DataFrame(
        {'word': excel_word_list,'freq':excel_fq_list, 'levels': excel_level_list, 'zh': excel_zhword_list})
    file_name = os.path.splitext(os.path.basename(pdf_file))[0]
    output_file_name= "hard_words_for_"+ file_name
    df.to_excel(f'./result/{output_file_name}.xlsx', index=False)


if __name__ == "__main__":
    # pdf_file = './example/java-aqs.pdf'
    pdf_file ='~/Python-for-MATLAB-Development.pdf'
    expand_pdf_file_path = os.path.expanduser(pdf_file)
    main(expand_pdf_file_path)