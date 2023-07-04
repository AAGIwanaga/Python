import re

texto1 = ''' João era um jovem de espírito livre e coração generoso. Desde cedo, ele demonstrou uma curiosidade insaciável pelo mundo ao seu redor. Seu sorriso cativante e sua disposição para ajudar os outros conquistavam a todos que cruzavam seu caminho.
Apesar das dificuldades que enfrentava em sua vida, João nunca perdeu a fé nem desistiu de seus sonhos. Ele acreditava firmemente que cada obstáculo era uma oportunidade de crescimento e aprendizado. Com determinação inabalável, ele se esforçava para superar as adversidades, sempre encontrando soluções criativas e positivas.
João tinha uma paixão especial pelas artes. Ele mergulhava de cabeça na pintura, na música e na escrita, buscando expressar suas emoções mais profundas por meio dessas formas de arte. Seus quadros vibrantes e suas melodias harmoniosas encantavam quem os contemplava, e suas palavras tocavam os corações daqueles que as liam.
Além de sua dedicação às artes, João também tinha uma preocupação sincera com o bem-estar dos outros. Ele se envolvia em projetos sociais, oferecendo seu tempo e habilidades para ajudar comunidades carentes. Sua empatia era inegável, e ele sempre encontrava uma maneira de tornar o mundo um lugar melhor para aqueles que mais precisavam.
Mesmo diante dos desafios da vida, João nunca deixou de ser uma fonte de inspiração para todos ao seu redor. Sua coragem e otimismo irradiavam esperança e motivavam aqueles que o conheciam. Ele entendia que a felicidade verdadeira estava nas pequenas coisas, nos momentos de conexão genuína e no amor compartilhado.
João, com seu espírito brilhante e gentileza inesgotável, deixou uma marca indelével no coração de todos que tiveram a sorte de cruzar seu caminho. Ele nos ensinou a valorizar cada instante da vida, a abraçar nossas paixões e a estender a mão para aqueles que precisam. Seu legado perdurará como um lembrete de que podemos fazer a diferença, mesmo que sejamos apenas uma pessoa.
E assim, João continua a viver em nossas memórias, como uma inspiração constante para buscarmos o melhor de nós mesmos e espalharmos bondade e amor ao mundo.'''

print(re.sub(r'joão', 'Carlinhos', texto1, flags = re.I)) # RE.SUB: FUNÇÃO DE SUBSTITUIÇÃO SENDO NECESSÁRIO ESPECIFICAR QUAL STRING SERÁ SUBSTITUÍDO POR OQ
print(re.match(r' João', texto1)) # re.match: É UM LOCALIZAR LIMITADO A VERIFICAR A PRIMEIRA PALAVRA DO TEXTO
print(re.split(r',', texto1))


''' PARA MAIS FUNÇÕES DA BIBLIOTECA RE SEGUE O LINK:
https://docs.python.org/3/library/re.html '''