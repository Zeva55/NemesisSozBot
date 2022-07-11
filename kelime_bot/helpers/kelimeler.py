import random
kelimeler = ["ailə", "ailəli", "əzab", "əzbərləmək", "əzgil",
             "əziyyət", "əziz", "əzizləmək", "əzmək", "əzələ", "əzəmət",     
             "əzəmətli", "iş", "sus", "susmaq", "istedad", "istefa","istehlak",  
             "istehsal", "gələcək", "əsəbləşmək", "yemək", "gecə", "səhər", "ölmək",
             "ayılmaq", "ayrılmaq", "sözsüz", "xonça", "əvəzedilməz", "ömür", "səbrsiz"
             'kəlmə', 'sual', 'əmr', 'radyo', 'götürmək', 'sərhəd', 'sərhədsiz', 'üzülmək',   
             'darıxmaq', 'külək', 'sənəd', 'sümük', 'sahibsiz', 'vətən', 'əməliyyat', 'əziyyət',  
             'söyüş', 'meyxana', 'istəmək', 'danışmaq', 'gülmək', 'azərbaycanlı', 'namaz', 'görüşmək',  
             'mahnı', 'restoran', 'riyaziyyat', 'səhvsiz', 'səməni', 'həyat', 'küçələr', 'yerimək', 'televizor', 
             ]


def kelime_sec():
    return random.choice(kelimeler)
