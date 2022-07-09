import random
kelimeler = ["ailə", "ailəli", "əzab", "əzbərləmək", "əzgil",
             "əziyyət", "əziz", "əzizləmək","əzmək","əzələ", "əzəmət",     
             "əzəmətli", "əş", "sus", "susmaq", "istedad", "istefa","istehlak",  
             "istehsal", "Gələcək", "Əsəbləşmək", "Yemək", "Gecə", "Səhər", 
             ]


def kelime_sec():
    return random.choice(kelimeler)
