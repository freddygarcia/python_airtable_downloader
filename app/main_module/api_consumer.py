import requests
import json

questions = {
    'success': True,
    'code': 200,
    'content': [
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec6bnuwjmSfM9vi2"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Quisque bibendum orci vel elit scelerisque tristique.",
                    "option_a": "Cras volutpat sem a ultrices viverra.",
                    "option_b": "Etiam dapibus lectus hendrerit enim aliquam, vel pretium magna laoreet.",
                    "option_c": "Quisque bibendum orci vel elit scelerisque tristique.",
                    "option_d": "Phasellus consequat neque et placerat condimentum.",
                    "question_id": 1725,
                    "question_text": "Fusce pharetra mi ac libero tincidunt commodo.",
                    "status": "Approved",
                    "tell_me_more": [
                        "At the same time as defending Britain, the British military was fighting the Axis on many other fronts. In Singapore, the Japanese defeated the British and then occupied Burma, threatening India. The United States entered the war when the Japanese bombed its naval base at Pearl Harbour in December 1941."
                    ]
                },
                "id": "rec03gaeD5bLjHUXa"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recqbxAfAYLZ8ZPH5"
                    ],
                    "correct_answer": [
                        "B",
                        "D"
                    ],
                    "feedback": "Suspendisse aliquet arcu ac quam mollis pulvinar.",
                    "option_a": "Proin ullamcorper velit eget blandit feugiat.",
                    "option_b": "Mauris eu sapien sit amet erat tincidunt ullamcorper.",
                    "option_c": "Suspendisse aliquet arcu ac quam mollis pulvinar.",
                    "option_d": "In viverra nulla nec purus interdum aliquet vitae eu lorem.",
                    "question_id": 1955,
                    "question_text": "Donec vehicula nulla quis erat mattis aliquet.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The Union Flag\n Although Ireland had had the same monarch as England and Wales since Henry VIII, it had remained a separate country. In 1801, Ireland became unified with England, Scotland and Wales after the Act of Union of 1800. This created the United Kingdom of Great Britain and Ireland. One symbol of this union between England, Scotland, Wales and Ireland was a new version of the official flag, the Union Flag. This is often called the Union Jack. The flag combined crosses associated with England, Scotland and Ireland. It is still used today as the official flag of the UK.\n The Union Flag consists of three crosses:\n - The cross of St George, patron saint of England, is a red cross on a white ground.\n - The cross of St Andrew, patron saint of Scotland, is a diagonal white cross on a blue ground.\n - The cross of St Patrick, patron saint of Ireland, is a diagonal red cross on a white ground.\n The Union Flag, also known as the Union Jack"
                    ]
                },
                "id": "rec06i3CJF5QEZs0o"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recqbxAfAYLZ8ZPH5"
                    ],
                    "correct_answer": [
                        "B",
                        "D"
                    ],
                    "feedback": "Praesent a eros vitae ligula fringilla fringilla.",
                    "option_a": "Duis vehicula mauris a justo interdum, vitae sodales quam lobortis.",
                    "option_b": "Nulla eu arcu scelerisque, egestas enim egestas, pellentesque dui.",
                    "option_c": "Praesent a eros vitae ligula fringilla fringilla.",
                    "option_d": "Mauris feugiat lorem id diam convallis, efficitur blandit nibh tempor.",
                    "question_id": 2137,
                    "question_text": "Phasellus aliquam arcu vitae enim lacinia scelerisque.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The Union Flag\n Although Ireland had had the same monarch as England and Wales since Henry VIII, it had remained a separate country. In 1801, Ireland became unified with England, Scotland and Wales after the Act of Union of 1800. This created the United Kingdom of Great Britain and Ireland. One symbol of this union between England, Scotland, Wales and Ireland was a new version of the official flag, the Union Flag. This is often called the Union Jack. The flag combined crosses associated with England, Scotland and Ireland. It is still used today as the official flag of the UK.\n The Union Flag consists of three crosses:\n - The cross of St George, patron saint of England, is a red cross on a white ground.\n - The cross of St Andrew, patron saint of Scotland, is a diagonal white cross on a blue ground.\n - The cross of St Patrick, patron saint of Ireland, is a diagonal red cross on a white ground.\n The Union Flag, also known as the Union Jack"
                    ]
                },
                "id": "rec0Iamaf0PT1GcZd"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recWEwUTqv82HNzK2"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Donec convallis metus non odio ullamcorper, vitae venenatis arcu lacinia.",
                    "option_a": "Morbi cursus nisi consectetur gravida mollis.",
                    "option_b": "Cras in eros vehicula, aliquet dolor sed, egestas lectus.",
                    "option_c": "Donec convallis metus non odio ullamcorper, vitae venenatis arcu lacinia.",
                    "option_d": "Suspendisse quis augue euismod, sollicitudin lorem at, blandit urna.",
                    "question_id": 1998,
                    "question_text": "Praesent elementum erat ac massa lobortis tincidunt eu a augue.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Notable British artists\n Thomas Gainsborough (1727\u201a\u00c4\u00ec88) was a portrait painter who often painted people in country or garden scenery.\n David Allan (1744\u201a\u00c4\u00ec96) was a Scottish painter who was best known for painting portraits. One of his most famous works is called The Origin of Painting.\n Joseph Turner (1775\u201a\u00c4\u00ec1851) was an influential landscape painter in a modern style. He is considered the artist who raised the profile of landscape painting.\n John Constable (1776\u201a\u00c4\u00ec1837) was a landscape painter most famous for his works of Dedham Vale on the Suffolk-Essex border in the east of England.\n The Pre-Raphaelites were an important group of artists in the second half of the 19th century. They painted detailed pictures on religious or literary themes in bright colours. The group included Holman Hunt, Dante Gabriel Rossetti and Sir John Millais.\n Sir John Lavery (1856\u201a\u00c4\u00ec1941) was a very successful Northern Irish portrait painter. His work included painting the Royal Family.\n Henry Moore (1898\u201a\u00c4\u00ec1986) was an English sculptor and artist. He is best known for his large bronze abstract sculptures."
                    ]
                },
                "id": "rec0S35MVpEQ8MQyg"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recWEwUTqv82HNzK2"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Pellentesque sit amet ipsum ut orci rutrum ultricies.",
                    "option_a": "Etiam pulvinar lacus et mauris imperdiet facilisis.",
                    "option_b": "Ut ac nisl at arcu pulvinar condimentum.",
                    "option_c": "Pellentesque sit amet ipsum ut orci rutrum ultricies.",
                    "option_d": "Vivamus mattis odio ac ligula vulputate, vitae scelerisque tortor egestas.",
                    "question_id": 1972,
                    "question_text": "Nullam sit amet metus aliquam, eleifend erat ac, pulvinar justo.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Notable British artists\n Thomas Gainsborough (1727\u201a\u00c4\u00ec88) was a portrait painter who often painted people in country or garden scenery.\n David Allan (1744\u201a\u00c4\u00ec96) was a Scottish painter who was best known for painting portraits. One of his most famous works is called The Origin of Painting.\n Joseph Turner (1775\u201a\u00c4\u00ec1851) was an influential landscape painter in a modern style. He is considered the artist who raised the profile of landscape painting.\n John Constable (1776\u201a\u00c4\u00ec1837) was a landscape painter most famous for his works of Dedham Vale on the Suffolk-Essex border in the east of England.\n The Pre-Raphaelites were an important group of artists in the second half of the 19th century. They painted detailed pictures on religious or literary themes in bright colours. The group included Holman Hunt, Dante Gabriel Rossetti and Sir John Millais.\n Sir John Lavery (1856\u201a\u00c4\u00ec1941) was a very successful Northern Irish portrait painter. His work included painting the Royal Family.\n Henry Moore (1898\u201a\u00c4\u00ec1986) was an English sculptor and artist. He is best known for his large bronze abstract sculptures."
                    ]
                },
                "id": "rec0Z22EmL64Qpl18"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Vivamus sollicitudin odio quis lacus volutpat efficitur.",
                    "option_a": "Nunc sit amet justo venenatis, interdum lectus at, lacinia quam.",
                    "option_b": "Ut varius lacus ac ante mollis consequat.",
                    "option_c": "Vivamus sollicitudin odio quis lacus volutpat efficitur.",
                    "option_d": "Proin dapibus sapien eget arcu consequat, eget pellentesque sem lacinia.",
                    "question_id": 1964,
                    "question_text": "Phasellus eget felis congue, tristique ante quis, tempus tellus.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "rec0l3WlpwiYBzV3i"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "B"
                    ],
                    "feedback": "Donec quis eros eget augue pretium porta ac quis mi.",
                    "option_a": "Nunc dapibus odio sit amet neque imperdiet condimentum.",
                    "option_b": "Nunc vitae lectus tempor, sollicitudin turpis a, sodales purus.",
                    "option_c": "Donec quis eros eget augue pretium porta ac quis mi.",
                    "option_d": "Quisque vitae diam quis metus tempor fermentum.",
                    "question_id": 1827,
                    "question_text": "Ut non felis vel leo posuere condimentum sit amet vitae mauris.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "rec0sDfjxtOxc05ke"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "B"
                    ],
                    "feedback": "Nam efficitur nunc sed sapien sodales aliquam.",
                    "option_a": "Phasellus ac sem et ex hendrerit imperdiet sed non dolor.",
                    "option_b": "Nunc ornare orci venenatis dolor ornare ultricies.",
                    "option_c": "Nam efficitur nunc sed sapien sodales aliquam.",
                    "option_d": "Integer finibus odio a libero fringilla, sed tempus erat tincidunt.",
                    "question_id": 2204,
                    "question_text": "Donec dapibus diam cursus ornare malesuada.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec0tcWtvWK33IxIJ"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "In viverra nulla nec purus interdum aliquet vitae eu lorem.",
                    "option_a": "Mauris eu sapien sit amet erat tincidunt ullamcorper.",
                    "option_b": "Vivamus sollicitudin odio quis lacus volutpat efficitur.",
                    "option_c": "In viverra nulla nec purus interdum aliquet vitae eu lorem.",
                    "option_d": "Aliquam in purus id mauris volutpat tincidunt nec eget augue.",
                    "question_id": 1960,
                    "question_text": "Proin ullamcorper velit eget blandit feugiat.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec0w3mJcGBsb8BVf"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "B"
                    ],
                    "feedback": "Nam eu leo eget arcu interdum consequat pharetra sit amet est.",
                    "option_a": "Donec molestie erat et condimentum pulvinar.",
                    "option_b": "Etiam rhoncus nunc sit amet dolor condimentum congue at vel ante.",
                    "option_c": "Nam eu leo eget arcu interdum consequat pharetra sit amet est.",
                    "option_d": "Pellentesque id sem ut massa tempor pharetra.",
                    "question_id": 1840,
                    "question_text": "Integer eleifend arcu nec libero tincidunt, a aliquam lectus dignissim.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "rec0yC5EyToE9efvM"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec6bnuwjmSfM9vi2"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Ut vulputate justo at mauris tincidunt, nec convallis metus congue.",
                    "option_a": "Proin gravida urna sed aliquam dictum.",
                    "option_b": "Fusce cursus quam a turpis hendrerit, ut blandit magna viverra.",
                    "option_c": "Ut vulputate justo at mauris tincidunt, nec convallis metus congue.",
                    "option_d": "Nullam porttitor tellus malesuada elementum lacinia.",
                    "question_id": 2028,
                    "question_text": "Nunc et odio lacinia, convallis velit sit amet, aliquam lorem.",
                    "status": "Approved",
                    "tell_me_more": [
                        "At the same time as defending Britain, the British military was fighting the Axis on many other fronts. In Singapore, the Japanese defeated the British and then occupied Burma, threatening India. The United States entered the war when the Japanese bombed its naval base at Pearl Harbour in December 1941."
                    ]
                },
                "id": "rec14y0yUZMuI79Aa"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "C",
                        "D"
                    ],
                    "feedback": "Phasellus lobortis eros sed nisl semper fringilla.",
                    "option_a": "Ut vitae mi vel metus pulvinar porta vel quis odio.",
                    "option_b": "Aliquam sit amet sapien aliquam, porttitor ligula ut, sollicitudin mi.",
                    "option_c": "Phasellus lobortis eros sed nisl semper fringilla.",
                    "option_d": "Nunc efficitur tellus a neque pellentesque, sed maximus ipsum consequat.",
                    "question_id": 1787,
                    "question_text": "Mauris a tellus commodo, tincidunt nisl id, facilisis sem.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec1FgGOunNZtqRm9"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec6bnuwjmSfM9vi2"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Curabitur pulvinar dolor varius ante venenatis, nec rhoncus dolor placerat.",
                    "option_a": "Fusce vitae dui eget arcu faucibus lacinia non a nulla.",
                    "option_b": "Fusce bibendum ex in orci faucibus, id rhoncus lacus imperdiet.",
                    "option_c": "Curabitur pulvinar dolor varius ante venenatis, nec rhoncus dolor placerat.",
                    "option_d": "In ac felis facilisis, ullamcorper neque rhoncus, semper ante.",
                    "question_id": 2145,
                    "question_text": "Donec varius nulla bibendum tempus euismod.",
                    "status": "Approved",
                    "tell_me_more": [
                        "At the same time as defending Britain, the British military was fighting the Axis on many other fronts. In Singapore, the Japanese defeated the British and then occupied Burma, threatening India. The United States entered the war when the Japanese bombed its naval base at Pearl Harbour in December 1941."
                    ]
                },
                "id": "rec1I1iLcAiFpcIyn"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "B",
                        "D"
                    ],
                    "feedback": "Cras lacinia nisl a quam vehicula tristique.",
                    "option_a": "Fusce ut metus facilisis, ultrices mi vel, commodo eros.",
                    "option_b": "Aliquam in nunc cursus, consequat libero non, laoreet sapien.",
                    "option_c": "Cras lacinia nisl a quam vehicula tristique.",
                    "option_d": "Mauris non massa accumsan, tincidunt urna eget, mollis dolor.",
                    "question_id": 2163,
                    "question_text": "Nunc tempus leo ac odio laoreet, ac finibus mi commodo.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec1R641k4OLLwvO1"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recqbxAfAYLZ8ZPH5"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Integer eleifend arcu nec libero tincidunt, a aliquam lectus dignissim.",
                    "option_a": "Integer vel enim sit amet ligula maximus fringilla sed et urna.",
                    "option_b": "Donec id felis quis sapien dignissim ultrices vel non enim.",
                    "option_c": "Integer eleifend arcu nec libero tincidunt, a aliquam lectus dignissim.",
                    "option_d": "Donec molestie erat et condimentum pulvinar.",
                    "question_id": 1834,
                    "question_text": "Nulla vel sem at nisi interdum laoreet id eu diam.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The Union Flag\n Although Ireland had had the same monarch as England and Wales since Henry VIII, it had remained a separate country. In 1801, Ireland became unified with England, Scotland and Wales after the Act of Union of 1800. This created the United Kingdom of Great Britain and Ireland. One symbol of this union between England, Scotland, Wales and Ireland was a new version of the official flag, the Union Flag. This is often called the Union Jack. The flag combined crosses associated with England, Scotland and Ireland. It is still used today as the official flag of the UK.\n The Union Flag consists of three crosses:\n - The cross of St George, patron saint of England, is a red cross on a white ground.\n - The cross of St Andrew, patron saint of Scotland, is a diagonal white cross on a blue ground.\n - The cross of St Patrick, patron saint of Ireland, is a diagonal red cross on a white ground.\n The Union Flag, also known as the Union Jack"
                    ]
                },
                "id": "rec1VeGRyu4PeZV75"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Pellentesque id sem ut massa tempor pharetra.",
                    "option_a": "Etiam rhoncus nunc sit amet dolor condimentum congue at vel ante.",
                    "option_b": "Ut non eros in lacus accumsan faucibus.",
                    "option_c": "Pellentesque id sem ut massa tempor pharetra.",
                    "option_d": "Integer in nulla ut velit gravida pulvinar.",
                    "question_id": 1845,
                    "question_text": "Donec molestie erat et condimentum pulvinar.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec1Wj5oCx3Phlyjq"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect3Mzfmz3cVYDvz"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Morbi cursus nisi consectetur gravida mollis.",
                    "option_a": "Donec vel turpis ultrices, posuere mauris ut, tempor magna.",
                    "option_b": "Praesent posuere risus a eros laoreet maximus.",
                    "option_c": "Morbi cursus nisi consectetur gravida mollis.",
                    "option_d": "Cras in eros vehicula, aliquet dolor sed, egestas lectus.",
                    "question_id": 1997,
                    "question_text": "Curabitur vestibulum nibh eu felis vulputate cursus.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The king\u201a\u00c4\u00f4s army was defeated at the Battles of Marston Moor and Naseby. By 1646, it was clear that Parliament had won the war. Charles was held prisoner by the parliamentary army. He was still unwilling to reach any agreement with Parliament and in 1649 he was executed."
                    ]
                },
                "id": "rec1ansnF5YmWLSLN"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "Mauris feugiat lorem id diam convallis, efficitur blandit nibh tempor.",
                    "option_a": "Nulla eu arcu scelerisque, egestas enim egestas, pellentesque dui.",
                    "option_b": "Pellentesque ac risus quis metus venenatis elementum.",
                    "option_c": "Mauris feugiat lorem id diam convallis, efficitur blandit nibh tempor.",
                    "option_d": "Quisque cursus lectus vel quam dictum viverra.",
                    "question_id": 2142,
                    "question_text": "Duis vehicula mauris a justo interdum, vitae sodales quam lobortis.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec1hcy5CSZNSZ2WK"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recqbxAfAYLZ8ZPH5"
                    ],
                    "correct_answer": [
                        "B",
                        "D"
                    ],
                    "feedback": "Aenean eu diam condimentum, eleifend sem at, posuere est.",
                    "option_a": "Suspendisse cursus leo eget quam convallis, eget eleifend enim efficitur.",
                    "option_b": "Duis sed lectus eu magna pulvinar viverra.",
                    "option_c": "Aenean eu diam condimentum, eleifend sem at, posuere est.",
                    "option_d": "Sed sodales est ac sem pharetra euismod.",
                    "question_id": 2020,
                    "question_text": "Sed luctus nulla mollis nunc interdum, eu vehicula tortor facilisis.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The Union Flag\n Although Ireland had had the same monarch as England and Wales since Henry VIII, it had remained a separate country. In 1801, Ireland became unified with England, Scotland and Wales after the Act of Union of 1800. This created the United Kingdom of Great Britain and Ireland. One symbol of this union between England, Scotland, Wales and Ireland was a new version of the official flag, the Union Flag. This is often called the Union Jack. The flag combined crosses associated with England, Scotland and Ireland. It is still used today as the official flag of the UK.\n The Union Flag consists of three crosses:\n - The cross of St George, patron saint of England, is a red cross on a white ground.\n - The cross of St Andrew, patron saint of Scotland, is a diagonal white cross on a blue ground.\n - The cross of St Patrick, patron saint of Ireland, is a diagonal red cross on a white ground.\n The Union Flag, also known as the Union Jack"
                    ]
                },
                "id": "rec1lGtN7zUavuDRn"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec6bnuwjmSfM9vi2"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Curabitur sagittis mi at viverra gravida.",
                    "option_a": "Donec venenatis erat eget arcu rhoncus, sit amet gravida ipsum vulputate.",
                    "option_b": "Duis placerat lectus et cursus pharetra.",
                    "option_c": "Curabitur sagittis mi at viverra gravida.",
                    "option_d": "Aliquam ut ipsum nec nulla aliquam luctus.",
                    "question_id": 1764,
                    "question_text": "Donec id ex posuere, placerat tellus at, blandit diam.",
                    "status": "Approved",
                    "tell_me_more": [
                        "At the same time as defending Britain, the British military was fighting the Axis on many other fronts. In Singapore, the Japanese defeated the British and then occupied Burma, threatening India. The United States entered the war when the Japanese bombed its naval base at Pearl Harbour in December 1941."
                    ]
                },
                "id": "rec1oC7qqxePSEAaB"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recCUgReDYfYvLJgM"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Proin fringilla magna et ligula sodales consequat.",
                    "option_a": "Curabitur vel metus bibendum, malesuada erat sit amet, scelerisque tortor.",
                    "option_b": "Sed sed mi quis dui placerat aliquam.",
                    "option_c": "Proin fringilla magna et ligula sodales consequat.",
                    "option_d": "Sed venenatis eros vel leo ultricies, ut feugiat urna pellentesque.",
                    "question_id": 2095,
                    "question_text": "Etiam eleifend elit sed erat fringilla, sed aliquam nibh molestie.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1997 the Labour Party led by Tony Blair was elected. The Blair government introduced a Scottish Parliament and a Welsh Assembly (see page 129). The Scottish Parliament has substantial powers to legislate. The Welsh Assembly was given fewer legislative powers but considerable control over public services. In Northern Ireland, the Blair government was able to build on the peace process, resulting in the Good Friday Agreement signed in 1998. The Northern Ireland Assembly was elected in 1999 but suspended in 2002. It was not reinstated until 2007. Most paramilitary groups in Northern Ireland have decommissioned their arms and are inactive. Gordon Brown took over as Prime Minister in 2007."
                    ]
                },
                "id": "rec21Xg9eC4Yp7rAi"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Nullam accumsan mauris id mauris sodales, id ultricies dolor lobortis.",
                    "option_a": "Praesent pretium velit vel lectus tincidunt venenatis.",
                    "option_b": "Nulla rhoncus ligula et elit consectetur iaculis.",
                    "option_c": "Nullam accumsan mauris id mauris sodales, id ultricies dolor lobortis.",
                    "option_d": "Vivamus et nibh ultricies, imperdiet felis eget, finibus ex.",
                    "question_id": 2057,
                    "question_text": "Ut facilisis metus non dui egestas aliquam.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec25263jZnDoDOqB"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recfTFrUo79SGIhvU"
                    ],
                    "correct_answer": [
                        "C",
                        "D"
                    ],
                    "feedback": "Donec accumsan risus nec dolor placerat gravida id at lacus.",
                    "option_a": "Ut tempor purus vel justo ullamcorper feugiat.",
                    "option_b": "Fusce ornare nulla eu fermentum sodales.",
                    "option_c": "Donec accumsan risus nec dolor placerat gravida id at lacus.",
                    "option_d": "Ut eu turpis blandit, ultricies mauris in, commodo lectus.",
                    "question_id": 2125,
                    "question_text": "Nunc id nisl interdum, venenatis metus non, vestibulum sem.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are many museums in the UK, which range from small community museums to large national and civic collections. Famous landmarks exist in towns, cities and the countryside throughout the UK. Most of them are open to the public to view (generally for a charge)."
                    ]
                },
                "id": "rec25uOFGTGrvgL4H"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recfTFrUo79SGIhvU"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Mauris nec diam vehicula, pellentesque metus eget, bibendum est.",
                    "option_a": "In vel ante a mi commodo vehicula.",
                    "option_b": "Proin eu orci ut ex elementum pharetra.",
                    "option_c": "Mauris nec diam vehicula, pellentesque metus eget, bibendum est.",
                    "option_d": "Duis tempus quam eu est interdum, id convallis purus tincidunt.",
                    "question_id": 1744,
                    "question_text": "Mauris viverra dui consequat diam imperdiet imperdiet.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are many museums in the UK, which range from small community museums to large national and civic collections. Famous landmarks exist in towns, cities and the countryside throughout the UK. Most of them are open to the public to view (generally for a charge)."
                    ]
                },
                "id": "rec2MH4VjhIpdvgFX"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Ut eu turpis blandit, ultricies mauris in, commodo lectus.",
                    "option_a": "Fusce ornare nulla eu fermentum sodales.",
                    "option_b": "Integer at elit sed nunc viverra pretium eget a sapien.",
                    "option_c": "Ut eu turpis blandit, ultricies mauris in, commodo lectus.",
                    "option_d": "Integer porttitor arcu non accumsan efficitur.",
                    "question_id": 2130,
                    "question_text": "Ut tempor purus vel justo ullamcorper feugiat.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "rec2WDPcjAFmAx2dt"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect3Mzfmz3cVYDvz"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Donec blandit nunc non dapibus suscipit.",
                    "option_a": "Vivamus vel nunc sit amet nibh sodales elementum.",
                    "option_b": "Proin vitae ligula lobortis, vestibulum purus vel, faucibus erat.",
                    "option_c": "Donec blandit nunc non dapibus suscipit.",
                    "option_d": "Aenean sed neque eu sapien porta sodales.",
                    "question_id": 1798,
                    "question_text": "Nunc efficitur tellus a neque pellentesque, sed maximus ipsum consequat.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The king\u201a\u00c4\u00f4s army was defeated at the Battles of Marston Moor and Naseby. By 1646, it was clear that Parliament had won the war. Charles was held prisoner by the parliamentary army. He was still unwilling to reach any agreement with Parliament and in 1649 he was executed."
                    ]
                },
                "id": "rec2iSimw3izhfiS9"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recN6N3OOPvSYlh5B"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Duis eu risus sit amet risus posuere iaculis.",
                    "option_a": "Suspendisse luctus dolor sed nisi congue consequat.",
                    "option_b": "Nullam sit amet metus aliquam, eleifend erat ac, pulvinar justo.",
                    "option_c": "Duis eu risus sit amet risus posuere iaculis.",
                    "option_d": "Aenean pellentesque erat eu ligula consectetur, ac ultrices libero consequat.",
                    "question_id": 1962,
                    "question_text": "Nunc commodo lorem vel dui accumsan convallis.",
                    "status": "Approved",
                    "tell_me_more": [
                        "From the end of June 1940 until the German invasion of the Soviet Union in June 1941, Britain and the Empire stood almost alone against Nazi Germany."
                    ]
                },
                "id": "rec378u3iCWz9HBDa"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "B"
                    ],
                    "feedback": "Aenean ut orci euismod sapien auctor elementum.",
                    "option_a": "Cras id sapien a quam cursus interdum.",
                    "option_b": "Proin at ante ut sem sodales iaculis.",
                    "option_c": "Aenean ut orci euismod sapien auctor elementum.",
                    "option_d": "Quisque ac felis rutrum, molestie nisl condimentum, dapibus quam.",
                    "question_id": 1736,
                    "question_text": "Phasellus consequat neque et placerat condimentum.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "rec3JHz9p8ub09xxb"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect3Mzfmz3cVYDvz"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Morbi tristique tellus ac mi varius ullamcorper.",
                    "option_a": "Mauris dignissim lacus at magna porttitor, et facilisis orci blandit.",
                    "option_b": "Vestibulum sagittis est non quam consequat dignissim.",
                    "option_c": "Morbi tristique tellus ac mi varius ullamcorper.",
                    "option_d": "Phasellus ut nibh viverra mauris malesuada placerat et eu nunc.",
                    "question_id": 1837,
                    "question_text": "Nunc vitae lectus tempor, sollicitudin turpis a, sodales purus.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The king\u201a\u00c4\u00f4s army was defeated at the Battles of Marston Moor and Naseby. By 1646, it was clear that Parliament had won the war. Charles was held prisoner by the parliamentary army. He was still unwilling to reach any agreement with Parliament and in 1649 he was executed."
                    ]
                },
                "id": "rec3P3y9wNPOKLWJ2"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recWEwUTqv82HNzK2"
                    ],
                    "correct_answer": [
                        "B",
                        "D"
                    ],
                    "feedback": "Aenean eu nibh tempus, consectetur augue finibus, imperdiet lectus.",
                    "option_a": "Donec auctor nibh vitae turpis lobortis porttitor.",
                    "option_b": "Quisque bibendum orci vel elit scelerisque tristique.",
                    "option_c": "Aenean eu nibh tempus, consectetur augue finibus, imperdiet lectus.",
                    "option_d": "Sed dignissim lectus non nisl viverra, ut sodales lectus ultrices.",
                    "question_id": 1721,
                    "question_text": "Donec nec nulla quis augue faucibus lobortis et eget lectus.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Notable British artists\n Thomas Gainsborough (1727\u201a\u00c4\u00ec88) was a portrait painter who often painted people in country or garden scenery.\n David Allan (1744\u201a\u00c4\u00ec96) was a Scottish painter who was best known for painting portraits. One of his most famous works is called The Origin of Painting.\n Joseph Turner (1775\u201a\u00c4\u00ec1851) was an influential landscape painter in a modern style. He is considered the artist who raised the profile of landscape painting.\n John Constable (1776\u201a\u00c4\u00ec1837) was a landscape painter most famous for his works of Dedham Vale on the Suffolk-Essex border in the east of England.\n The Pre-Raphaelites were an important group of artists in the second half of the 19th century. They painted detailed pictures on religious or literary themes in bright colours. The group included Holman Hunt, Dante Gabriel Rossetti and Sir John Millais.\n Sir John Lavery (1856\u201a\u00c4\u00ec1941) was a very successful Northern Irish portrait painter. His work included painting the Royal Family.\n Henry Moore (1898\u201a\u00c4\u00ec1986) was an English sculptor and artist. He is best known for his large bronze abstract sculptures."
                    ]
                },
                "id": "rec3haSsdUx8vX1Xq"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "Duis congue sem ac molestie tincidunt.",
                    "option_a": "Curabitur volutpat orci at massa hendrerit posuere.",
                    "option_b": "Pellentesque egestas quam at leo elementum, eget dapibus quam feugiat.",
                    "option_c": "Duis congue sem ac molestie tincidunt.",
                    "option_d": "Curabitur at eros placerat, commodo tellus vel, laoreet eros.",
                    "question_id": 2012,
                    "question_text": "Donec ut sem finibus, cursus quam in, rhoncus ex.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec3jEeZ2pRZr4sC6"
            },
            {
                "createdTime": "2019-08-18T13:05:34.000Z",
                "fields": {
                    "chapter": "Chapter 4",
                    "citation_ref": [
                        "rect3Mzfmz3cVYDvz"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Civil war broke out in the UK after Charles I tried to arrest parliamentary leaders. His army was defeated at the Battles of Marston Moor and Naseby. By 1646, it was clear that Parliament, lead by Oliver Cromwell, had won the war. ",
                    "old_question_id": "6428",
                    "option_a": "Elizabeth I",
                    "option_b": "James I",
                    "option_c": "Charles I",
                    "option_d": "Henry VII",
                    "question_id": 13,
                    "question_text": "Which monarch was defeated by Oliver Cromwell in the English Civil War?",
                    "status": "Approved",
                    "tell_me_more": [
                        "The king\u201a\u00c4\u00f4s army was defeated at the Battles of Marston Moor and Naseby. By 1646, it was clear that Parliament had won the war. Charles was held prisoner by the parliamentary army. He was still unwilling to reach any agreement with Parliament and in 1649 he was executed."
                    ]
                },
                "id": "rec3q5sdetGazJJnG"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recqbxAfAYLZ8ZPH5"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Nullam accumsan quam a sapien gravida, vel scelerisque lectus mollis.",
                    "option_a": "Etiam posuere magna at nisi finibus mattis.",
                    "option_b": "Donec vitae eros auctor, dignissim purus ac, ullamcorper eros.",
                    "option_c": "Nullam accumsan quam a sapien gravida, vel scelerisque lectus mollis.",
                    "option_d": "Cras finibus tellus eget nibh elementum, pharetra molestie enim sagittis.",
                    "question_id": 1912,
                    "question_text": "Mauris et ipsum vel felis suscipit commodo eget eu enim.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The Union Flag\n Although Ireland had had the same monarch as England and Wales since Henry VIII, it had remained a separate country. In 1801, Ireland became unified with England, Scotland and Wales after the Act of Union of 1800. This created the United Kingdom of Great Britain and Ireland. One symbol of this union between England, Scotland, Wales and Ireland was a new version of the official flag, the Union Flag. This is often called the Union Jack. The flag combined crosses associated with England, Scotland and Ireland. It is still used today as the official flag of the UK.\n The Union Flag consists of three crosses:\n - The cross of St George, patron saint of England, is a red cross on a white ground.\n - The cross of St Andrew, patron saint of Scotland, is a diagonal white cross on a blue ground.\n - The cross of St Patrick, patron saint of Ireland, is a diagonal red cross on a white ground.\n The Union Flag, also known as the Union Jack"
                    ]
                },
                "id": "rec3vxq6SFrk798EC"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Vivamus in urna feugiat, efficitur eros vel, vestibulum nulla.",
                    "option_a": "Morbi lobortis elit vel leo venenatis, eget porttitor elit auctor.",
                    "option_b": "Ut in nisi sed enim hendrerit tincidunt.",
                    "question_id": 2211,
                    "question_text": "Aliquam volutpat leo ut ligula iaculis fermentum.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec3zG2kA08h9QAcC"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recWEwUTqv82HNzK2"
                    ],
                    "correct_answer": [
                        "B",
                        "D"
                    ],
                    "feedback": "Proin pulvinar mauris vitae ex ultricies, eu interdum felis mattis.",
                    "option_a": "Sed nec felis tincidunt, convallis massa at, accumsan enim.",
                    "option_b": "Praesent ac urna quis elit aliquam sodales.",
                    "option_c": "Proin pulvinar mauris vitae ex ultricies, eu interdum felis mattis.",
                    "option_d": "Duis ut eros at mi tincidunt semper.",
                    "question_id": 1747,
                    "question_text": "Quisque ac felis rutrum, molestie nisl condimentum, dapibus quam.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Notable British artists\n Thomas Gainsborough (1727\u201a\u00c4\u00ec88) was a portrait painter who often painted people in country or garden scenery.\n David Allan (1744\u201a\u00c4\u00ec96) was a Scottish painter who was best known for painting portraits. One of his most famous works is called The Origin of Painting.\n Joseph Turner (1775\u201a\u00c4\u00ec1851) was an influential landscape painter in a modern style. He is considered the artist who raised the profile of landscape painting.\n John Constable (1776\u201a\u00c4\u00ec1837) was a landscape painter most famous for his works of Dedham Vale on the Suffolk-Essex border in the east of England.\n The Pre-Raphaelites were an important group of artists in the second half of the 19th century. They painted detailed pictures on religious or literary themes in bright colours. The group included Holman Hunt, Dante Gabriel Rossetti and Sir John Millais.\n Sir John Lavery (1856\u201a\u00c4\u00ec1941) was a very successful Northern Irish portrait painter. His work included painting the Royal Family.\n Henry Moore (1898\u201a\u00c4\u00ec1986) was an English sculptor and artist. He is best known for his large bronze abstract sculptures."
                    ]
                },
                "id": "rec40cmIzE1NGijaV"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec6bnuwjmSfM9vi2"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Donec commodo odio luctus ornare suscipit.",
                    "option_a": "Cras et magna tempor, auctor risus non, placerat velit.",
                    "option_b": "Praesent vel sem vitae nisl dapibus fermentum in sed arcu.",
                    "option_c": "Donec commodo odio luctus ornare suscipit.",
                    "option_d": "Duis non diam non felis gravida lacinia eget et ipsum.",
                    "question_id": 2106,
                    "question_text": "Sed venenatis eros vel leo ultricies, ut feugiat urna pellentesque.",
                    "status": "Approved",
                    "tell_me_more": [
                        "At the same time as defending Britain, the British military was fighting the Axis on many other fronts. In Singapore, the Japanese defeated the British and then occupied Burma, threatening India. The United States entered the war when the Japanese bombed its naval base at Pearl Harbour in December 1941."
                    ]
                },
                "id": "rec4281vWpEkk0rJW"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect8zlDQoCg3xfbG"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Vivamus a lacus hendrerit, accumsan urna in, laoreet nisi.",
                    "option_a": "Ut lobortis eros id massa mollis, eu viverra ipsum efficitur.",
                    "option_b": "Suspendisse feugiat enim a est eleifend ullamcorper.",
                    "option_c": "Vivamus a lacus hendrerit, accumsan urna in, laoreet nisi.",
                    "option_d": "Fusce finibus purus vitae arcu malesuada blandit.",
                    "question_id": 1820,
                    "question_text": "Sed in nunc sagittis, commodo elit vel, pellentesque nunc.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The laws passed after the Glorious Revolution are the beginning of what is called \u201a\u00c4\u00f2constitutional monarchy\u201a\u00c4\u00f4. The monarch remained very important but was no longer able to insist on particular policies or actions if Parliament did not agree. After William III, the ministers gradually became more important than the monarch but this was not a democracy in the modern sense. The number of people who had the right to vote for members of Parliament was still very small. Only men who owned property of a certain value were able to vote. No women at all had the vote. Some constituencies were controlled by a single wealthy family. These were called \u201a\u00c4\u00f2pocket boroughs\u201a\u00c4\u00f4. Other constituencies had hardly any voters and were called \u201a\u00c4\u00f2rotten boroughs\u201a\u00c4\u00f4."
                    ]
                },
                "id": "rec4Mql2sXufBWSJq"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "Aliquam dapibus enim ac purus bibendum, sit amet congue sapien accumsan.",
                    "option_a": "Morbi at sem id est lobortis imperdiet ac vitae sapien.",
                    "option_b": "Pellentesque fermentum mi sed tortor lacinia, ac tempus ante tincidunt.",
                    "option_c": "Aliquam dapibus enim ac purus bibendum, sit amet congue sapien accumsan.",
                    "option_d": "Nulla scelerisque ligula a purus venenatis, quis vehicula nunc tempus.",
                    "question_id": 1947,
                    "question_text": "Ut vitae dolor placerat, congue lacus vitae, tempor nisl.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec4czGKFGd6ZkKir"
            },
            {
                "createdTime": "2019-08-18T13:05:34.000Z",
                "fields": {
                    "chapter": "Chapter 4",
                    "citation_ref": [
                        "rec8CttRBQ4sckKIt"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Henry VIII wanted a divorce because his wife, Catherine of Aragon, had not given him a surviving heir. In order to get a divorce and remarry he needed to approval of the Pope, who had authority over all Christians in western Europe. When the Pope refused, Henry established the Church of England.",
                    "old_question_id": "6426",
                    "option_a": "Henry VIII",
                    "option_b": "Elizabeth I",
                    "option_c": "Edward I",
                    "option_d": "Henry VII",
                    "question_id": 12,
                    "question_text": "Which monarch established the Church of England?",
                    "status": "Approved",
                    "tell_me_more": [
                        "To divorce his first wife, Henry needed the approval of the Pope. When the Pope refused, Henry established the Church of England. In this new Church, the king, not the Pope, would have the power to appoint bishops and order how people should worship."
                    ]
                },
                "id": "rec4lTUINzwJGX9OF"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect3Mzfmz3cVYDvz"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Fusce in purus vitae orci semper scelerisque.",
                    "option_a": "Nunc in purus ac lectus facilisis laoreet.",
                    "option_b": "Vestibulum aliquam sem et mattis blandit.",
                    "option_c": "Fusce in purus vitae orci semper scelerisque.",
                    "option_d": "Mauris viverra dui consequat diam imperdiet imperdiet.",
                    "question_id": 1733,
                    "question_text": "Phasellus semper enim a volutpat tincidunt.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The king\u201a\u00c4\u00f4s army was defeated at the Battles of Marston Moor and Naseby. By 1646, it was clear that Parliament had won the war. Charles was held prisoner by the parliamentary army. He was still unwilling to reach any agreement with Parliament and in 1649 he was executed."
                    ]
                },
                "id": "rec4ltsmfsmhKRZXb"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Curabitur vel metus bibendum, malesuada erat sit amet, scelerisque tortor.",
                    "option_a": "Donec quis eros et arcu commodo ornare.",
                    "option_b": "Etiam bibendum nisi id lacus tincidunt, eu imperdiet enim convallis.",
                    "option_c": "Curabitur vel metus bibendum, malesuada erat sit amet, scelerisque tortor.",
                    "option_d": "Sed sed mi quis dui placerat aliquam.",
                    "question_id": 2094,
                    "question_text": "Morbi sed odio ut massa tincidunt egestas laoreet id ipsum.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "rec4nQymKUfzYF2Xk"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect3Mzfmz3cVYDvz"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Ut tristique nunc non turpis semper commodo.",
                    "option_a": "Aliquam nec urna sit amet est condimentum vehicula.",
                    "option_b": "Sed bibendum turpis eget augue ornare mollis.",
                    "option_c": "Ut tristique nunc non turpis semper commodo.",
                    "option_d": "Vivamus et ante rutrum, fermentum lectus in, scelerisque erat.",
                    "question_id": 2036,
                    "question_text": "Donec vitae magna ac mauris semper sagittis eget et justo.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The king\u201a\u00c4\u00f4s army was defeated at the Battles of Marston Moor and Naseby. By 1646, it was clear that Parliament had won the war. Charles was held prisoner by the parliamentary army. He was still unwilling to reach any agreement with Parliament and in 1649 he was executed."
                    ]
                },
                "id": "rec4ymnn96KvqQXDR"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "Praesent facilisis ipsum ac lectus eleifend, id condimentum nibh convallis.",
                    "option_a": "Proin maximus nisi sed est lobortis blandit.",
                    "option_b": "Praesent tincidunt neque id dolor finibus sollicitudin.",
                    "option_c": "Praesent facilisis ipsum ac lectus eleifend, id condimentum nibh convallis.",
                    "option_d": "Suspendisse mattis neque quis feugiat vestibulum.",
                    "question_id": 2116,
                    "question_text": "Praesent vel sem vitae nisl dapibus fermentum in sed arcu.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec5Bp74lZBQ4gaym"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec8CttRBQ4sckKIt"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Fusce pharetra mi ac libero tincidunt commodo.",
                    "option_a": "Mauris sit amet massa non tortor vulputate condimentum eget eget ligula.",
                    "option_b": "Phasellus quis nisl eu nisl dictum tempor.",
                    "option_c": "Fusce pharetra mi ac libero tincidunt commodo.",
                    "option_d": "Cras volutpat sem a ultrices viverra.",
                    "question_id": 1719,
                    "question_text": "Praesent et massa eget purus auctor volutpat non quis nibh.",
                    "status": "Approved",
                    "tell_me_more": [
                        "To divorce his first wife, Henry needed the approval of the Pope. When the Pope refused, Henry established the Church of England. In this new Church, the king, not the Pope, would have the power to appoint bishops and order how people should worship."
                    ]
                },
                "id": "rec5E7b7gCNvzBCvG"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recfTFrUo79SGIhvU"
                    ],
                    "correct_answer": [
                        "C",
                        "D"
                    ],
                    "feedback": "Proin dapibus sapien eget arcu consequat, eget pellentesque sem lacinia.",
                    "option_a": "Ut varius lacus ac ante mollis consequat.",
                    "option_b": "Quisque fermentum velit et elit malesuada, sit amet dapibus nunc ornare.",
                    "option_c": "Proin dapibus sapien eget arcu consequat, eget pellentesque sem lacinia.",
                    "option_d": "Ut maximus mauris at risus pellentesque interdum.",
                    "question_id": 1969,
                    "question_text": "Nunc sit amet justo venenatis, interdum lectus at, lacinia quam.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are many museums in the UK, which range from small community museums to large national and civic collections. Famous landmarks exist in towns, cities and the countryside throughout the UK. Most of them are open to the public to view (generally for a charge)."
                    ]
                },
                "id": "rec5QRQI64imx5ax5"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Ut maximus mauris at risus pellentesque interdum.",
                    "option_a": "Quisque fermentum velit et elit malesuada, sit amet dapibus nunc ornare.",
                    "option_b": "Vestibulum pulvinar justo blandit, pharetra libero ut, laoreet nibh.",
                    "option_c": "Ut maximus mauris at risus pellentesque interdum.",
                    "option_d": "Proin non tellus malesuada, placerat nisl nec, vulputate lacus.",
                    "question_id": 1974,
                    "question_text": "Ut varius lacus ac ante mollis consequat.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "rec5RwLNGjJybqjE8"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec8CttRBQ4sckKIt"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Nullam laoreet sem at iaculis placerat.",
                    "option_a": "Duis sit amet libero vel justo maximus interdum eu nec justo.",
                    "option_b": "Vivamus quis ex placerat, vestibulum tellus ac, fermentum velit.",
                    "option_c": "Nullam laoreet sem at iaculis placerat.",
                    "option_d": "Sed eu leo a sem aliquet egestas.",
                    "question_id": 1914,
                    "question_text": "Nam placerat sem ut lectus ultricies, non dictum quam porta.",
                    "status": "Approved",
                    "tell_me_more": [
                        "To divorce his first wife, Henry needed the approval of the Pope. When the Pope refused, Henry established the Church of England. In this new Church, the king, not the Pope, would have the power to appoint bishops and order how people should worship."
                    ]
                },
                "id": "rec5UFOpF4LKuxWXf"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recfTFrUo79SGIhvU"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "In lacinia enim a tortor feugiat, eget posuere magna gravida.",
                    "option_a": "Fusce pharetra enim dictum sem blandit, ut elementum nulla blandit.",
                    "option_b": "In at quam efficitur, elementum sapien vel, imperdiet augue.",
                    "option_c": "In lacinia enim a tortor feugiat, eget posuere magna gravida.",
                    "option_d": "Duis accumsan nibh ac risus facilisis commodo.",
                    "question_id": 1757,
                    "question_text": "Praesent ac urna quis elit aliquam sodales.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are many museums in the UK, which range from small community museums to large national and civic collections. Famous landmarks exist in towns, cities and the countryside throughout the UK. Most of them are open to the public to view (generally for a charge)."
                    ]
                },
                "id": "rec5uQ1cQoMfnD1R5"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recqbxAfAYLZ8ZPH5"
                    ],
                    "correct_answer": [
                        "B",
                        "D"
                    ],
                    "feedback": "Duis non diam non felis gravida lacinia eget et ipsum.",
                    "option_a": "Praesent vel sem vitae nisl dapibus fermentum in sed arcu.",
                    "option_b": "Proin maximus nisi sed est lobortis blandit.",
                    "option_c": "Duis non diam non felis gravida lacinia eget et ipsum.",
                    "option_d": "Praesent facilisis ipsum ac lectus eleifend, id condimentum nibh convallis.",
                    "question_id": 2111,
                    "question_text": "Cras et magna tempor, auctor risus non, placerat velit.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The Union Flag\n Although Ireland had had the same monarch as England and Wales since Henry VIII, it had remained a separate country. In 1801, Ireland became unified with England, Scotland and Wales after the Act of Union of 1800. This created the United Kingdom of Great Britain and Ireland. One symbol of this union between England, Scotland, Wales and Ireland was a new version of the official flag, the Union Flag. This is often called the Union Jack. The flag combined crosses associated with England, Scotland and Ireland. It is still used today as the official flag of the UK.\n The Union Flag consists of three crosses:\n - The cross of St George, patron saint of England, is a red cross on a white ground.\n - The cross of St Andrew, patron saint of Scotland, is a diagonal white cross on a blue ground.\n - The cross of St Patrick, patron saint of Ireland, is a diagonal red cross on a white ground.\n The Union Flag, also known as the Union Jack"
                    ]
                },
                "id": "rec5vjCR4kMVu8UNl"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "Phasellus aliquam mi nec orci convallis, id tempor nunc auctor.",
                    "option_a": "Etiam eleifend elit sed erat fringilla, sed aliquam nibh molestie.",
                    "option_b": "Curabitur vel metus bibendum, malesuada erat sit amet, scelerisque tortor.",
                    "option_c": "Phasellus aliquam mi nec orci convallis, id tempor nunc auctor.",
                    "option_d": "Proin fringilla magna et ligula sodales consequat.",
                    "question_id": 2090,
                    "question_text": "Aenean tincidunt nisl eget finibus sollicitudin.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec64cwFaGzoiCz3B"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec6bnuwjmSfM9vi2"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Nunc sit amet justo venenatis, interdum lectus at, lacinia quam.",
                    "option_a": "Duis eu risus sit amet risus posuere iaculis.",
                    "option_b": "Aenean pellentesque erat eu ligula consectetur, ac ultrices libero consequat.",
                    "option_c": "Nunc sit amet justo venenatis, interdum lectus at, lacinia quam.",
                    "option_d": "Ut varius lacus ac ante mollis consequat.",
                    "question_id": 1963,
                    "question_text": "Suspendisse hendrerit ligula et imperdiet tincidunt.",
                    "status": "Approved",
                    "tell_me_more": [
                        "At the same time as defending Britain, the British military was fighting the Axis on many other fronts. In Singapore, the Japanese defeated the British and then occupied Burma, threatening India. The United States entered the war when the Japanese bombed its naval base at Pearl Harbour in December 1941."
                    ]
                },
                "id": "rec66Avj6ViUoWu3X"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect8zlDQoCg3xfbG"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Aenean tincidunt nisl eget finibus sollicitudin.",
                    "option_a": "Donec finibus odio rhoncus, bibendum lorem sed, vehicula ligula.",
                    "option_b": "Morbi sed odio ut massa tincidunt egestas laoreet id ipsum.",
                    "option_c": "Aenean tincidunt nisl eget finibus sollicitudin.",
                    "option_d": "Etiam eleifend elit sed erat fringilla, sed aliquam nibh molestie.",
                    "question_id": 2084,
                    "question_text": "Donec porta nibh et velit laoreet, eleifend molestie neque aliquet.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The laws passed after the Glorious Revolution are the beginning of what is called \u201a\u00c4\u00f2constitutional monarchy\u201a\u00c4\u00f4. The monarch remained very important but was no longer able to insist on particular policies or actions if Parliament did not agree. After William III, the ministers gradually became more important than the monarch but this was not a democracy in the modern sense. The number of people who had the right to vote for members of Parliament was still very small. Only men who owned property of a certain value were able to vote. No women at all had the vote. Some constituencies were controlled by a single wealthy family. These were called \u201a\u00c4\u00f2pocket boroughs\u201a\u00c4\u00f4. Other constituencies had hardly any voters and were called \u201a\u00c4\u00f2rotten boroughs\u201a\u00c4\u00f4."
                    ]
                },
                "id": "rec699WDLLT9Azfyl"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Suspendisse ac tortor aliquet, aliquam odio ut, blandit ipsum.",
                    "option_a": "Aliquam volutpat leo ut ligula iaculis fermentum.",
                    "option_b": "Nunc ornare orci venenatis dolor ornare ultricies.",
                    "option_c": "Maecenas aliquet arcu pretium gravida mattis.",
                    "option_d": "Integer finibus odio a libero fringilla, sed tempus erat tincidunt.",
                    "question_id": 2212,
                    "question_text": "Maecenas aliquet arcu pretium gravida mattis.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec6R95oLf7LwCWxo"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Quisque pharetra sapien vel sollicitudin sagittis.",
                    "option_a": "Phasellus eu nibh eget augue interdum dictum.",
                    "option_b": "Aliquam volutpat leo ut ligula iaculis fermentum.",
                    "option_c": "Quisque pharetra sapien vel sollicitudin sagittis.",
                    "option_d": "Maecenas aliquet arcu pretium gravida mattis.",
                    "question_id": 2201,
                    "question_text": "Donec pretium metus a ex pretium, at aliquet massa eleifend.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec6VrJ0jtOuJNQly"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect3Mzfmz3cVYDvz"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Duis fringilla ipsum at felis porttitor, non interdum dolor ornare.",
                    "option_a": "Pellentesque ultrices mauris nec luctus dictum.",
                    "option_b": "Phasellus nec velit aliquam, suscipit enim eget, viverra elit.",
                    "option_c": "Duis fringilla ipsum at felis porttitor, non interdum dolor ornare.",
                    "option_d": "In dictum ante ut ligula ullamcorper, sit amet porta risus porta.",
                    "question_id": 1876,
                    "question_text": "Nam tincidunt felis quis erat viverra bibendum.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The king\u201a\u00c4\u00f4s army was defeated at the Battles of Marston Moor and Naseby. By 1646, it was clear that Parliament had won the war. Charles was held prisoner by the parliamentary army. He was still unwilling to reach any agreement with Parliament and in 1649 he was executed."
                    ]
                },
                "id": "rec6YCoghO6Ac328Q"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Praesent auctor felis ac arcu pharetra vestibulum id sed dui.",
                    "option_a": "Ut gravida purus vitae accumsan tincidunt.",
                    "option_b": "Phasellus congue erat vitae enim sodales hendrerit.",
                    "option_c": "Praesent auctor felis ac arcu pharetra vestibulum id sed dui.",
                    "option_d": "Cras eu ex viverra, accumsan erat sed, pulvinar lorem.",
                    "question_id": 2192,
                    "question_text": "Nunc commodo nisi bibendum orci consequat malesuada.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec6Z3aNAosoZY0jF"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Nam bibendum nisl at aliquam varius.",
                    "option_a": "In ac nisl non mauris scelerisque imperdiet.",
                    "option_b": "Nunc tempus leo ac odio laoreet, ac finibus mi commodo.",
                    "option_c": "Nam bibendum nisl at aliquam varius.",
                    "option_d": "Phasellus porttitor mi id metus ultrices, quis interdum risus molestie.",
                    "question_id": 2153,
                    "question_text": "Quisque cursus lectus vel quam dictum viverra.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec6aIZX6ikE34ri3"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Curabitur at mauris condimentum, facilisis libero at, luctus velit.",
                    "option_a": "Nulla scelerisque ligula a purus venenatis, quis vehicula nunc tempus.",
                    "option_b": "Suspendisse hendrerit ligula et imperdiet tincidunt.",
                    "option_c": "Curabitur at mauris condimentum, facilisis libero at, luctus velit.",
                    "option_d": "Phasellus eget felis congue, tristique ante quis, tempus tellus.",
                    "question_id": 1953,
                    "question_text": "Aliquam dapibus enim ac purus bibendum, sit amet congue sapien accumsan.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec6e4HH6i53oGA5L"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recCUgReDYfYvLJgM"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Ut a enim eu leo scelerisque viverra.",
                    "option_a": "Pellentesque rutrum nibh vel mi dictum sagittis.",
                    "option_b": "In ac purus a massa bibendum efficitur sed at nisl.",
                    "option_c": "Ut a enim eu leo scelerisque viverra.",
                    "option_d": "Vestibulum vitae odio et ligula venenatis mollis in vitae tellus.",
                    "question_id": 1818,
                    "question_text": "Maecenas id nibh sed magna dictum ornare.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1997 the Labour Party led by Tony Blair was elected. The Blair government introduced a Scottish Parliament and a Welsh Assembly (see page 129). The Scottish Parliament has substantial powers to legislate. The Welsh Assembly was given fewer legislative powers but considerable control over public services. In Northern Ireland, the Blair government was able to build on the peace process, resulting in the Good Friday Agreement signed in 1998. The Northern Ireland Assembly was elected in 1999 but suspended in 2002. It was not reinstated until 2007. Most paramilitary groups in Northern Ireland have decommissioned their arms and are inactive. Gordon Brown took over as Prime Minister in 2007."
                    ]
                },
                "id": "rec6gZqqim3p0QXBw"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "C",
                        "D"
                    ],
                    "feedback": "Morbi lobortis elit vel leo venenatis, eget porttitor elit auctor.",
                    "option_a": "Integer finibus odio a libero fringilla, sed tempus erat tincidunt.",
                    "option_b": "Suspendisse ac tortor aliquet, aliquam odio ut, blandit ipsum.",
                    "option_c": "Morbi lobortis elit vel leo venenatis, eget porttitor elit auctor.",
                    "option_d": "Curabitur pretium enim id lorem vulputate, vitae iaculis purus malesuada.",
                    "question_id": 2216,
                    "question_text": "Morbi lobortis elit vel leo venenatis, eget porttitor elit auctor.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec6jhhIiAui1ZIug"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec6bnuwjmSfM9vi2"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Mauris viverra dui consequat diam imperdiet imperdiet.",
                    "option_a": "Vestibulum aliquam sem et mattis blandit.",
                    "option_b": "Phasellus efficitur ante in mi varius ullamcorper.",
                    "option_c": "Mauris viverra dui consequat diam imperdiet imperdiet.",
                    "option_d": "In vel ante a mi commodo vehicula.",
                    "question_id": 1738,
                    "question_text": "Nunc in purus ac lectus facilisis laoreet.",
                    "status": "Approved",
                    "tell_me_more": [
                        "At the same time as defending Britain, the British military was fighting the Axis on many other fronts. In Singapore, the Japanese defeated the British and then occupied Burma, threatening India. The United States entered the war when the Japanese bombed its naval base at Pearl Harbour in December 1941."
                    ]
                },
                "id": "rec6sgwjOdcDpBAuv"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "Fusce luctus augue eu justo volutpat molestie.",
                    "option_a": "Sed dictum magna quis purus placerat posuere.",
                    "option_b": "Donec sodales augue ut metus vehicula, eu feugiat elit sollicitudin.",
                    "option_c": "Fusce luctus augue eu justo volutpat molestie.",
                    "option_d": "Curabitur posuere velit eu iaculis porta.",
                    "question_id": 2155,
                    "question_text": "Fusce bibendum ex in orci faucibus, id rhoncus lacus imperdiet.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec6vZhdJL1OORXQO"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec8CttRBQ4sckKIt"
                    ],
                    "correct_answer": [
                        "B"
                    ],
                    "feedback": "Sed venenatis eros vel leo ultricies, ut feugiat urna pellentesque.",
                    "option_a": "Sed sed mi quis dui placerat aliquam.",
                    "option_b": "Phasellus id metus vitae odio condimentum rutrum.",
                    "option_c": "Sed venenatis eros vel leo ultricies, ut feugiat urna pellentesque.",
                    "option_d": "Cras et magna tempor, auctor risus non, placerat velit.",
                    "question_id": 2100,
                    "question_text": "Curabitur vel metus bibendum, malesuada erat sit amet, scelerisque tortor.",
                    "status": "Approved",
                    "tell_me_more": [
                        "To divorce his first wife, Henry needed the approval of the Pope. When the Pope refused, Henry established the Church of England. In this new Church, the king, not the Pope, would have the power to appoint bishops and order how people should worship."
                    ]
                },
                "id": "rec6wszDcwlv4pxpX"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "Mauris non massa accumsan, tincidunt urna eget, mollis dolor.",
                    "option_a": "Aliquam in nunc cursus, consequat libero non, laoreet sapien.",
                    "option_b": "Vestibulum vestibulum elit ac libero sagittis auctor.",
                    "option_c": "Mauris non massa accumsan, tincidunt urna eget, mollis dolor.",
                    "option_d": "Maecenas condimentum arcu ut est tristique finibus.",
                    "question_id": 2168,
                    "question_text": "Fusce ut metus facilisis, ultrices mi vel, commodo eros.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec745eiaQSfPVebv"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Integer porttitor arcu non accumsan efficitur.",
                    "option_a": "Integer at elit sed nunc viverra pretium eget a sapien.",
                    "option_b": "Donec varius nulla bibendum tempus euismod.",
                    "option_c": "Integer porttitor arcu non accumsan efficitur.",
                    "option_d": "Integer viverra turpis et velit hendrerit iaculis.",
                    "question_id": 2135,
                    "question_text": "Fusce ornare nulla eu fermentum sodales.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec7AyRxuCwVqy8bg"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect3Mzfmz3cVYDvz"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Vivamus eget felis nec metus tincidunt ornare in vitae lorem.",
                    "option_a": "Curabitur auctor lectus id mi fringilla venenatis nec et lacus.",
                    "option_b": "Duis feugiat felis sed arcu maximus, sit amet vehicula diam tempus.",
                    "option_c": "Vivamus eget felis nec metus tincidunt ornare in vitae lorem.",
                    "option_d": "Phasellus sit amet nibh quis nulla dignissim pulvinar.",
                    "question_id": 1984,
                    "question_text": "Vestibulum pulvinar justo blandit, pharetra libero ut, laoreet nibh.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The king\u201a\u00c4\u00f4s army was defeated at the Battles of Marston Moor and Naseby. By 1646, it was clear that Parliament had won the war. Charles was held prisoner by the parliamentary army. He was still unwilling to reach any agreement with Parliament and in 1649 he was executed."
                    ]
                },
                "id": "rec7NL8VBvSDMeCYx"
            },
            {
                "createdTime": "2019-11-23T17:31:18.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recqbxAfAYLZ8ZPH5"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Nunc non sapien volutpat metus porta pulvinar.",
                    "option_a": "Ut vehicula velit nec tortor dignissim, ac iaculis quam convallis.",
                    "option_b": "Aenean eu nibh tempus, consectetur augue finibus, imperdiet lectus.",
                    "option_c": "Nunc non sapien volutpat metus porta pulvinar.",
                    "option_d": "Sed id orci ut augue tristique ultrices eget vel velit.",
                    "question_id": 1717,
                    "question_text": "Phasellus vel odio tempus, condimentum ante nec, bibendum lectus.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The Union Flag\n Although Ireland had had the same monarch as England and Wales since Henry VIII, it had remained a separate country. In 1801, Ireland became unified with England, Scotland and Wales after the Act of Union of 1800. This created the United Kingdom of Great Britain and Ireland. One symbol of this union between England, Scotland, Wales and Ireland was a new version of the official flag, the Union Flag. This is often called the Union Jack. The flag combined crosses associated with England, Scotland and Ireland. It is still used today as the official flag of the UK.\n The Union Flag consists of three crosses:\n - The cross of St George, patron saint of England, is a red cross on a white ground.\n - The cross of St Andrew, patron saint of Scotland, is a diagonal white cross on a blue ground.\n - The cross of St Patrick, patron saint of Ireland, is a diagonal red cross on a white ground.\n The Union Flag, also known as the Union Jack"
                    ]
                },
                "id": "rec7VohWqdHYO7bT6"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Donec sodales augue ut metus vehicula, eu feugiat elit sollicitudin.",
                    "option_a": "Phasellus porttitor mi id metus ultrices, quis interdum risus molestie.",
                    "option_b": "Cras lacinia nisl a quam vehicula tristique.",
                    "option_c": "Donec sodales augue ut metus vehicula, eu feugiat elit sollicitudin.",
                    "option_d": "Pellentesque sed justo quis metus pellentesque mattis sed vitae urna.",
                    "question_id": 2159,
                    "question_text": "Nam bibendum nisl at aliquam varius.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec7kuSxTDRPGr6X7"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recCUgReDYfYvLJgM"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Proin at ante ut sem sodales iaculis.",
                    "option_a": "Donec maximus neque sed ex pharetra viverra.",
                    "option_b": "Mauris nec diam vehicula, pellentesque metus eget, bibendum est.",
                    "option_c": "Proin at ante ut sem sodales iaculis.",
                    "option_d": "Nunc sollicitudin neque id auctor tincidunt.",
                    "question_id": 1740,
                    "question_text": "Suspendisse at nunc eu metus euismod laoreet sit amet viverra mi.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1997 the Labour Party led by Tony Blair was elected. The Blair government introduced a Scottish Parliament and a Welsh Assembly (see page 129). The Scottish Parliament has substantial powers to legislate. The Welsh Assembly was given fewer legislative powers but considerable control over public services. In Northern Ireland, the Blair government was able to build on the peace process, resulting in the Good Friday Agreement signed in 1998. The Northern Ireland Assembly was elected in 1999 but suspended in 2002. It was not reinstated until 2007. Most paramilitary groups in Northern Ireland have decommissioned their arms and are inactive. Gordon Brown took over as Prime Minister in 2007."
                    ]
                },
                "id": "rec7yHmkCKnTt1cSh"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "C",
                        "D"
                    ],
                    "feedback": "Vestibulum at tellus sit amet diam pharetra ornare ac at tortor.",
                    "option_a": "Duis sit amet nisi ut massa mollis elementum.",
                    "option_b": "Nulla cursus eros et nunc bibendum, quis pulvinar purus gravida.",
                    "option_c": "Vestibulum at tellus sit amet diam pharetra ornare ac at tortor.",
                    "option_d": "Suspendisse congue ex et ex dignissim hendrerit.",
                    "question_id": 1878,
                    "question_text": "Integer porta lectus id sapien fringilla, quis gravida turpis fermentum.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec82fn19hkuzlzoc"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec6bnuwjmSfM9vi2"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Phasellus sit amet nibh quis nulla dignissim pulvinar.",
                    "option_a": "Duis feugiat felis sed arcu maximus, sit amet vehicula diam tempus.",
                    "option_b": "Sed non turpis euismod, sagittis est ac, semper lorem.",
                    "option_c": "Phasellus sit amet nibh quis nulla dignissim pulvinar.",
                    "option_d": "Morbi vitae leo quis turpis sodales placerat id ut metus.",
                    "question_id": 1989,
                    "question_text": "Curabitur auctor lectus id mi fringilla venenatis nec et lacus.",
                    "status": "Approved",
                    "tell_me_more": [
                        "At the same time as defending Britain, the British military was fighting the Axis on many other fronts. In Singapore, the Japanese defeated the British and then occupied Burma, threatening India. The United States entered the war when the Japanese bombed its naval base at Pearl Harbour in December 1941."
                    ]
                },
                "id": "rec8IgcMhMyiKIbiz"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recWEwUTqv82HNzK2"
                    ],
                    "correct_answer": [
                        "B",
                        "D"
                    ],
                    "feedback": "Pellentesque at nunc ac tortor tincidunt pellentesque.",
                    "option_a": "Donec blandit nunc non dapibus suscipit.",
                    "option_b": "Aenean sed neque eu sapien porta sodales.",
                    "option_c": "Pellentesque at nunc ac tortor tincidunt pellentesque.",
                    "option_d": "Nulla sed dui eget turpis congue tristique.",
                    "question_id": 1799,
                    "question_text": "Fusce viverra mauris nec lacus eleifend porta.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Notable British artists\n Thomas Gainsborough (1727\u201a\u00c4\u00ec88) was a portrait painter who often painted people in country or garden scenery.\n David Allan (1744\u201a\u00c4\u00ec96) was a Scottish painter who was best known for painting portraits. One of his most famous works is called The Origin of Painting.\n Joseph Turner (1775\u201a\u00c4\u00ec1851) was an influential landscape painter in a modern style. He is considered the artist who raised the profile of landscape painting.\n John Constable (1776\u201a\u00c4\u00ec1837) was a landscape painter most famous for his works of Dedham Vale on the Suffolk-Essex border in the east of England.\n The Pre-Raphaelites were an important group of artists in the second half of the 19th century. They painted detailed pictures on religious or literary themes in bright colours. The group included Holman Hunt, Dante Gabriel Rossetti and Sir John Millais.\n Sir John Lavery (1856\u201a\u00c4\u00ec1941) was a very successful Northern Irish portrait painter. His work included painting the Royal Family.\n Henry Moore (1898\u201a\u00c4\u00ec1986) was an English sculptor and artist. He is best known for his large bronze abstract sculptures."
                    ]
                },
                "id": "rec8NZffVUwMda2Uy"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Fusce gravida nulla non mauris tristique, eu aliquet nulla ultricies.",
                    "option_a": "Suspendisse congue ex et ex dignissim hendrerit.",
                    "option_b": "Etiam tristique augue at lorem maximus, gravida lobortis justo ultrices.",
                    "option_c": "Fusce gravida nulla non mauris tristique, eu aliquet nulla ultricies.",
                    "option_d": "Duis eget tortor molestie, placerat arcu vel, consequat quam.",
                    "question_id": 1884,
                    "question_text": "Vestibulum at tellus sit amet diam pharetra ornare ac at tortor.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec8UFUwjZRUzskj4"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect8zlDQoCg3xfbG"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Mauris vel lectus et eros venenatis sollicitudin consequat id ex.",
                    "option_a": "Aenean egestas augue non velit feugiat ultrices.",
                    "option_b": "Maecenas ut nisi nec odio viverra porta tempus non eros.",
                    "option_c": "Mauris vel lectus et eros venenatis sollicitudin consequat id ex.",
                    "option_d": "Integer vestibulum lorem in magna luctus, nec ultrices magna eleifend.",
                    "question_id": 2045,
                    "question_text": "Integer pretium massa bibendum ullamcorper congue.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The laws passed after the Glorious Revolution are the beginning of what is called \u201a\u00c4\u00f2constitutional monarchy\u201a\u00c4\u00f4. The monarch remained very important but was no longer able to insist on particular policies or actions if Parliament did not agree. After William III, the ministers gradually became more important than the monarch but this was not a democracy in the modern sense. The number of people who had the right to vote for members of Parliament was still very small. Only men who owned property of a certain value were able to vote. No women at all had the vote. Some constituencies were controlled by a single wealthy family. These were called \u201a\u00c4\u00f2pocket boroughs\u201a\u00c4\u00f4. Other constituencies had hardly any voters and were called \u201a\u00c4\u00f2rotten boroughs\u201a\u00c4\u00f4."
                    ]
                },
                "id": "rec8Vjom3aZ0VpYHl"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recWEwUTqv82HNzK2"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Morbi at sem id est lobortis imperdiet ac vitae sapien.",
                    "option_a": "Vivamus in lacus id tellus blandit cursus.",
                    "option_b": "Sed id dui id metus tincidunt porta ut id leo.",
                    "option_c": "Morbi at sem id est lobortis imperdiet ac vitae sapien.",
                    "option_d": "Pellentesque fermentum mi sed tortor lacinia, ac tempus ante tincidunt.",
                    "question_id": 1946,
                    "question_text": "Phasellus sed sapien at magna porta volutpat at quis enim.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Notable British artists\n Thomas Gainsborough (1727\u201a\u00c4\u00ec88) was a portrait painter who often painted people in country or garden scenery.\n David Allan (1744\u201a\u00c4\u00ec96) was a Scottish painter who was best known for painting portraits. One of his most famous works is called The Origin of Painting.\n Joseph Turner (1775\u201a\u00c4\u00ec1851) was an influential landscape painter in a modern style. He is considered the artist who raised the profile of landscape painting.\n John Constable (1776\u201a\u00c4\u00ec1837) was a landscape painter most famous for his works of Dedham Vale on the Suffolk-Essex border in the east of England.\n The Pre-Raphaelites were an important group of artists in the second half of the 19th century. They painted detailed pictures on religious or literary themes in bright colours. The group included Holman Hunt, Dante Gabriel Rossetti and Sir John Millais.\n Sir John Lavery (1856\u201a\u00c4\u00ec1941) was a very successful Northern Irish portrait painter. His work included painting the Royal Family.\n Henry Moore (1898\u201a\u00c4\u00ec1986) was an English sculptor and artist. He is best known for his large bronze abstract sculptures."
                    ]
                },
                "id": "rec8fAXyUysotsM1y"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "C",
                        "D"
                    ],
                    "feedback": "In at quam efficitur, elementum sapien vel, imperdiet augue.",
                    "option_a": "Proin nec lacus sit amet est aliquam sodales tristique vel dui.",
                    "option_b": "Cras vulputate mauris ultrices justo tincidunt, ut convallis est eleifend.",
                    "option_c": "In at quam efficitur, elementum sapien vel, imperdiet augue.",
                    "option_d": "Phasellus in eros blandit, mollis nunc non, volutpat lorem.",
                    "question_id": 1761,
                    "question_text": "Quisque egestas dui non molestie pretium.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec8h6mMP2r6K9VgK"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Vivamus lacinia ligula sed scelerisque blandit.",
                    "option_a": "Donec vitae magna ac mauris semper sagittis eget et justo.",
                    "option_b": "Aliquam nec urna sit amet est condimentum vehicula.",
                    "option_c": "Vivamus lacinia ligula sed scelerisque blandit.",
                    "option_d": "Ut tristique nunc non turpis semper commodo.",
                    "question_id": 2031,
                    "question_text": "Sed sodales est ac sem pharetra euismod.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec8sHb9yTHyRFb8x"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recCUgReDYfYvLJgM"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Nam tincidunt felis quis erat viverra bibendum.",
                    "option_a": "Duis interdum mauris ac quam luctus, non auctor sem tempus.",
                    "option_b": "Curabitur eget velit vel metus vulputate bibendum id ut ipsum.",
                    "option_c": "Nam tincidunt felis quis erat viverra bibendum.",
                    "option_d": "Pellentesque ultrices mauris nec luctus dictum.",
                    "question_id": 1870,
                    "question_text": "Cras finibus mauris in tortor accumsan porta.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1997 the Labour Party led by Tony Blair was elected. The Blair government introduced a Scottish Parliament and a Welsh Assembly (see page 129). The Scottish Parliament has substantial powers to legislate. The Welsh Assembly was given fewer legislative powers but considerable control over public services. In Northern Ireland, the Blair government was able to build on the peace process, resulting in the Good Friday Agreement signed in 1998. The Northern Ireland Assembly was elected in 1999 but suspended in 2002. It was not reinstated until 2007. Most paramilitary groups in Northern Ireland have decommissioned their arms and are inactive. Gordon Brown took over as Prime Minister in 2007."
                    ]
                },
                "id": "rec8tqU7t09SRmNNy"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec6bnuwjmSfM9vi2"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Mauris sit amet dui a enim porttitor elementum a in velit.",
                    "option_a": "Sed eu leo a sem aliquet egestas.",
                    "option_b": "Vestibulum fringilla sapien in eros maximus, id egestas odio gravida.",
                    "option_c": "Mauris sit amet dui a enim porttitor elementum a in velit.",
                    "option_d": "Nam at enim gravida, vulputate risus at, feugiat nibh.",
                    "question_id": 1920,
                    "question_text": "Nullam laoreet sem at iaculis placerat.",
                    "status": "Approved",
                    "tell_me_more": [
                        "At the same time as defending Britain, the British military was fighting the Axis on many other fronts. In Singapore, the Japanese defeated the British and then occupied Burma, threatening India. The United States entered the war when the Japanese bombed its naval base at Pearl Harbour in December 1941."
                    ]
                },
                "id": "rec8w4rVtSPlmoUdD"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Ut tincidunt eros nec vehicula condimentum.",
                    "option_a": "Ut facilisis metus non dui egestas aliquam.",
                    "option_b": "Praesent pretium velit vel lectus tincidunt venenatis.",
                    "option_c": "Ut tincidunt eros nec vehicula condimentum.",
                    "option_d": "Nullam accumsan mauris id mauris sodales, id ultricies dolor lobortis.",
                    "question_id": 2052,
                    "question_text": "Phasellus varius mi at nibh iaculis, at volutpat lorem pulvinar.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "rec93xkXaAOZlIbn4"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "Pellentesque rutrum nibh vel mi dictum sagittis.",
                    "option_a": "Nunc placerat odio eget vehicula ornare.",
                    "option_b": "Ut non felis vel leo posuere condimentum sit amet vitae mauris.",
                    "option_c": "Pellentesque rutrum nibh vel mi dictum sagittis.",
                    "option_d": "In ac purus a massa bibendum efficitur sed at nisl.",
                    "question_id": 1817,
                    "question_text": "Fusce ut ex maximus, mattis diam quis, feugiat nisl.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "rec9AcCesmzB65Dvp"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rect8zlDQoCg3xfbG"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Etiam dapibus lectus hendrerit enim aliquam, vel pretium magna laoreet.",
                    "option_a": "Sed finibus lorem quis orci convallis faucibus.",
                    "option_b": "Fusce in purus vitae orci semper scelerisque.",
                    "option_c": "Etiam dapibus lectus hendrerit enim aliquam, vel pretium magna laoreet.",
                    "option_d": "Suspendisse at nunc eu metus euismod laoreet sit amet viverra mi.",
                    "question_id": 1729,
                    "question_text": "Phasellus quis nisl eu nisl dictum tempor.",
                    "status": "Approved",
                    "tell_me_more": [
                        "The laws passed after the Glorious Revolution are the beginning of what is called \u201a\u00c4\u00f2constitutional monarchy\u201a\u00c4\u00f4. The monarch remained very important but was no longer able to insist on particular policies or actions if Parliament did not agree. After William III, the ministers gradually became more important than the monarch but this was not a democracy in the modern sense. The number of people who had the right to vote for members of Parliament was still very small. Only men who owned property of a certain value were able to vote. No women at all had the vote. Some constituencies were controlled by a single wealthy family. These were called \u201a\u00c4\u00f2pocket boroughs\u201a\u00c4\u00f4. Other constituencies had hardly any voters and were called \u201a\u00c4\u00f2rotten boroughs\u201a\u00c4\u00f4."
                    ]
                },
                "id": "rec9HF1uYAV8FLHqp"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "B"
                    ],
                    "feedback": "Vivamus in urna feugiat, efficitur eros vel, vestibulum nulla.",
                    "option_a": "Morbi lobortis elit vel leo venenatis, eget porttitor elit auctor.",
                    "option_b": "Curabitur pretium enim id lorem vulputate, vitae iaculis purus malesuada.",
                    "question_id": 2217,
                    "question_text": "Vivamus in urna feugiat, efficitur eros vel, vestibulum nulla.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec9HbLJAUGi9JEnl"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "Sed semper nisi nec vehicula porttitor.",
                    "option_a": "Duis tincidunt ex imperdiet, posuere lorem a, commodo felis.",
                    "option_b": "Aenean in justo id ligula placerat mattis sed ac mauris.",
                    "option_c": "Sed semper nisi nec vehicula porttitor.",
                    "option_d": "In accumsan tortor at quam tincidunt dapibus.",
                    "question_id": 2103,
                    "question_text": "Vivamus finibus lacus non lectus mattis rhoncus.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec9SBaljC862zFHy"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Ut bibendum risus at purus rhoncus, sit amet imperdiet arcu porttitor.",
                    "option_a": "Suspendisse mattis neque quis feugiat vestibulum.",
                    "option_b": "Sed non leo dapibus, pretium nisi eu, accumsan risus.",
                    "option_c": "Ut bibendum risus at purus rhoncus, sit amet imperdiet arcu porttitor.",
                    "option_d": "Sed sed metus at metus hendrerit pellentesque quis et enim.",
                    "question_id": 2122,
                    "question_text": "Praesent facilisis ipsum ac lectus eleifend, id condimentum nibh convallis.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec9VbJvdX5apA72M"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recWEwUTqv82HNzK2"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Nulla eu arcu scelerisque, egestas enim egestas, pellentesque dui.",
                    "option_a": "Integer viverra turpis et velit hendrerit iaculis.",
                    "option_b": "Curabitur pulvinar dolor varius ante venenatis, nec rhoncus dolor placerat.",
                    "option_c": "Nulla eu arcu scelerisque, egestas enim egestas, pellentesque dui.",
                    "option_d": "Pellentesque ac risus quis metus venenatis elementum.",
                    "question_id": 2141,
                    "question_text": "Integer porttitor arcu non accumsan efficitur.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Notable British artists\n Thomas Gainsborough (1727\u201a\u00c4\u00ec88) was a portrait painter who often painted people in country or garden scenery.\n David Allan (1744\u201a\u00c4\u00ec96) was a Scottish painter who was best known for painting portraits. One of his most famous works is called The Origin of Painting.\n Joseph Turner (1775\u201a\u00c4\u00ec1851) was an influential landscape painter in a modern style. He is considered the artist who raised the profile of landscape painting.\n John Constable (1776\u201a\u00c4\u00ec1837) was a landscape painter most famous for his works of Dedham Vale on the Suffolk-Essex border in the east of England.\n The Pre-Raphaelites were an important group of artists in the second half of the 19th century. They painted detailed pictures on religious or literary themes in bright colours. The group included Holman Hunt, Dante Gabriel Rossetti and Sir John Millais.\n Sir John Lavery (1856\u201a\u00c4\u00ec1941) was a very successful Northern Irish portrait painter. His work included painting the Royal Family.\n Henry Moore (1898\u201a\u00c4\u00ec1986) was an English sculptor and artist. He is best known for his large bronze abstract sculptures."
                    ]
                },
                "id": "rec9XRPoIl5iA2F3b"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recCUgReDYfYvLJgM"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Curabitur vestibulum nibh eu felis vulputate cursus.",
                    "option_a": "Nam sit amet risus hendrerit, facilisis lectus ut, malesuada diam.",
                    "option_b": "Proin consequat justo sed ullamcorper vestibulum.",
                    "option_c": "Curabitur vestibulum nibh eu felis vulputate cursus.",
                    "option_d": "Donec vel turpis ultrices, posuere mauris ut, tempor magna.",
                    "question_id": 1991,
                    "question_text": "Morbi fermentum velit non nisi rhoncus, vitae blandit risus tincidunt.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1997 the Labour Party led by Tony Blair was elected. The Blair government introduced a Scottish Parliament and a Welsh Assembly (see page 129). The Scottish Parliament has substantial powers to legislate. The Welsh Assembly was given fewer legislative powers but considerable control over public services. In Northern Ireland, the Blair government was able to build on the peace process, resulting in the Good Friday Agreement signed in 1998. The Northern Ireland Assembly was elected in 1999 but suspended in 2002. It was not reinstated until 2007. Most paramilitary groups in Northern Ireland have decommissioned their arms and are inactive. Gordon Brown took over as Prime Minister in 2007."
                    ]
                },
                "id": "rec9bSIztHqIhhih3"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Sed finibus lorem quis orci convallis faucibus.",
                    "option_a": "Phasellus semper enim a volutpat tincidunt.",
                    "option_b": "Nunc in purus ac lectus facilisis laoreet.",
                    "option_c": "Sed finibus lorem quis orci convallis faucibus.",
                    "option_d": "Fusce in purus vitae orci semper scelerisque.",
                    "question_id": 1728,
                    "question_text": "Sed id orci ut augue tristique ultrices eget vel velit.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "rec9eLdz9jdRoysqy"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recfTFrUo79SGIhvU"
                    ],
                    "correct_answer": [
                        "C",
                        "D"
                    ],
                    "feedback": "Pellentesque facilisis mi sed dui molestie accumsan.",
                    "option_a": "Mauris sollicitudin urna aliquet pretium porttitor.",
                    "option_b": "Suspendisse interdum lorem nec tortor finibus suscipit.",
                    "option_c": "Pellentesque facilisis mi sed dui molestie accumsan.",
                    "option_d": "Duis vel lectus ac purus sollicitudin lobortis vitae a eros.",
                    "question_id": 1982,
                    "question_text": "Ut ac nisl at arcu pulvinar condimentum.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are many museums in the UK, which range from small community museums to large national and civic collections. Famous landmarks exist in towns, cities and the countryside throughout the UK. Most of them are open to the public to view (generally for a charge)."
                    ]
                },
                "id": "rec9sgQOxcVRPY5my"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "C",
                        "D"
                    ],
                    "feedback": "Proin molestie libero sed mauris viverra gravida fringilla non turpis.",
                    "option_a": "Nunc ut velit pulvinar, consequat mi sed, luctus lorem.",
                    "option_b": "Sed tempor dui nec ultricies blandit.",
                    "option_c": "Proin molestie libero sed mauris viverra gravida fringilla non turpis.",
                    "option_d": "Integer elementum odio at felis dignissim, ut cursus nisl consectetur.",
                    "question_id": 1852,
                    "question_text": "Morbi vitae augue at nulla ultricies vulputate sit amet at augue.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "rec9vFb7ETos2SGK6"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recN6N3OOPvSYlh5B"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Fusce convallis ex et tortor porta posuere.",
                    "option_a": "Cras iaculis sem in enim euismod sagittis.",
                    "option_b": "Ut bibendum risus at purus rhoncus, sit amet imperdiet arcu porttitor.",
                    "option_c": "Fusce convallis ex et tortor porta posuere.",
                    "option_d": "Nullam varius nisl vel iaculis feugiat.",
                    "question_id": 2118,
                    "question_text": "Nullam nec tortor venenatis, volutpat mi lobortis, porttitor justo.",
                    "status": "Approved",
                    "tell_me_more": [
                        "From the end of June 1940 until the German invasion of the Soviet Union in June 1941, Britain and the Empire stood almost alone against Nazi Germany."
                    ]
                },
                "id": "rec9wafXfpSiGFFoJ"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "D"
                    ],
                    "feedback": "Morbi in ligula varius, iaculis turpis sit amet, consequat felis.",
                    "option_a": "Donec convallis metus non odio ullamcorper, vitae venenatis arcu lacinia.",
                    "option_b": "Suspendisse quis augue euismod, sollicitudin lorem at, blandit urna.",
                    "option_c": "Morbi in ligula varius, iaculis turpis sit amet, consequat felis.",
                    "option_d": "Ut rhoncus enim in erat dapibus mattis.",
                    "question_id": 1999,
                    "question_text": "Sed non turpis euismod, sagittis est ac, semper lorem.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "recA3eV0uzrpoUPhO"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recCUgReDYfYvLJgM"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Ut rhoncus enim in erat dapibus mattis.",
                    "option_a": "Suspendisse quis augue euismod, sollicitudin lorem at, blandit urna.",
                    "option_b": "Quisque efficitur arcu at tellus aliquet varius.",
                    "option_c": "Ut rhoncus enim in erat dapibus mattis.",
                    "option_d": "Praesent ultricies metus ut dolor hendrerit consequat.",
                    "question_id": 2004,
                    "question_text": "Donec convallis metus non odio ullamcorper, vitae venenatis arcu lacinia.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1997 the Labour Party led by Tony Blair was elected. The Blair government introduced a Scottish Parliament and a Welsh Assembly (see page 129). The Scottish Parliament has substantial powers to legislate. The Welsh Assembly was given fewer legislative powers but considerable control over public services. In Northern Ireland, the Blair government was able to build on the peace process, resulting in the Good Friday Agreement signed in 1998. The Northern Ireland Assembly was elected in 1999 but suspended in 2002. It was not reinstated until 2007. Most paramilitary groups in Northern Ireland have decommissioned their arms and are inactive. Gordon Brown took over as Prime Minister in 2007."
                    ]
                },
                "id": "recANOkedf2L3jkIZ"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec6bnuwjmSfM9vi2"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Fusce id eros vitae quam porta fringilla eget vitae arcu.",
                    "option_a": "Mauris et ipsum vel felis suscipit commodo eget eu enim.",
                    "option_b": "Etiam posuere magna at nisi finibus mattis.",
                    "option_c": "Fusce id eros vitae quam porta fringilla eget vitae arcu.",
                    "option_d": "Nullam accumsan quam a sapien gravida, vel scelerisque lectus mollis.",
                    "question_id": 1907,
                    "question_text": "Proin ac urna auctor, malesuada lacus non, finibus nibh.",
                    "status": "Approved",
                    "tell_me_more": [
                        "At the same time as defending Britain, the British military was fighting the Axis on many other fronts. In Singapore, the Japanese defeated the British and then occupied Burma, threatening India. The United States entered the war when the Japanese bombed its naval base at Pearl Harbour in December 1941."
                    ]
                },
                "id": "recAS8cM5RboX8ma3"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "B"
                    ],
                    "feedback": "Vestibulum et mauris id erat egestas lobortis sed vel arcu.",
                    "option_a": "Proin id nisi sit amet purus lobortis gravida a eu erat.",
                    "option_b": "Donec id nisi ac massa viverra bibendum bibendum sed quam.",
                    "option_c": "Vestibulum et mauris id erat egestas lobortis sed vel arcu.",
                    "option_d": "Phasellus condimentum leo eget euismod elementum.",
                    "question_id": 1892,
                    "question_text": "Praesent tristique erat eu vulputate fermentum.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "recAtQutLGGhEp6aP"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recftETFxju2tPg3S"
                    ],
                    "correct_answer": [
                        "C",
                        "D"
                    ],
                    "feedback": "Nunc dapibus odio sit amet neque imperdiet condimentum.",
                    "option_a": "Fusce finibus purus vitae arcu malesuada blandit.",
                    "option_b": "Sed sit amet quam in ex pellentesque iaculis.",
                    "option_c": "Nunc dapibus odio sit amet neque imperdiet condimentum.",
                    "option_d": "Nunc vitae lectus tempor, sollicitudin turpis a, sodales purus.",
                    "question_id": 1826,
                    "question_text": "Vivamus a lacus hendrerit, accumsan urna in, laoreet nisi.",
                    "status": "Approved",
                    "tell_me_more": [
                        "Traditional foods\n There are a variety of foods that are traditionally associated with different parts of the UK:\n England: Roast beef, which is served with potatoes, vegetables, Yorkshire puddings (batter that is baked in the oven) and other accompaniments. Fish and chips are also popular.\n Wales: Welsh cakes \u201a\u00c4\u00ec a traditional Welsh snack made from flour, dried fruits and spices, and served either hot or cold.\n Scotland: Haggis \u201a\u00c4\u00ec a sheep\u201a\u00c4\u00f4s stomach stuffed with offal, suet, onions and oatmeal.\n Northern Ireland: Ulster fry \u201a\u00c4\u00ec a fried meal with bacon, eggs, sausage, black pudding, white pudding, tomatoes, mushrooms, soda bread and potato bread."
                    ]
                },
                "id": "recB3a8slMyLVMzj4"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Ut dignissim nisl vitae dolor convallis, et iaculis ipsum facilisis.",
                    "option_a": "Cras id lorem eget orci sodales ultrices id et lorem.",
                    "option_b": "Duis vitae quam ultrices, elementum massa malesuada, luctus lacus.",
                    "option_c": "Ut dignissim nisl vitae dolor convallis, et iaculis ipsum facilisis.",
                    "option_d": "Sed semper tortor non nisl pulvinar porta.",
                    "question_id": 2179,
                    "question_text": "Maecenas condimentum arcu ut est tristique finibus.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "recBD51EJKpuX4vd5"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "C"
                    ],
                    "feedback": "Fusce ut metus facilisis, ultrices mi vel, commodo eros.",
                    "option_a": "Vivamus rutrum mi a orci tristique tempus.",
                    "option_b": "Aenean ultrices mauris vitae congue bibendum.",
                    "option_c": "Fusce ut metus facilisis, ultrices mi vel, commodo eros.",
                    "option_d": "Aliquam in nunc cursus, consequat libero non, laoreet sapien.",
                    "question_id": 2162,
                    "question_text": "Cras volutpat augue nec vehicula fringilla.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "recBHM2oVCit2Ga9b"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "recoNnDFCrZWMBGf4"
                    ],
                    "correct_answer": [
                        "A"
                    ],
                    "feedback": "Fusce viverra mauris nec lacus eleifend porta.",
                    "option_a": "Nunc efficitur tellus a neque pellentesque, sed maximus ipsum consequat.",
                    "option_b": "Vivamus vel nunc sit amet nibh sodales elementum.",
                    "option_c": "Fusce viverra mauris nec lacus eleifend porta.",
                    "option_d": "Donec blandit nunc non dapibus suscipit.",
                    "question_id": 1793,
                    "question_text": "Phasellus lobortis eros sed nisl semper fringilla.",
                    "status": "Approved",
                    "tell_me_more": [
                        "There are people in the UK with ethnic origins from all over the world. In surveys, the most common ethnic description chosen is white, which includes people of European, Australian, Canadian, New Zealand and American descent. Other significant groups are those of Asian, black and mixed descent."
                    ]
                },
                "id": "recBZYHcuIO10NlYC"
            },
            {
                "createdTime": "2019-11-23T17:31:21.000Z",
                "fields": {
                    "chapter": "Chapter 5",
                    "citation_ref": [
                        "rec0dm0Lcs0rE98rZ"
                    ],
                    "correct_answer": [
                        "B"
                    ],
                    "feedback": "Vivamus quis ex placerat, vestibulum tellus ac, fermentum velit.",
                    "option_a": "Cras finibus tellus eget nibh elementum, pharetra molestie enim sagittis.",
                    "option_b": "Mauris euismod orci vel velit vehicula vestibulum.",
                    "option_c": "Vivamus quis ex placerat, vestibulum tellus ac, fermentum velit.",
                    "option_d": "Vivamus et urna vitae leo porta gravida.",
                    "question_id": 1918,
                    "question_text": "Nullam accumsan quam a sapien gravida, vel scelerisque lectus mollis.",
                    "status": "Approved",
                    "tell_me_more": [
                        "In 1837, Queen Victoria became queen of the UK at the age of 18. She reigned until 1901, almost 64 years. Her reign is known as the Victorian Age. It was a time when Britain increased in power and influence abroad. Within the UK, the middle classes because increasingly significant and a number of reformers led moves to improve conditions of life for the poor."
                    ]
                },
                "id": "recBZoc4eVZoY1rhm"
            }
        ]
}


def get_questions(base_id: str, key: str, offset=None) -> list:
    '''
        :params
        - base_id: Airtable Base ID
        - key : Airtable API KEY
        - offset: offset id from request to paginate resulsts
    '''

    # decide if have to offset
    offset = '&offset=' + offset if offset else ''
    # status filter and offset
    extra = '?filterByFormula=({status}="Approved")' + offset
    # build url
    url = f'https://api.airtable.com/v0/{base_id}/Questions' + extra
    # required headers to correctly authenticate
    headers = {'Authorization': 'Bearer ' + key}
    # everything together
    r = requests.get(url, headers=headers)

    # check if the request of successful
    if not r.ok:
        return {
            'success': False,
            'code': r.status_code,
            'content': r.reason
        }

    # convert the result into a dict
    json_response = json.loads(r.text)
    # extract the possible offset from response
    offset = json_response.get('offset')
    # get only the record list from response
    questions = json_response.get('records', list())

    # if there is more data, append to it. same process
    if offset:
        questions += get_questions(base_id, key, offset)['content']

    # return the question dict list
    return {
        'success': True,
        'code': r.status_code,
        'content': questions
    }
