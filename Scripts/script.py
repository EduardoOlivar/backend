from api.models import *
import random
#algebra, numeros, probabilidad, geometria
dataNumeros = [
{
            'name': 'Ensayo numeros',
            'type': 'numeros',
            'questions': [
                {
                    'question': '¿\\text{Cuál es el valor de: }(1 - \\frac{1}{2})(1 - \\frac{1}{3})(1 - \\frac{1}{4})(1 - \\frac{1}{5})?',
                    'subject': 'numeros',
                    'link_resolution':'https://youtube.com/embed/OxgnJ-IgxA0?start=124',
                    'answer': [
                        {
                            'label': '\\frac{1}{5}',
                            'right': 1
                        },
                        {
                            'label': '\\frac{119}{120}',
                            'right': 0
                        },
                        {
                            'label': '\\text{0}',
                            'right': 0
                        },
                        {
                            'label': '\\frac{599}{120}',
                            'right': 0
                        },

                    ],
                },
                {
                    'question': '¿\\text{Cuál es el valor de: }1 - (\\frac{1}{2})^{-3}?',
                    'subject': 'numeros',
                    'link_resolution':'https://youtube.com/embed/OxgnJ-IgxA0?start=383',
                    'answer': [
                        {
                            'label': '\\text{-7}',
                            'right': 1
                        },
                        {
                            'label': '\\frac{1}{2}',
                            'right': 0
                        },
                        {
                            'label': '\\frac{9}{8}',
                            'right': 0
                        },
                        {
                            'label': '\\frac{1}{8}',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '\\text{Un número aumentado en su 30% es igual a 910.}',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=1682',
                    'answer': [
                        {
                            'label': '\\text{700}',
                            'right': 1
                        },
                        {
                            'label': '\\text{637}',
                            'right': 0
                        },
                        {
                            'label': '\\text{273}',
                            'right': 0
                        },
                        {
                            'label': '\\text{1.183}',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '\\text{¿Cuál es el resultado de: }\sqrt{2} - \sqrt{8} + \sqrt{18}?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=1895',
                    'answer': [
                        {
                            'label': '2\sqrt{2}',
                            'right': 1
                        },
                        {
                            'label': '\sqrt{2}',
                            'right': 0
                        },
                        {
                            'label': '\sqrt{12}',
                            'right': 0
                        },
                        {
                            'label': '6\sqrt{2}',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '\\text{Si }\log_m\lparen\\frac {8} {125}\rparen\ = -3 \\text{, ¿cuál es el valor de m?}',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=2031',
                    'answer': [
                        {
                            'label': '\\frac {5} {2}',
                            'right': 1
                        },
                        {
                            'label': '\\frac {2} {5}',
                            'right': 0
                        },
                        {
                            'label': '{\lparen\\frac {8} {125}\rparen}^{-3}',
                            'right': 0
                        },
                        {
                            'label': '-\\frac {2} {5}',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': 'text{¿Cuál de las siguientes cantidades corresponde al 5} \%\\newline \\text{del precio de un artículo? }',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=1540',
                    'answer': [
                        {
                            'label': '\\text{El precio del artículo divido por 100, y luego multiplicado por 5}',
                            'right': 1
                        },
                        {
                            'label': '\\text{Un quinto del precio del artículo.}',
                            'right': 0
                        },
                        {
                            'label': '\\text{El precio del artículo multiplicado por cinco décimos}',
                            'right': 0
                        },
                        {
                            'label': '\\text{El precio del artículo divido por 5, y luego multiplicado por 100}',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '\\text{¿Cuál es el valor de 2,32 + 17,4?}',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/nKR73i6zASg?start=38',
                    'answer': [
                        {
                            'label': '\\text{(232 + 1740):100}',
                            'right': 1
                        },
                        {
                            'label': '\\text{(232 + 174):10}',
                            'right': 0
                        },
                        {
                            'label': '\\text{(2320 + 174):100}',
                            'right': 0
                        },
                        {
                            'label': '\\text{(232 + 1740):1000}',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '\\text{¿Cuál de las siguientes expresiones representa el 22\% }\\newline \\text{del 15\% de P?}',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/nKR73i6zASg?start=577',
                    'answer': [
                        {
                            'label': '\\frac{33}{1000}P',
                            'right': 1
                        },
                        {
                            'label': '\\text{3,3P}',
                            'right': 0
                        },
                        {
                            'label': '\\text{0,37P}',
                            'right': 0
                        },
                        {
                            'label': '\\frac{33}{100}P',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '\\text{¿Cuál de las siguientes opciones presenta una resolución}\\newline \\text{correcta de } \\frac{27^\\frac{1}{3}}{8}*\\frac{16^\\frac{1}{2}}{9}?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/nKR73i6zASg?start=755',
                    'answer': [
                        {
                            'label': '\\frac{27^\\frac{1}{3}}{8}*\\frac{16^\\frac{1}{2}}{9} =\\frac{(27^3)^\\frac{1}{3}}{8}*\\frac{(4^2)\\frac{1}{2}}{9} = \\frac{3}{8}*\\frac{4}{9} = \\frac{12}{72} = \\frac{1}{6}',
                            'right': 1
                        },
                        {
                            'label': '\\frac{27^\\frac{1}{3}}{8}*\\frac{16^\\frac{1}{2}}{9} = (\\frac{27}{8})^\\frac{1}{3}*(\\frac{16}{9})^\\frac{1}{2} = \\frac{3}{2}*\\frac{4}{3} = 2',
                            'right': 0
                        },
                        {
                            'label': '\\frac{27^\\frac{1}{3}}{8}*\\frac{16^\\frac{1}{2}}{9} = (\\frac{27*16}{8*9})^{\\frac{1}{3}*\\frac{1}{2}} = 6^\\frac{1}{6}',
                            'right': 0
                        },
                        {
                            'label': '\\frac{27^\\frac{1}{3}}{8}*\\frac{16^\\frac{1}{2}}{9} = \\frac{27^\\frac{1}{3}*16^\\frac{1}{2}}{8*9} = \\frac{9}{8}*\\frac{8}{9} = 1',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '\\text{¿Cuál es el valor de } \sqrt{8}(\sqrt{18}-\sqrt{8})?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/nKR73i6zASg?start=1154',
                    'answer': [
                        {
                            'label': '\\text{4}',
                            'right': 1
                        },
                        {
                            'label': '\\text{8}',
                            'right': 0
                        },
                        {
                            'label': '\sqrt{80}',
                            'right': 0
                        },
                        {
                            'label': '\\text{80}',
                            'right': 0
                        },
                    ],
                },
            ],
    },
]
dataAlgebra = [
{
        'name': 'Ensayo algebra',
        'type': 'algebra',
        'questions': [
            {
                'question': '\\text{¿Cuál es el valor de x en la ecuación 0,3 + 10x = 0,5?}',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=4092',
                'answer': [
                    {
                        'label': '\\text{0,02}',
                        'right': 1
                    },
                    {
                        'label': '\\text{8}',
                        'right': 0
                    },
                    {
                        'label': '\\text{2}',
                        'right': 0
                    },
                    {
                        'label': '\\text{0,08}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{Un bidón tiene ocupada con gasolina la mitad de su} \\newline \\text{capacidad máxima.}\\newline \\text{Al agregar 8L de gasolina se llega a las }\\frac{5}{6} \\text{ partes de su}\\newline \\text{capacidad.}\\newline \\text{¿Cuál es la capacidad máxima del bidón?}',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=4290',
                'answer': [
                    {
                        'label': '\\text{24 L}',
                        'right': 1
                    },
                    {
                        'label': '\\text{10 L}',
                        'right': 0
                    },
                    {
                        'label': '\\text{12 L}',
                        'right': 0
                    },
                    {
                        'label': '\\text{20 L}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{Si} \log_2{(-2x + 3p)} = 3 \\text{y} \log_3{x +2p} = 1 \\newline \\text{¿Cuál es el valor de x-2p?}',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=5349',
                'answer': [
                    {
                        'label': '\\text{-5}',
                        'right': 1
                    },
                    {
                        'label': '\\frac{-13}{7}',
                        'right': 0
                    },
                    {
                        'label': '\\frac{-27}{7}',
                        'right': 0
                    },
                    {
                        'label': '\\text{3}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{Si } a * b = 10 \\text{ y } a^2 + b^2 = 29',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/jZGMcWoN-_M?start=582',
                'answer': [
                    {
                        'label': '\\text{9}',
                        'right': 1
                    },
                    {
                        'label': '\\text{19}',
                        'right': 0
                    },
                    {
                        'label': '\\text{29}',
                        'right': 0
                    },
                    {
                        'label': '\\text{49}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{Para que el doble de (a + c) sea igual a 18, le faltan 4}\\newline \\text{unidades, se expresa como}',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/jZGMcWoN-_M?start=1382',
                'answer': [
                    {
                        'label': '2(a + c) + 4 = 18',
                        'right': 1
                    },
                    {
                        'label': '2(a + c) - 4 = 18',
                        'right': 0
                    },
                    {
                        'label': '2a + c + 4 = 18',
                        'right': 0
                    },
                    {
                        'label': '4 - 2(a + c) = 18',
                        'right': 0
                    },

                ],
            },
        ],
    },
]


def poblarBd(data):
    for essay_data in data:
        question = essay_data.pop('questions')
        essay_object = Essay.objects.create(**essay_data)
        for question_data in question:
            answers = question_data.pop('answer')
            question_object = Question.objects.create(**question_data, essay=essay_object)
            for answer_data in answers:
                Answer.objects.create(**answer_data, question=question_object)


poblarBd(dataAlgebra)
poblarBd(dataNumeros)

# for essay in Essay.objects.filter():
#     print(essay.name)
#     for question_data in Question.objects.filter():
#         print(f'Pregunta>>>: ',question_data.question)
#         answers_list = []
#         for answer in Answer.objects.filter(question=question_data):
#             # print(answer)
#             answers_list.append(answer)
#         random_answer = random.choice(answers_list)
#         print(f'Respuesta>>>: ', random_answer.right)
#         random_answer.essay.add(essay)
