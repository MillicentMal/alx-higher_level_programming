#!/usr/bin/python3


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    new_string = []
    delimiters = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for i in text:
            new_string.append(i)
            if i in delimiters:
                print(''.join(new_string))
                print()
                print()
                new_string.clear()


text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
