# Caption scraper and parser. Run before building the graph.

import spacy
import re

def cleaned_captions(captions):
    name_cleaned1 = []
    count = 0
    for names in captions:
        name_no_space =  ' '.join(names.split())#names.lstrip()
        name_cleaned1.append(name_no_space)

    filtered_list = []
    count = 0
    for _ in name_cleaned1:
        r1 = re.sub(r'[\|]|([A-Z]{2,})|(-ing)|(board member)|(board)|(chairman)|(family)|(\d)|(Right)|(Left)',' ',_)
        del_word_list = ['his','her','friend','Gala','opening','here','of','dinner']
        delimiters = [r"\s+with\s+",",","\|","\n","Dr. ","Jr. ","Mayor","President","Dr "\
                      "Gala Honorary Chairman","Executive Producer","Chairman","Governor",\
                     "Chief","Director","Consul General","President",\
                    "General","Chair","Lady","Consul General","Caption",\
                    "Princess","Prince","Director\/Writer\s+","Chef ","Sir ","Ambassador","Mrs. ",\
                     "at Plum Hamptons magazine's a Literary Evening"]
        regex = "|".join(delimiters)
        filtered= re.split(regex,r1)
        filtered_list.append(filtered)

    for i in range(len(filtered_list)):
        aa = []
        for j in range(len(filtered_list[i])):
            raw_name = filtered_list[i][j].split()
            if len(raw_name)>1 and len(raw_name)<9 and (not any(x.lower() in del_word_list for x in raw_name))\
                and raw_name[0][0].isupper() and (not 'and' in raw_name):
                aa.append(' '.join(raw_name))
                count +=1
            elif len(raw_name)>1 and str(raw_name[0]) == 'and'and (not any(x.lower() in del_word_list for x in raw_name)):
                aa.append(' '.join(raw_name[1:]))
                count +=1
            elif len(raw_name)>3 and len(raw_name)<8 and (not any(x.lower() in del_word_list for x in raw_name))\
                and raw_name[0][0].isupper():
                index_and = raw_name.index('and')
                if index_and !=1:
                    aa.append(' '.join(raw_name[0:index_and]))
                    count +=1
                    if len(raw_name[index_and+1:])>1 and (not any(x.lower() in del_word_list for x in raw_name)):
                        aa.append(' '.join(raw_name[index_and+1:]))
                        count +=1
                if index_and == 1:
                    aa.append(' '.join([raw_name[0],raw_name[-1]]))
                    aa.append(' '.join(raw_name[index_and+1:]))
                    count +=2
        filtered_list[i] = aa
    final_caption_list = [x for x in filtered_list if x]
    return [final_caption_list,count]

# Get cleaned captions
cleaned_captions_whole=[]
count = 0
num_names_total = 0
for url in link_url_all:
    captions_one_link=[]
    cleaned_captions_one_link=[]
    try:
        captions_one_link = get_captions(url)
        if captions_one_link:
            cleaned_captions_one_link,num_names_one_link= cleaned_captions(captions_one_link)
            num_names_total += num_names_one_link
            count += len(cleaned_captions_one_link)
            print('current link index: {}'.format(link_url_all.index(url)))
            cleaned_captions_whole.append(cleaned_captions_one_link)
            print('total numbers of captions: {}'.format(count))
            print('total numbers of names: {}'.format(num_names_total))
    except Exception as e:
        print(e) # for the repr
        print(str(e)) # for just the message
        print(e.args)

# Get connection subset. Saved to pandas df.
import pandas as pd

subset_whole=[]
for j in range(len(cleaned_captions_whole)):
    for i in range(len(cleaned_captions_whole[j])):
        if len(cleaned_captions_whole[j][i])>1:
            subset_sigle_caption = find_subset(cleaned_captions_whole[j][i])
            subset_whole.append(subset_sigle_caption)

df_subset_whole = pd.DataFrame()
for i in range(len(subset_whole)):
    df_subset = pd.DataFrame(subset_whole[i],columns=['node1','node2'])
    df_subset_whole= df_subset_whole.append(df_subset,ignore_index=True)
df_subset_whole.to_csv('edges', encoding='utf-8')
