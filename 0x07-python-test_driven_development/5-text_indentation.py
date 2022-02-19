#!/usr/bin/python3
"""
text Indentation
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    # stringList = []
    start = 0
    delimiters = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
    #     for string in text:
    #         if string in delimiters:
    #             stringList.append(string + '\n\n')
    #         else:
    #             stringList.append(string.lstrip().rstrip())
    
    #     stringList = ''.join(stringList)
    # print(stringList)
        for i in range(len(text)) and i + 1 <:
            if text[i] in delimiters:
                print(text[start:i+1].rstrip()+'\n\n')
                start =  i
                text = text[i:]
            else:
                print(text[start:i+1].rstrip())
                
text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")





