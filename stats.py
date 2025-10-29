def count_words(book_content):
    words = book_content.split()
    return len(words)

def char_counter(book_content):
    book_content_lower = book_content.lower()
    char_dict ={}
    char_counter = 0

    for char in book_content_lower:
        if char in char_dict:
            char_dict[char] += 1 
        else:
            char_dict[char] = 1
    
    return char_dict

def get_char_count(dicter):
    return dicter[1]["num"]

def sorted_char_dict(char_dict):
    sorted_list=[]

    for key in char_dict:
        chars={}
        numbers={}
        dummy_list=[]

        chars["char"] = key
        numbers["num"] = char_dict[key]

        dummy_list =[chars,numbers]
        sorted_list.append(dummy_list)

    sorted_list.sort(reverse=True, key=get_char_count)
    return sorted_list
   