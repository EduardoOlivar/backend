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
                    'question': '¿Cual es el valor de: [(1 - \\frac{1}{2})(1 - \\frac{1}{3})(1 - \\frac{1}{4})(1 - \\frac{1}{5})]?',
                    'subject': 'numeros',
                    'link_resolution':'https://youtube.com/embed/OxgnJ-IgxA0?start=124',
                    'answer': [
                        {
                            'label': '[\\frac{1}{5}]',
                            'right': 1
                        },
                        {
                            'label': '[\\frac{119}{120}]',
                            'right': 0
                        },
                        {
                            'label': '[0]',
                            'right': 0
                        },
                        {
                            'label': '[\\frac{599}{120}]',
                            'right': 0
                        },

                    ],
                },
                {
                    'question': '¿Cual es el valor de: [1 - (\\frac{1}{2})^{-3}]?',
                    'subject': 'numeros',
                    'link_resolution':'https://youtube.com/embed/OxgnJ-IgxA0?start=383',
                    'answer': [
                        {
                            'label': '[-7]',
                            'right': 1
                        },
                        {
                            'label': '[\\frac{1}{2}]',
                            'right': 0
                        },
                        {
                            'label': '[\\frac{9}{8}]',
                            'right': 0
                        },
                        {
                            'label': '[\\frac{1}{8}]',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': 'Un numero aumentado en su [30%] es igual a [910].',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=1682',
                    'answer': [
                        {
                            'label': '[700]',
                            'right': 1
                        },
                        {
                            'label': '[637]',
                            'right': 0
                        },
                        {
                            'label': '[273]',
                            'right': 0
                        },
                        {
                            'label': '[1.183]',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '¿Cual es el resultado de: [\sqrt{2} - \sqrt{8} + \sqrt{18}] ',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=1895',
                    'answer': [
                        {
                            'label': '2[\sqrt{2}]',
                            'right': 1
                        },
                        {
                            'label': '[\sqrt{2}]',
                            'right': 0
                        },
                        {
                            'label': '[\sqrt{12}]',
                            'right': 0
                        },
                        {
                            'label': '6[\sqrt{2}]',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': 'Si [\log_m\lparen\\frac {8} {125}\\rparen\ = -3], ¿cual es el valor de m?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=2031',
                    'answer': [
                        {
                            'label': '[\\frac {5} {2}]',
                            'right': 1
                        },
                        {
                            'label': '[\\frac {2} {5}]',
                            'right': 0
                        },
                        {
                            'label': '[{\lparen\\frac {8} {125}\\rparen}^{-3}]',
                            'right': 0
                        },
                        {
                            'label': '-[\\frac {2} {5}]',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '¿Cual de las siguientes cantidades corresponde al [5%] del precio de un articulo? ',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=1540',
                    'answer': [
                        {
                            'label': 'El precio del articulo divido por [100], y luego multiplicado por [5]',
                            'right': 1
                        },
                        {
                            'label': 'Un quinto del precio del articulo.',
                            'right': 0
                        },
                        {
                            'label': 'El precio del articulo multiplicado por cinco decimos',
                            'right': 0
                        },
                        {
                            'label': 'El precio del articulo divido por [5], y luego multiplicado por [100]',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '¿Cual es el valor de [2,32 + 17,4]?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/nKR73i6zASg?start=38',
                    'answer': [
                        {
                            'label': '[(232 + 1740):100]',
                            'right': 1
                        },
                        {
                            'label': '[(232 + 174):10]',
                            'right': 0
                        },
                        {
                            'label': '[(2320 + 174):100]',
                            'right': 0
                        },
                        {
                            'label': '[(232 + 1740):1000]',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '¿Cual de las siguientes expresiones representa el [22%]  del [15%] de P?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/nKR73i6zASg?start=577',
                    'answer': [
                        {
                            'label': '[\\frac{33}{1000}P]',
                            'right': 1
                        },
                        {
                            'label': '[3,3P]',
                            'right': 0
                        },
                        {
                            'label': '[0,37P]',
                            'right': 0
                        },
                        {
                            'label': '[\\frac{33}{100}P]',
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
                            'label': '[\\frac{27^\\frac{1}{3}}{8}*\\frac{16^\\frac{1}{2}}{9} =\\frac{(27^3)^\\frac{1}{3}}{8}*\\frac{(4^2)\\frac{1}{2}}{9} = \\frac{3}{8}*\\frac{4}{9} = \\frac{12}{72} = \\frac{1}{6}]',
                            'right': 1
                        },
                        {
                            'label': '[\\frac{27^\\frac{1}{3}}{8}*\\frac{16^\\frac{1}{2}}{9} = (\\frac{27}{8})^\\frac{1}{3}*(\\frac{16}{9})^\\frac{1}{2} = \\frac{3}{2}*\\frac{4}{3} = 2]',
                            'right': 0
                        },
                        {
                            'label': '[\\frac{27^\\frac{1}{3}}{8}*\\frac{16^\\frac{1}{2}}{9} = (\\frac{27*16}{8*9})^{\\frac{1}{3}*\\frac{1}{2}} = 6^\\frac{1}{6}]',
                            'right': 0
                        },
                        {
                            'label': '[\\frac{27^\\frac{1}{3}}{8}*\\frac{16^\\frac{1}{2}}{9} = \\frac{27^\\frac{1}{3}*16^\\frac{1}{2}}{8*9} = \\frac{9}{8}*\\frac{8}{9} = 1]',
                            'right': 0
                        },
                    ],
                },
                {
                    'question': '¿Cual es el valor de [\sqrt{8}]([\sqrt{18}]-[\sqrt{8})]?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/nKR73i6zASg?start=1154',
                    'answer': [
                        {
                            'label': '[4]',
                            'right': 1
                        },
                        {
                            'label': '[8]',
                            'right': 0
                        },
                        {
                            'label': '[\sqrt{80}]',
                            'right': 0
                        },
                        {
                            'label': '[80]',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': 'Por el arriendo de un juego inflable se cobra una cuota fija de $120.000 por cuatro horas, más $25.000 por cada hora adicional.[\\newline]¿Cuántas horas como máximo puede arrendar una empresa el juego inflable si tiene un presupuesto de $240.000 para este efecto?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=6',
                    'answer': [
                        {
                            'label': '[8]',
                            'right': 1
                        },
                        {
                            'label': '[4]',
                            'right': 0
                        },
                        {
                            'label': '[9]',
                            'right': 0
                        },
                        {
                            'label': '[10]',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': 'Considera el númerop distinto de cero que es multiplicado dos veces por 1,25 y luego, dos veces por 0,75, tal como se representa a continuación:[\\newline p\\cdot1,25\\cdot1,25\\cdot0,75\\cdot0,75 \\newline] ¿Qué pueden representar dichas multiplicaciones, respecto del número original [p] ?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=71',
                    'answer': [
                        {
                            'label': 'Que hubo dos aumentos del 25 % y luego, dos disminuciones del 25 %',
                            'right': 1
                        },
                        {
                            'label': 'Que no hubo aumento de p ni disminución de p',
                            'right': 0
                        },
                        {
                            'label': 'Que hubo dos aumentos de 0,25 y luego, dos disminuciones de 0,75',
                            'right': 0
                        },
                        {
                            'label': 'Que hubo dos aumentos del 25 % y luego, dos disminuciones del 75 %',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': 'La automotora “Mi auto” tiene cinco marcas de automóviles, cada marca tiene tres modelos y cada modelo está en tres colores distintos.[\\newline]La automotora “Viaje feliz” tiene cuatro marcas de automóviles, cada marca tiene tres modelos y cada modelo en cuatro colores distintos.[\\newline] Si las marcas de los automóviles de las automotoras son distintas entre sí, ¿cuál de las siguientes afirmaciones es verdadera?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=71',
                    'answer': [
                        {
                            'label': 'La automotora “Viaje feliz” ofrece tres posibilidades distintas más para elegir un automóvil que la automotora “Mi auto”',
                            'right': 1
                        },
                        {
                            'label': 'Ambas automotoras ofrecen la misma cantidad de posibilidades distintas para elegir un automóvil',
                            'right': 0
                        },
                        {
                            'label': 'La automotora “Mi auto” ofrece más posibilidades distintas para elegir un automóvil que la automotora “Viaje feliz”',
                            'right': 0
                        },
                        {
                            'label': 'El total de las distintas posibilidades de elegir un automóvil está determinado por la suma entre la cantidad de marcas, de modelos y de colores',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': 'El modelo RVA de colores, permite crear cualquier color mediante la mezcla de los distintos tonos de tres olores: rojo, verde y azul. Los valores de la intensidad decada uno de estos colores van desde el 0 al 255 y cada color creado tiene un código de tres números donde el primero representa al rojo, el segundo al verde y el tercero al azul.[\\newline]El código de la mezcla de dos colores se obtiene haciendo el promedio de cada uno de los valores de los colores originales tal como se presenta a continuación:[\\newline \\begin{array}{c:c} \\text{Colores para mezclar} & \\text{Color resultante} \\newline \\hline (a,b,c),(m,n,t) & (\\frac{a + m}{2} \\cdot \\frac{b + n}{2} \\cdot \\frac{c + t}{2}) \\newline \\hline \\end{array} \\newline]¿Con qué color hay que mezclar el color (160, 60, 120) para obtener el color (170, 80, 60)?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=298',
                    'answer': [
                        {
                            'label': '(180,100,0)',
                            'right': 1
                        },
                        {
                            'label': '(180,100,60)',
                            'right': 0
                        },
                        {
                            'label': '(10,20,60)',
                            'right': 0
                        },
                        {
                            'label': '(165,70,90)',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': 'En la temporada de invierno, la diferencia horaria entre Nueva Zelanda y Chile es de 16 h , desde Chile. Por ejemplo, si en Chile son las 11 de la mañana de un lunes, en Nueva Zelanda son las 3 de la mañana del martes.[\\newline]En la misma temporada la diferencia horaria entre México y Chile es de -1 h , desde Chile. Es decir, cuando en Chile son las 11 de la mañana de un lunes, en México son las 10 de la mañana del mismo día.[\\newline]¿Cuál es la diferencia horaria entre Nueva Zelanda y México, desde México, en la temporada de invierno?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=430',
                    'answer': [
                        {
                            'label': '17',
                            'right': 1
                        },
                        {
                            'label': '-17',
                            'right': 0
                        },
                        {
                            'label': '-15',
                            'right': 0
                        },
                        {
                            'label': '15',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': 'Un comerciante compra una cantidad de naranjas a razón de 3 kilogramos por $600 y las vende todas a razón de 4 kilogramos por $1000.[\\newline]Si obtuvo una ganancia de $3000 , ¿cuántos kilogramos de naranjas compró?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=500',
                    'answer': [
                        {
                            'label': '60',
                            'right': 1
                        },
                        {
                            'label': '25',
                            'right': 0
                        },
                        {
                            'label': '12',
                            'right': 0
                        },
                        {
                            'label': '8',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': '¿Cuál es el [40%] del [15%] de 300 ?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=611',
                    'answer': [
                        {
                            'label': '18',
                            'right': 1
                        },
                        {
                            'label': '75',
                            'right': 0
                        },
                        {
                            'label': '165',
                            'right': 0
                        },
                        {
                            'label': '180',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': 'Si el precio de un helado es $500 , ¿cuál de las siguientes expresiones representa el valor del helado aumentado en su [120%]?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=653',
                    'answer': [
                        {
                            'label': '[2,2 \\codt 500]',
                            'right': 1
                        },
                        {
                            'label': '[1,2 \\codt 500]',
                            'right': 0
                        },
                        {
                            'label': '[50 + 20 \\codt 500]',
                            'right': 0
                        },
                        {
                            'label': '[50 + 120 \\codt 500]',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': '¿Qué porcentaje es 4740 de 15800 ?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=814',
                    'answer': [
                        {
                            'label': '[30%]',
                            'right': 1
                        },
                        {
                            'label': '[3,\\bar{3}%]',
                            'right': 0
                        },
                        {
                            'label': '[3%]',
                            'right': 0
                        },
                        {
                            'label': '[0,3%]',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': 'Un profesor ve algunos resultados de una encuesta por internet realizada a 100 personas un determinado día, de las cuales el [25 %] omitió la última pregunta.Una semana después se realiza la misma encuesta a otras 100 personas, de las cuales un [35 %] omitió la última pregunta.[\\newline]El profesor le pide a cuatro de sus estudiantes que realicen conclusiones de estos datos.[\\newline \\bullet]Sebastián señala: del total de personas encuestadas un [60 %] omitió la última pregunta.[\\newline \\bullet]Angélica señala: en la segunda encuesta la omisión total tuvo un aumento de 10 puntos porcentuales con respecto a la omisión total de la primera encuesta.[\\newline \\bullet]Luisa señala: del total de personas encuestadas 60 personas omitieron la última pregunta.[\\newline \\bullet]Manuel señala: en la segunda encuesta la pregunta más omitida fue la última.[\\newline]¿Cuál de ellos está en lo correcto?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=857',
                    'answer': [
                        {
                            'label': 'Luisa',
                            'right': 1
                        },
                        {
                            'label': 'Angélica',
                            'right': 0
                        },
                        {
                            'label': 'Manuel',
                            'right': 0
                        },
                        {
                            'label': 'Sebastián',
                            'right': 0
                        },
                    ],
                },
                {#PAES 2023 M1 FORMA 113
                    'question': 'En un estudio realizado a un grupo de 25 personas, se les consultó por su bebida favorita, de entre cuatro disponibles (Almíbar, Refrescante, Quitased y Frutirico).En la tabla adjunta se presentan los resultados obtenidos.[\\newline \\newline \\begin{array}{c:c} \\text{Bebida} & \\text{Cantidad de personas} \\newline \\hline Almíbar & 12 \\newline \\hdashline Refrescante & 4 \\newline \\hdashline Quitased & 8 \\newline \\hdashline Frutirico & 1 \\newline \\hline \\end{array} \\newline][\\newline]¿Cuál de las siguientes afirmaciones es verdadera?',
                    'subject': 'numeros',
                    'link_resolution':'https://www.youtube.com/embed/2nghljBMp1k?start=753',
                    'answer': [
                        {
                            'label': 'El [80%] de las personas prefiere la bebida Almíbar o la bebida Quitased.',
                            'right': 1
                        },
                        {
                            'label': 'Un [0,16%] de las personas prefiere la bebida Refrescante.',
                            'right': 0
                        },
                        {
                            'label': 'Las personas que prefieren la bebida Frutirico representan un [1%] de las personas que prefieren la bebida Quitased.',
                            'right': 0
                        },
                        {
                            'label': 'Las personas que prefieren la bebida Almíbar o la bebida Frutirico representan menos del [50%] del total de personas.',
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
                'question': '¿Cual es el valor de [x] en la ecuacion [0,3 + 10x = 0,5]?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=4092',
                'answer': [
                    {
                        'label': '[0,02]',
                        'right': 1
                    },
                    {
                        'label': '[8]',
                        'right': 0
                    },
                    {
                        'label': '[2]',
                        'right': 0
                    },
                    {
                        'label': '[0,08]',
                        'right': 0
                    },

                ],
            },
            {
                'question': 'Un bidon tiene ocupada con gasolina la mitad de su capacidad maxima. Al agregar 8L de gasolina se llega a las [\\frac{5}{6}] partes de su capacidad. ¿Cual es la capacidad maxima del bidon?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=4290',
                'answer': [
                    {
                        'label': '[24 L]',
                        'right': 1
                    },
                    {
                        'label': '[10 L]',
                        'right': 0
                    },
                    {
                        'label': '[12 L]',
                        'right': 0
                    },
                    {
                        'label': '[20 L]',
                        'right': 0
                    },

                ],
            },
            {
                'question': 'Si [\log_2{(-2x + 3p)} = 3] y [\log_3{x +2p} = 1] ¿Cual es el valor de x-2p?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=5349',
                'answer': [
                    {
                        'label': '[-5]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{-13}{7}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{-27}{7}]',
                        'right': 0
                    },
                    {
                        'label': '[3]',
                        'right': 0
                    },

                ],
            },
            {
                'question': 'Si  [a * b = 10] y [a^2 + b^2 = 29]',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/jZGMcWoN-_M?start=582',
                'answer': [
                    {
                        'label': '[9]',
                        'right': 1
                    },
                    {
                        'label': '[19]',
                        'right': 0
                    },
                    {
                        'label': '[29]',
                        'right': 0
                    },
                    {
                        'label': '[49]',
                        'right': 0
                    },

                ],
            },
            {
                'question': 'Para que el doble de [(a + c)] sea igual a [18], le faltan [4] unidades, se expresa como:',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/jZGMcWoN-_M?start=1382',
                'answer': [
                    {
                        'label': '[2(a + c) + 4 = 18]',
                        'right': 1
                    },
                    {
                        'label': '[2(a + c) - 4 = 18]',
                        'right': 0
                    },
                    {
                        'label': '[2a + c + 4 = 18]',
                        'right': 0
                    },
                    {
                        'label': '[4 - 2(a + c) = 18]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'La expresión [(a + 2)^{2} + (a + 1)(a - 3)] se factoriza como el producto de dos factores, tal que uno de ellos es [(a + 1)].[\\newline]¿Cuál de las siguientes expresiones corresponde al otro factor de la expresión?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/fhSir6Yd4pQ?start=196',
                'answer': [
                    {
                        'label': '[(2a - 2)]',
                        'right': 1
                    },
                    {
                        'label': '[a^{2} - a - 2]',
                        'right': 0
                    },
                    {
                        'label': '[a - 2]',
                        'right': 0
                    },
                    {
                        'label': '[a^{2} + 3a - 2]',
                        'right': 0
                    },
                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': '¿Cuál de las siguientes expresiones es igual que [(a + (b + c)) \\cdot (a + (b - c))]?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/fhSir6Yd4pQ?start=1',
                'answer': [
                    {
                        'label': '[a^{2} + 2ab + b^{2} - c^{2}]',
                        'right': 1
                    },
                    {
                        'label': '[a^{2} + b^{2} - c^{2}]',
                        'right': 0
                    },
                    {
                        'label': '[a^{2} + a^{2}b^{2} + b^{2} - c^{2}]',
                        'right': 0
                    },
                    {
                        'label': '[a^{2} + (b - c)^{2}]',
                        'right': 0
                    },
                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'En una tienda de mascotas se dispone de un monto máximo de $50000 para pagar la electricidad que se onsume en un mes.[\\newline]La empresa eléctrica que suministra este servicio realiza el cobro, en pesos, mediante la función [c(x) = 100x + 5000] , siendo [x] la cantidad de kWh consumidos en el mes.[\\newline]¿Cuál de los siguientes conjuntos contiene a todos y únicamente los posiblesvalores del consumo en kWh en el mes que se puede solventar con el montodisponible en esa tienda?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/fhSir6Yd4pQ?start=525',
                'answer': [
                    {
                        'label': '[\\lbrack 0, 450\\rbrack]',
                        'right': 1
                    },
                    {
                        'label': '[\\lbrack 0, 450\\lbrack]',
                        'right': 0
                    },
                    {
                        'label': '[\\lbrack 0, 550\\lbrack]',
                        'right': 0
                    },
                    {
                        'label': '[\\lbrack 0, 5500\\rbrack]',
                        'right': 0
                    },
                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'En una frutería cada durazno cuesta $480 y cada mango cuesta $400 . Una persona gastó $6800 en total comprando solo 16 frutas entre duraznos y mangos.[\\newline]¿Cuál de las siguientes ecuaciones permite determinar la cantidad [x] de duraznos que compró la persona?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/APzM_Ein_bE?start=2',
                'answer': [
                    {
                        'label': '[480x + 400(16 - x) = 6800]',
                        'right': 1
                    },
                    {
                        'label': '[480x + 400(x - 16) = 6800]',
                        'right': 0
                    },
                    {
                        'label': '[480x + 400x = 16]',
                        'right': 0
                    },
                    {
                        'label': '[(480 + 400)x = 6800 + 16]',
                        'right': 0
                    },
                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': '¿Cuáles son las soluciones de la ecuación [x^{2} -12x +35 = 0] ?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/APzM_Ein_bE?start=197',
                'answer': [
                    {
                        'label': '[7 y 5]',
                        'right': 1
                    },
                    {
                        'label': '[-7 y -5]',
                        'right': 0
                    },
                    {
                        'label': '[-14 y -10]',
                        'right': 0
                    },
                    {
                        'label': '[14 y 10]',
                        'right': 0
                    },
                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'Ignacio se dedica a vender productos encargados por sus clientes, que importa mediante una aplicación móvil. El precio de venta al que Ignacio vende los productos lo determina según la función [P(x) = 1,5x + 2500] , tal que [x] representa el precio, en pesos, al que compra el producto en la aplicación.[\\newline]¿Cuál de las siguientes afirmaciones es verdadera?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/APzM_Ein_bE?start=496',
                'answer': [
                    {
                        'label': 'Ignacio realiza un recargo de un [50%] del precio del producto importado sin considerar ese recargo en el cargo fijo.',
                        'right': 1
                    },
                    {
                        'label': 'Ignacio cobra un costo fijo de [$(1,5 + 2500)] a todos los productos que vende.',
                        'right': 0
                    },
                    {
                        'label': 'Ignacio cobra un costo fijo de [$1,5 \\cdot 2500)] a todos los productos que vende.',
                        'right': 0
                    },
                    {
                        'label': 'Ignacio realiza un recargo de [1,5%] del precio del producto importado sin considerar el cargo fijo.',
                        'right': 0
                    },
                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'En una distribuidora envasaron 360 L de detergente líquido en bidones de 3 L y de 5 L de capacidad.[\\newline]Si se ocuparon en total 100 bidones, ¿cuál de los siguientes valores es la diferencia entre la cantidad de bidones de distinta capacidad que se usaron?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/APzM_Ein_bE?start=550',
                'answer': [
                    {
                        'label': '[40]',
                        'right': 1
                    },
                    {
                        'label': '[25]',
                        'right': 0
                    },
                    {
                        'label': '[48]',
                        'right': 0
                    },
                    {
                        'label': '[50]',
                        'right': 0
                    },
                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'Considera la ecuación [3x - p = 2x + p + 1].[\\newline]¿Cuál es el menor valor que puede tomar x para que p sea un número entero positivo?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=762',
                'answer': [
                    {
                        'label': '[3]',
                        'right': 1
                    },
                    {
                        'label': '[0]',
                        'right': 0
                    },
                    {
                        'label': '[1]',
                        'right': 0
                    },
                    {
                        'label': '[2]',
                        'right': 0
                    },
                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'Considera el sistema [\\begin{rcases} ax + by + 1 = 0 \\newline bx + ay + 1 = 0 \\end{rcases}]., en x e y , con a y b números reales distintos entre sí, distintos de cero y [a \\mathrlap{/}{=} -b].[\\newline]¿Cuál es la solución del sistema?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=1083',
                'answer': [
                    {
                        'label': '[x = \\frac{-1}{a + b}; y = \\frac{-1}{a + b}]',
                        'right': 1
                    },
                    {
                        'label': '[x = \\frac{1}{a + b}; y = \\frac{1}{a + b}]',
                        'right': 0
                    },
                    {
                        'label': '[x = \\frac{-1}{a - b}; y = \\frac{-1}{a - b}]',
                        'right': 0
                    },
                    {
                        'label': '[x = \\frac{-1}{a + b}; y = \\frac{1}{a + b}]',
                        'right': 0
                    },
                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'Considera la ecuación [(x -3)(x - 4) = 2].[\\newline]¿Cuál de los siguientes argumentos es válido?',
                'subject': 'algebra',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=1083',
                'answer': [
                    {
                        'label': 'Las soluciones de la ecuación son [x = 2] y [x = 5] , porque [(2 - 3)(2 - 4) = 2] y [(5 - 3)(5 - 4) = 2].',
                        'right': 1
                    },
                    {
                        'label': 'La ecuación posee dos soluciones, porque [x = 3] y [x = 4] satisfacen la igualdad.',
                        'right': 0
                    },
                    {
                        'label': 'Las soluciones de la ecuación son ambas positivas, porque el discriminante asociado a la ecuación es positivo.',
                        'right': 0
                    },
                    {
                        'label': 'Las soluciones son [x = 2] y [x = 5] , porque ambos valores satisfacen la ecuación [x^{2} -7x +12 = 0].',
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
                'question': 'El dinero total que tienen ahorrado tres amigas es  [\$210.000]. Se sabe que Claudia aporto el doble que Maria y que Yasna aporto el doble que Claudia. ¿Cual es el promedio de dinero aportado por Claudia y Yasna?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=13136',
                'answer': [
                    {
                        'label': '[\$90.000]',
                        'right': 1
                    },
                    {
                        'label': '[\$70.000]',
                        'right': 0
                    },
                    {
                        'label': '[\$45.000]',
                        'right': 0
                    },
                    {
                        'label': '[\$35.000]',
                        'right': 0
                    },

                ],
            },
            {
                'question': 'En la siguiente tabla se muestra la distribucion de las edades, en años, de un grupo de niños.  [\\newline \\begin{array}{c:c} \\text{Edad} & \\text{Frecuencia} \\newline \\hline 2 & 5 \\newline \\hdashline 3 & 6 \\newline \\hdashline 4 & 9 \\newline \\hdashline 5 & 3 \\newline \\hline \\end{array} \\newline] ¿Cual es la mediana de edad de este grupo de niños?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=13314',
                'answer': [
                    {
                        'label': '[4 años]',
                        'right': 1
                    },
                    {
                        'label': '[3,5 años]',
                        'right': 0
                    },
                    {
                        'label': '[7,5 años]',
                        'right': 0
                    },
                    {
                        'label': '[9 años]',
                        'right': 0
                    },

                ],
            },
            {
                'question': 'Al lanzar un dado cargado, numerado del [1] al [6], la probabilidad de que salga un numero par es el doble de la probabilidad de que salga un numero impar. Si se lanza este dado, ¿cual es la probabilidad de que salga un numero impar?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=14765',
                'answer': [
                    {
                        'label': '[\\frac{1}{3}]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{1}{9}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{2}{3}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{2}{9}]',
                        'right': 0
                    },

                ],
            },
            {
                'question': 'En un mazo de cartas de naipes ingles [52 cartas], [13] de ellas son de trebol. Si se extraen del mazo dos cartas al azar, una despues de la otra y sin reposicion, ¿cual es la probabilidad de que ambas sean de trebol?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=14941',
                'answer': [
                    {
                        'label': '[\\frac{13}{52}] *[\\frac{12}{51}]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{13}{52}] *[\\frac{12}{52}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{13}{52}]+[\\frac{12}{52}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{13}{52}] +[\\frac{12}{51}]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'A un grupo de personas se le consultó acerca de la cantidad de películas vistas el último mes. En la tabla adjunta se presenta la distribución de los resultados de dicha consulta.[\\newline \\begin{array}{c:c} \\text{Cantidad de películas vistas el último mes} & \\text{Frecuencia} \\newline \\hline 1 & h \\newline \\hdashline 2 & 200 \\newline \\hdashline 3 & t \\newline \\hdashline 4 & 50 \\newline \\hline \\end{array} \\newline]Si se agregan personas al grupo de tal manera que la frecuencia de todos los datos aumenta en un [20%], ¿cuál de las siguientes expresiones representa la cantidad total de personas que hay finalmente en el grupo?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/Kdr9QVeILdI?start=358',
                'answer': [
                    {
                        'label': '[300 + 1,2h + 1,2t]',
                        'right': 1
                    },
                    {
                        'label': '[1,2h + 1,2t]',
                        'right': 0
                    },
                    {
                        'label': '[300]',
                        'right': 0
                    },
                    {
                        'label': '[12]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'Los resultados de las dos primeras pruebas de matemática de Esteban son un 5,3 y un 5,9.[\\newline]¿Cuál de las siguientes notas es la mínima que debe obtener Esteban en la tercera prueba para que su promedio sea de al menos un 5,9 en las tres pruebas?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/Kdr9QVeILdI?start=570',
                'answer': [
                    {
                        'label': '[6,5]',
                        'right': 1
                    },
                    {
                        'label': '[6,2]',
                        'right': 0
                    },
                    {
                        'label': '[6,1]',
                        'right': 0
                    },
                    {
                        'label': '[5,9]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'Se consultó a un grupo de 50 personas acerca de su sabor favorito de cierto tipo de helado. En la tabla adjunta se registran los resultados obtenidos.[\\newline \\begin{array}{c:c} \\text{Sabor} & \\text{Frecuencia} \\newline \\hline Vainilla & 9 \\newline \\hdashline Chocolate & 15 \\newline \\hdashline Frutilla & 6 \\newline \\hdashline Manjar & 20 \\newline \\hline \\end{array} \\newline]Si se elige a una de estas personas al azar, ¿cuál es la probabilidad de que su sabor favorito sea de vainilla o de frutilla?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/4-FdwiMge7Y?start=226',
                'answer': [
                    {
                        'label': '[\\frac{3}{10}]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{9}{50} \\cdot \\frac{6}{50}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{1}{54}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{1}{15}]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'Una caja contiene seis tarjetas todas del mismo tipo y en cada una de ellas hay una palabra escrita. Las palabras escritas en cuatro de las tar jetas son: CLASE, SOL, TEMPRANO y LEON.[\\newline]Se sabe que al extraer al azar una tarjeta de la caja la probabilidad de que la palabra escrita en ella tenga menos de tres letras vocales es [\\frac{2}{3}].[\\newline]¿Cuáles de las siguientes palabras podrían estar escritas en las otras dos tarjetas?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/4-FdwiMge7Y?start=275',
                'answer': [
                    {
                        'label': 'CUADRILATERO y CANTO',
                        'right': 1
                    },
                    {
                        'label': 'VASO y RED',
                        'right': 0
                    },
                    {
                        'label': 'CINCO y SEIS',
                        'right': 0
                    },
                    {
                        'label': 'PARALELOGRAMO y GIGANTESCO',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'Si se lanzan tres monedas, ¿cuál es la probabilidad de obtener al menos un sello?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/4-FdwiMge7Y?start=355',
                'answer': [
                    {
                        'label': '[\\frac{7}{8}]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{1}{3}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{1}{8}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{1}{2}]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'Una caja M contiene solo 3 bolitas rojas y 2 verdes, todas del mismo tipo y una caja N contiene solo una bolita roja y 3 bolitas verdes, todas del mismo tipo.[\\newline]Un experimento aleatorio consiste en lanzar un dado común, si sale un número par se extrae una bolita desde la caja M, en caso contrario se extrae una bolita de la caja N.[\\newline]Si se realiza este experimento, ¿cuál es la probabilidad de extraer una bolita roja?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=2875',
                'answer': [
                    {
                        'label': '[\\frac{17}{40}]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{17}{20}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{1}{8}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{1}{4}]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'Considera las tiendas A , B y C dedicadas a la venta de relojes. Si un cliente compra un reloj en una de estas tres tiendas, la probabilidad de que compre en A es 0,2 ; en B es 0,3 y en C es 0,5. Se sabe que la probabilidad de que cualquier reloj que se venda en las tiendas A, B y C tenga fallas es 0,3; 0,5 y 0,6 , respectivamente.[\\newline]Si Teresa compra un reloj que no tiene fallas, ¿cuál es la probabilidad de que lo haya comprado en la tienda A?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=2931',
                'answer': [
                    {
                        'label': '[\\frac{0,2 \\cdot 0,7}{0,2 \\cdot 0,7 + 0,3 \\cdot 0,5 + 0,5 \\cdot 0,4}]',
                        'right': 1
                    },
                    {
                        'label': '[0,2 \\cdot 0,7]',
                        'right': 0
                    },
                    {
                        'label': '[0,2 \\cdot 0,3]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{0,2 \\cdot 0,3}{0,2 \\cdot 0,3 + 0,3 \\cdot 0,5 + 0,5 \\cdot 0,6}]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'Cada uno de los estudiantes de los terceros medios de un colegio lleva una botella individual para hidratarse, ya sea de agua o jugo.[\\newline]Al seleccionar un estudiante de tercero medio de este colegio al azar, se puede determinar la probabilidad de que sea una mujer que lleva agua, si se sabe que:[\\newline](1) el [60%] de los estudiantes son hombres y de estos [\\frac{5}{6}] llevan agua.[\\newline](2) los [\\frac{2}{3}] de las mujeres llevan jugo.',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=3221',
                'answer': [
                    {
                        'label': 'Ambas juntas, (1) y (2)',
                        'right': 1
                    },
                    {
                        'label': '(1) por sí sola',
                        'right': 0
                    },
                    {
                        'label': '(2) por sí sola',
                        'right': 0
                    },
                    {
                        'label': 'Se requiere información adicional',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'De un grupo de 100 personas, 40 de ellas son fumadores. Un [20%]  de los fumadores no presenta una enfermedad respiratoria. Al seleccionar una persona al azar del grupo total, la probabilidad de que presente una enfermedad respiratoria es 0,35.[\\newline]Al seleccionar una persona al azar del grupo total, ¿cuál es la probabilidad de que no fume dado que no tiene una enfermedad respiratoria?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=3006',
                'answer': [
                    {
                        'label': '[\\frac{57}{65}]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{45}{60}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{57}{60}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{45}{65}]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'De un grupo de 100 personas, 40 de ellas son fumadores. Un [20%]  de los fumadores no presenta una enfermedad respiratoria. Al seleccionar una persona al azar del grupo total, la probabilidad de que presente una enfermedad respiratoria es 0,35.[\\newline]Al seleccionar una persona al azar del grupo total, ¿cuál es la probabilidad de que no fume dado que no tiene una enfermedad respiratoria?',
                'subject': 'probabilidades',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=3006',
                'answer': [
                    {
                        'label': '[\\frac{57}{65}]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{45}{60}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{57}{60}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{45}{65}]',
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
                'question': 'Sean [A(1,1)], [B(5,3)] y [C] los vertices de un triangulo. Se pueden determinar las coordenadas del vertice [C] del triangulo si se sabe que:  [(1)] Angulo [BAC = 90°] [(2)] El triangulo es isosceles y el vertice [C] esta en el cuarto cuadrante.',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=12325',
                'answer': [
                    {
                        'label': '[Ambas juntas, (1) y (2)]',
                        'right': 1
                    },
                    {
                        'label': '[(2) por si sola]',
                        'right': 0
                    },
                    {
                        'label': '[(1) por si sola]',
                        'right': 0
                    },
                    {
                        'label': '[Se requier informacion adicional]',
                        'right': 0
                    },

                ],
            },
            {
                'question': 'Considere los vectores [\\overrightarrow{u}] = [(-2,5)], [\\overrightarrow{v}] = [(3, -2)] y [\\overrightarrow{c}] = [(-1,-4)]. ¿Cual es el vector [\\overrightarrow{u}] + 2[\\overrightarrow{v}] - [\\overrightarrow{c}]?',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=9560',
                'answer': [
                    {
                        'label': '[(5,5)]',
                        'right': 1
                    },
                    {
                        'label': '[(3,5)]',
                        'right': 0
                    },
                    {
                        'label': '[(4,9)]',
                        'right': 0
                    },
                    {
                        'label': '[(2,1)]',
                        'right': 0
                    },

                ],
            },
            {
                'question': 'Si el punto (a,b) es la imagen que se obtiene al trasladar el punto R segun el vector (m,n), ¿cuales son las coordenadas de R?',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/OxgnJ-IgxA0?start=9691',
                'answer': [
                    {
                        'label': '[(a - m, b - n)]',
                        'right': 1
                    },
                    {
                        'label': '[(am, bn)]',
                        'right': 0
                    },
                    {
                        'label': '[(m - a, n - b)]',
                        'right': 0
                    },
                    {
                        'label': '[(a + m, b + n)]',
                        'right': 0
                    },

                ],
            },
            {
                'question': 'Con un cordel de largo d se forma un cuadrado. ¿Cuanto mide el area del un cuadrado?',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/m4qRM2mtjHA?start=480',
                'answer': [
                    {
                        'label': '[\\frac{d^2}{16}]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{d^2}{2}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{d^2}{4}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{d^2}{8}]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'Dos figuras geométricas son homotéticas con razón de homotecia -3.[\\newline]Si la figura original tiene un área de [b cm^{2} ], ¿cuál es el área de la imagen homotética?',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=2263',
                'answer': [
                    {
                        'label': '[9b cm^{2}]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{b}{3} cm^{2}]',
                        'right': 0
                    },
                    {
                        'label': '[9b^{2} cm^{2}]',
                        'right': 0
                    },
                    {
                        'label': '[3b cm^{2}]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': '¿Para qué puntos (x, y) en el plano cartesiano se cumple [\\frac{3x + y}{3} = x + y]?',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=2348',
                'answer': [
                    {
                        'label': 'Para los puntos de la forma (x, 0)',
                        'right': 1
                    },
                    {
                        'label': 'Para los puntos de la forma (x, y)',
                        'right': 0
                    },
                    {
                        'label': 'Solo para el punto (0, 0)',
                        'right': 0
                    },
                    {
                        'label': 'Para ningún punto',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': '¿Cuántos vectores (a, b) con coordenadas enteras y magnitud [\\sqrt{5}] hay en el plano cartesiano?',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=2414',
                'answer': [
                    {
                        'label': '[8]',
                        'right': 1
                    },
                    {
                        'label': '[2]',
                        'right': 0
                    },
                    {
                        'label': '[4]',
                        'right': 0
                    },
                    {
                        'label': 'Infinitos',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'Al trasladar el punto (x, y) según el vector (p, q) , se obtiene un punto en el segundo cuadrante.[\\newline]¿Cuál de las siguientes relaciones es verdadera?',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=2382',
                'answer': [
                    {
                        'label': '[x < -p e y > -q]',
                        'right': 1
                    },
                    {
                        'label': '[x > -p e y < -q]',
                        'right': 0
                    },
                    {
                        'label': '[x < p e y > q]',
                        'right': 0
                    },
                    {
                        'label': '[x < -p e y < -q]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193
                'question': 'Se necesita determinar el perímetro del rectángulo ABCD, cuyo largo y ancho miden (4x  1) cm y (x  2) cm, respectivamente. Se sabe que ABCD es semejante a un rectángulo cuyo largo y ancho miden 10 cm y 8cm, respectivamente.[\\newline]Para determinar el perímetro del rectángulo ABCD se realiza el siguiente procedimiento, cometiéndose un error: [\\newline] Paso 1: como los rectángulos son semejantes se plantea la expresión: [\\frac{4x + 1}{8} = \\frac{x + 2}{10}\\newline] Paso 2: se resuelve la expresión anterior, obteniéndose [x = \\fraac{3}{16} \\newline]Paso 3: se reemplaza este valor de x en (4x  1) cm y (x  2) cm, obteniéndose que el largo y el ancho del rectángulo son [\\frac{7}{4}]cm y [\\frac{35}{16}]cm, respectivamente.[\\newline]Paso 4: se calcula el perímetro del rectángulo obteniéndose [\\frac{63}{8}]cm.[\\newline]¿En cuál de los pasos se cometió el error?',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=1758',
                'answer': [
                    {
                        'label': 'En el Paso 1',
                        'right': 1
                    },
                    {
                        'label': 'En el Paso 2',
                        'right': 0
                    },
                    {
                        'label': 'En el Paso 3',
                        'right': 0
                    },
                    {
                        'label': 'En el Paso 4',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M2 FORMA 193 
                'question': 'La razón de semejanza entre las figuras P y Q, en ese orden, es [\\frac{3}{5}], mientras que la razón de semejanza entre las figuras R y P , en ese orden, es [\\frac{7}{3} \\newline]¿Cuál es la razón de semejanza entre las figuras R y Q, en ese orden?',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/3-qEJz0wATs?start=1813',
                'answer': [
                    {
                        'label': '[\\frac{7}{5}]',
                        'right': 1
                    },
                    {
                        'label': '[\\frac{44}{15}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{35}{9}]',
                        'right': 0
                    },
                    {
                        'label': '[\\frac{26}{15}]',
                        'right': 0
                    },

                ],
            },
            {#PAES 2023 M1 FORMA 113
                'question': 'A un punto P del plano cartesiano se le aplica una reflexión respecto al origen de este obteniéndose el punto Q, luego el punto Q se traslada según el vector [\\overrightarrow{v} = (-2, 3)] obteniéndose el punto R.[\\newline] Si R tiene coordenadas [(5, 4)] , ¿cuáles son las coordenadas del punto P ? ',
                'subject': 'geometria',
                'link_resolution':'https://www.youtube.com/embed/GFcXxDORRvo?start=560',
                'answer': [
                    {
                        'label': '[(-7,-1)]',
                        'right': 1
                    },
                    {
                        'label': '[(3,7)]',
                        'right': 0
                    },
                    {
                        'label': '[(7,-1)]',
                        'right': 0
                    },
                    {
                        'label': '[(-3,-7)]',
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
            question_object = Question.objects.create(**question_data, essays=essay_object)
            for answer_data in answers:
                Answer.objects.create(**answer_data, questions=question_object)


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
