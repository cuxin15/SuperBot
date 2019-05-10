from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import random
from chatterbot.conversation import Statement
from funtion_all import intersection, have


class AnComChua(LogicAdapter):
    '''Trả lời cho câu hỏi ``một ai đó làm gì đó chưa?``
    Ví dụ: ``Bạn ăn cơm chưa``-->``Tôi ăn cơm rồi``
    Mặc định trả về ``confidence:`` 0.95'''

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.default_responses = [
            '?'
        ]

    def can_process(self, statement):
        if ('chưa' in statement.text.split()) and (len(statement.text.split()) > 2):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters=None):

        list_S = ('bạn', 'cậu', 'mày')
        S = {'bạn': 'mình', 'cậu': 'tớ', 'mày': 'tao'}
        #V = ('đi','học','ăn','ngủ','làm','nghỉ','uống')

        # Preprocessing
        statement_split = input_statement.text.split()

        if (statement_split[0] in S) or (statement_split[len(statement_split)-1] in S):

            # Phép hỏi đầy đủ có chủ ngữ: Em ăn cơm chưa em?
            if (statement_split.count(statement_split[0]) >= 1) or (statement_split.count(statement_split[len(statement_split)-1]) >= 1):
                P = intersection(list_S, statement_split)[0]
                visual = list(statement_split)
                # Remove P and get verb
                if visual[0] in S:
                    visual.remove(visual[0])
                while 'chưa' != visual[len(visual)-1]:
                    visual.remove(visual[len(visual)-1])
                visual.remove('chưa')
                verb_full = ' '.join(visual)
                verb = visual[0]
                # Join string
                rep_1 = '{0} {1} rồi nha {2}'.format(S[P], verb_full, P)
                rep_2 = '{0} {1} rồi nha {2}'.format(S[P], verb, P)
                rep_3 = '{0} chưa {1} nha {2}'.format(S[P], verb_full, P)
                rep_4 = '{0} chưa {1} nha {2}'.format(S[P], verb, P)
                rep_5 = '{0} chưa {1}'.format(S[P], verb_full)
                rep_6 = '{0} chưa {1}'.format(S[P], verb)
                seq = (rep_1, rep_2, rep_3, rep_4, rep_5, rep_6)
                return Statement(random.choice(seq), confidence=1)

        # Hỏi trống trơn, không có chủ ngữ: Ăn cơm chưa?
        if have(statement_split, list_S) == False:
            visual = list(statement_split)
            # reomve chưa and get verb
            visual.remove('chưa')
            # get full verb and verb
            verb_full = ' '.join(visual)
            verb = visual[0]
        # Join string
            rep_1 = '{0} rồi'.format(verb_full)
            rep_2 = '{0} rồi'.format(verb)
            rep_3 = 'chưa {0}'.format(verb_full)
            rep_4 = 'chưa {0}'.format(verb)
            seq = (rep_1, rep_2, rep_3, rep_4)
            return Statement(random.choice(seq), confidence=1)
