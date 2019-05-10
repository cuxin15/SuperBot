from chatterbot.preprocessors import clean_whitespace
from chatterbot.conversation import Statement


def Crush(statement):
    '''
    ``statement``: Statement Object
    Lọc số ra khỏi ``statement.text`` trả về một statement.text ``lower()``
    '''
    statement = clean_whitespace(statement)
    split_statement = statement.text.split()
    dict_word_need_remove = {}  # key: word's index in split_statement, value: word
    for i in split_statement:
        if i.isalpha() == False:
            dict_word_need_remove[split_statement.index(i)] = i
        # remove characters is not alpha
    for key in dict_word_need_remove:
        word = dict_word_need_remove[key]
        new_word = ''
        list_word = list(word)
        list_token_need_remove = []
        for token in list_word:
            if token.isalpha() == False:
                list_token_need_remove.append(token)
        for w in list_token_need_remove:
            list_word.remove(w)
        for join in list_word:
            new_word += join
        dict_word_need_remove[key] = new_word
        # add them into split_statement
    for key in dict_word_need_remove:
        split_statement[key] = dict_word_need_remove[key]
    text = ' '.join(split_statement)
    return Statement(text.lower())


# print(TuXamXi(Statement('1Em 2tên g4ì')))
