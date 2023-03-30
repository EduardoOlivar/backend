from api.models import *
# -*- coding: utf-8 -*-
import random
#algebra, numeros, probabilidad, geometria
dataNumeros = [
{
            'name': 'Ensayo numeros',
            'type': 'numeros',
            'questions': [
                {
                    'question': 'Cual es el valor de: [\\\(1 - \\frac{1}{2})(1 - \\frac{1}{3})(1 - \\frac{1}{4})(1 - \\frac{1}{5})] ',
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
                    'question': 'Cual es el valor de: [1 - (\\frac{1}{2})^{-3}]?',
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
                    'question': 'Un numero aumentado en su 30% es igual a 910.',
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
                    'question': 'Cual es el resultado de: [\sqrt{2} - \sqrt{8} + \sqrt{18}]',
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
                    'question': 'Si [\log_m\lparen\\frac {8} {125}\\rparen\ = -3] , ¿cual es el valor de m?',
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
                            'label': '{\lparen\\frac {8} {125}\\rparen}^{-3}',
                            'right': 0
                        },
                        {
                            'label': '-\\frac {2} {5}',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '¿Cual de las siguientes cantidades corresponde al 5% del precio de un articulo? ',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=1540',
                    'answer': [
                        {
                            'label': '\\text{El precio del articulo divido por 100, y luego multiplicado por 5}',
                            'right': 1
                        },
                        {
                            'label': '\\text{Un quinto del precio del articulo.}',
                            'right': 0
                        },
                        {
                            'label': '\\text{El precio del articulo multiplicado por cinco decimos}',
                            'right': 0
                        },
                        {
                            'label': '\\text{El precio del articulo divido por 5, y luego multiplicado por 100}',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '¿Cual es el valor de 2,32 + 17,4?',
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
                    'question': '¿Cual de las siguientes expresiones representa el 22% del 15% de P?',
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
                    'question': '¿Cual de las siguientes opciones presenta una resolucion correcta de [\\frac{27^\\frac{1}{3}}{8}*\\frac{16^\\frac{1}{2}}{9}]?',
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
                    'question': '¿Cual es el valor de [\sqrt{8}(\sqrt{18}-\sqrt{8})]?',
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
                'question': '\\text{\\¿Cual es el valor de x en la ecuacion 0,3 + 10x = 0,5?}',
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
                'question': '\\text{Un bidon tiene ocupada con gasolina la mitad de su} \\newline \\text{capacidad maxima.}\\newline \\text{Al agregar 8L de gasolina se llega a las }\\frac{5}{6} \\text{ partes de su}\\newline \\text{capacidad.}\\newline \\text{\\¿Cual es la capacidad maxima del bidon?}',
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
                'question': '\\text{Si} \log_2{(-2x + 3p)} = 3 \\text{y} \log_3{x +2p} = 1 \\newline \\text{\\¿Cual es el valor de x-2p?}',
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
dataProbabilidades = [
     {
        'name': 'Ensayo probabilidades',
        'type': 'probabilidades',
        'questions': [
            {
                'question': '\\text{El dinero total que tienen ahorrado tres amigas es }\\newline \$210.000 \\text{. Se sabe que Claudia aporto el doble que Maria y} \\newline \\text{que Yasna aporto el doble que Claudia.}\\newline \\text{\\¿Cual es el primedio de dinero aportado por Claudia y}\\newline \\text{Yasna?}',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=13136',
                'answer': [
                    {
                        'label': '\$90.000',
                        'right': 1
                    },
                    {
                        'label': '\$70.000',
                        'right': 0
                    },
                    {
                        'label': '\$45.000',
                        'right': 0
                    },
                    {
                        'label': '\$35.000',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{En la siguiente tabla se muestra la distribucion de las}\\newline \\text{edades, en años, de un grupo de niños.} \\newline \\begin{array}{c:c} \\text{Edad} & \\text{Frecuencia} \\newline \\hline 2 & 5 \\newline \\hdashline 3 & 6 \\newline \\hdashline 4 & 9 \\newline \\hdashline 5 & 3 \\newline \\hline \\end{array} \\newline \\text{\\¿Cual es la mediana de edad de este grupo de niños?}',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=13314',
                'answer': [
                    {
                        'label': '\\text{4 años}',
                        'right': 1
                    },
                    {
                        'label': '\\text{3,5 años}',
                        'right': 0
                    },
                    {
                        'label': '\\text{7,5 años}',
                        'right': 0
                    },
                    {
                        'label': '\\text{9 años}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{Al lanzar un dado cargado, numerado del 1 al 6, la}\\newline \\text{probabilidad de que salga un numero par es el doble de la}\\newline \\text{probabilidad de que salga un numero impar.}\\newline \\text{Si se lanza este dado, \\¿cual es la probabilidad de que salga}\\newline \\text{un numero impar?}',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=14765',
                'answer': [
                    {
                        'label': '\\frac{1}{3}',
                        'right': 1
                    },
                    {
                        'label': '\\frac{1}{9}',
                        'right': 0
                    },
                    {
                        'label': '\\frac{2}{3}',
                        'right': 0
                    },
                    {
                        'label': '\\frac{2}{9}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{En un mazo de cartas de naipes ingles (52 cartas), 13 de}\\newline \\text{ ellas son de trebol. Si se extraen del mazo dos cartas al }\\newline \\text{azar, una despues de la otra y sin reposicion, \\¿cual es la }\\newline \\text{probabilidad de que ambas sean de trebol?}',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=14941',
                'answer': [
                    {
                        'label': '\\frac{13}{52} *\\frac{12}{51}',
                        'right': 1
                    },
                    {
                        'label': '\\frac{13}{52} *\\frac{12}{52}',
                        'right': 0
                    },
                    {
                        'label': '\\frac{13}{52} +\\frac{12}{52}',
                        'right': 0
                    },
                    {
                        'label': '\\frac{13}{52} +\\frac{12}{51}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{Un estudiante constesta una prueba en que cada pregunta}\\newline \\text{tiene 5 opciones solo una de ellas es la correcta.}\\newline \\text{Si responde las 3 ultimas preguntas al azar y de manera}\\newline \\text{independiente, \\¿cual es la probabilidad de tener estas 3 }\\newline \\text{respuestas correctas?}',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=15047',
                'answer': [
                    {
                        'label': '(\\frac{1}{5})^3',
                        'right': 1
                    },
                    {
                        'label': '\\frac{3}{15}',
                        'right': 0
                    },
                    {
                        'label': '\\frac{3}{5}',
                        'right': 0
                    },
                    {
                        'label': '3*(\\frac{1}{5})^3',
                        'right': 0
                    },

                ],
            },
        ]
    },
]
dataGeometria = [
     {
        'name': 'Ensayo geometria',
        'type': 'geometria',
        'questions': [
            {
                'question': '\\text{Sean A(1,1), B(5,3) y C los vertices de un triangulo.}\\newline \\text{Se pueden determinar las coordenadas del vertice C}\\newline \\text{del triangulo si se sabe que:} \\newline \\text{(1) Angulo BAC = 90°}\\newline \\text{(2) El triangulo es isosceles y el vertice C esta en el cuarto}\\newline \\text{cuadrante.}',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=12325',
                'answer': [
                    {
                        'label': '\\text{Ambas juntas, (1) y (2)}',
                        'right': 1
                    },
                    {
                        'label': '\\text{(2) por si sola}',
                        'right': 0
                    },
                    {
                        'label': '\\text{(1) por si sola}',
                        'right': 0
                    },
                    {
                        'label': '\\text{Se requier informacion adicional}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{Considere los vectores} \\overrightarrow{u} = (-2,5), \\overrightarrow{v} = (3, -2) \\text{ y } \\newline \\overrightarrow{c} = (-1,-4).\\newline \\text{¿Cual es el vector } \\overrightarrow{u} + 2\\overrightarrow{v} - \\overrightarrow{c} \\text{?}',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=9560',
                'answer': [
                    {
                        'label': '\\text{(5,5)}',
                        'right': 1
                    },
                    {
                        'label': '\\text{(3,5)}',
                        'right': 0
                    },
                    {
                        'label': '\\text{(4,9)}',
                        'right': 0
                    },
                    {
                        'label': '\\text{(2,1)}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{Si el punto (a,b) es la imagen que se obtiene al trasladar}\\newline \\text{el punto R segun el vector (m,n), ¿cuales son las}\\newline \\text{coordenadas de R?}',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=9691',
                'answer': [
                    {
                        'label': '\\text{(a - m, b - n)}',
                        'right': 1
                    },
                    {
                        'label': '\\text{(am, bn)}',
                        'right': 0
                    },
                    {
                        'label': '\\text{(m - a, n - b)}',
                        'right': 0
                    },
                    {
                        'label': '\\text{(a + m, b + n)}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{Con un cordel de largo d se forma un cuadrado. ¿Cuanto }\\newline \\text{mide el area del un cuadrado?}',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/m4qRM2mtjHA?start=480',
                'answer': [
                    {
                        'label': '\\frac{d^2}{16}',
                        'right': 1
                    },
                    {
                        'label': '\\frac{d^2}{2}',
                        'right': 0
                    },
                    {
                        'label': '\\frac{d^2}{4}',
                        'right': 0
                    },
                    {
                        'label': '\\frac{d^2}{8}',
                        'right': 0
                    },

                ],
            },
            {
                'question': '\\text{Un estudiante constesta una prueba en que cada pregunta}\\newline \\text{tiene 5 opciones solo una de ellas es la correcta.}\\newline \\text{Si responde las 3 ultimas preguntas al azar y de manera}\\newline \\text{independiente, ¿cual es la probabilidad de tener estas 3 }\\newline \\text{respuestas correctas?}',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/m4qRM2mtjHA?start=2631',
                'answer': [
                    {
                        'label': '\\sqrt{96}',
                        'right': 1
                    },
                    {
                        'label': '\\sqrt{104}',
                        'right': 0
                    },
                    {
                        'label': '\\sqrt{46}',
                        'right': 0
                    },
                    {
                        'label': '\\sqrt{21}',
                        'right': 0
                    },

                ],
            },
        ]
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
poblarBd(dataProbabilidades)
poblarBd(dataGeometria)

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
