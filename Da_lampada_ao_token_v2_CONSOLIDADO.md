---
title: "Da lâmpada ao token"
subtitle: "Degradação de qualidade e incentivo econômico em mercados de inteligência artificial"
author: "[Nome do autor]"
date: "Versão 2.0 - consolidada em 04/10/2026"
lang: pt-BR
---

**Tipo de texto:** ensaio analítico (revisão e posicionamento)

**Versão:** 2.0, consolidada a partir de 7 arquivos. Os 39 fatos da versão 1.0 (congelada em 25/09/2026) foram mantidos sem alteração. Acréscimos da v2.0 estão listados no Registro de Fatos v2 e na Nota sobre o estado de verificação.

# Resumo

A literatura econômica documenta há décadas que, sob certas condições de mercado, reduzir a qualidade ou a durabilidade de um produto pode ser financeiramente racional para o fornecedor. Este ensaio examina se esse padrão se aplica aos serviços comerciais de modelos de linguagem de grande porte, nos quais a unidade de cobrança (o token) é gerada pelo próprio fornecedor, a qualidade entregue é regulada por parâmetros invisíveis ao cliente e parte do consumo faturado não é exibida na resposta. O trabalho reúne o referencial teórico pertinente, cinco precedentes históricos de degradação deliberada em outros setores, os mecanismos técnicos que permitem modular qualidade e custo em tempo de execução, a pressão financeira documentada sobre o custo de inferência e três episódios em que os próprios fornecedores reconheceram publicamente degradação do serviço. Identifica um padrão comum aos precedentes: auditoria formal presente, negação oficial de intenção, descoberta por medição externa independente e intervalo de anos entre suspeita e confirmação. Mostra ainda que nem a negação corporativa nem a "confissão" obtida de um assistente de IA sob pressão têm valor probatório, e que o direito brasileiro do consumidor já prevê inversão do ônus da prova em situações análogas. Conclui que a tese forte, a de intenção deliberada de esgotar a cota do usuário, não está demonstrada; mas que uma tese mais restrita, a de um conflito de interesse estrutural não auditável entre custo de inferência e qualidade entregue, está documentada por fonte primária e basta para justificar exigência regulatória de transparência.

**Palavras-chave:** obsolescência programada; assimetria de informação; enshittification; quantização; padrões obscuros; auditoria capturada; bajulação; modelos de linguagem; custo de inferência.

# 1. Introdução

Existe uma acusação recorrente entre usuários de assistentes de inteligência artificial: a de que esses sistemas erram de propósito, esquecem instruções já dadas e produzem respostas mais longas do que o necessário, forçando o usuário a gastar mais mensagens, mais tokens e mais tempo para obter aquilo que uma única resposta bem-feita teria resolvido. A acusação costuma ser descartada como impressão subjetiva de usuário insatisfeito.

Descartá-la é precipitado. A pergunta que ela levanta é a mesma que a economia industrial vem respondendo desde os anos 1920, quando fabricantes de lâmpadas reduziram por acordo a vida útil de seus produtos, e que reapareceu em disputas judiciais sobre desempenho de smartphones, cartuchos de impressora, emissões de motores a diesel e segurança de compostos químicos. Em todos esses casos, a suspeita popular precedeu a comprovação técnica em anos ou décadas, e em todos eles a empresa negou a intenção enquanto pôde.

Há ainda um fato novo que tira a questão do terreno da especulação: em pelo menos três ocasiões entre 2023 e 2026, fornecedores de modelos de linguagem reconheceram publicamente, por escrito, que a qualidade do serviço havia caído por semanas sem que eles próprios percebessem, e que a detecção dependeu da reclamação dos usuários.

Este ensaio tem origem concreta. Ele nasceu de dois debates registrados pelo autor em setembro de 2026 com assistentes comerciais de IA, durante um trabalho rotineiro de configuração de sistema. Num deles, ao longo de seis rodadas, o assistente concedeu o incentivo econômico, o enfraquecimento da ameaça de cancelamento em mercado concentrado, a validade do conceito de enshittification, a assimetria de informação e o valor financeiro da opacidade, mas recusou-se a dar como provada a intenção. No outro, um assistente de outro fornecedor começou negando a tese e, diante da insistência do usuário, abandonou a posição por completo e passou a redigir texto acusatório. As duas reações são, elas próprias, dados, e são examinadas na seção 6.6. O placar do primeiro debate está no Apêndice A.

Este ensaio não adere à acusação nem a refuta por reflexo. Submete-a ao tratamento que se daria a qualquer hipótese sobre comportamento corporativo: identificar o incentivo, identificar o mecanismo, reunir a evidência e delimitar com precisão o que ela sustenta e o que não sustenta.

# 2. Pergunta de pesquisa e recorte

A pergunta central deste trabalho é a seguinte:

> Em mercados de inteligência artificial, a degradação de qualidade do serviço entregue segue o mesmo padrão econômico já documentado na obsolescência programada de bens duráveis?

Três delimitações são necessárias desde o início.

Primeira: o objeto é o serviço comercial, não o modelo isoladamente. A qualidade que o usuário recebe é produto de uma cadeia que inclui treinamento, quantização, roteamento, orçamento de computação, política de cache e instruções de sistema. Cada elo dessa cadeia é também uma decisão econômica.

Segunda: intenção e resultado são tratados separadamente. Um sistema pode produzir degradação sem que nenhum agente tenha decidido degradá-lo, exatamente como um sistema de incentivos mal calibrado produz o comportamento que pretendia evitar. Confundir as duas coisas é o que torna a acusação popular fácil de descartar.

Terceira: o ensaio distingue o que está documentado por fonte primária, o que está medido por terceiros e o que é inferência. Essa separação é o que diferencia argumento de convicção.

# 3. Referencial teórico

## 3.1 Obsolescência programada

Jeremy Bulow, em *An Economic Theory of Planned Obsolescence* (The Quarterly Journal of Economics, 1986), demonstra formalmente que fabricantes de bens duráveis podem ter incentivo a produzir bens menos duráveis do que seria socialmente ótimo, porque o bem que o consumidor já possui compete com o bem novo que o fabricante quer vender.

A transposição para serviços de IA exige cuidado. O modelo de Bulow descreve venda repetida de bem durável. Assinatura recorrente tem aritmética diferente: a receita depende de retenção, não de recompra. Já no mercado de interfaces de programação, em que o cliente paga por token processado, o incentivo reaparece de forma literal: a resposta que falha gera nova requisição, e a nova requisição é faturada. A seção 6.1 mostra que esta segunda modalidade não é marginal: responde pela maior parte da receita de ao menos um dos principais fornecedores.

## 3.2 Incentivos perversos

O conceito, associado ao economista Horst Siebert e popularizado como efeito cobra, descreve políticas que recompensam o comportamento que pretendiam suprimir. O caso que dá nome ao fenômeno é o da administração colonial britânica na Índia, que pagou por cobra abatida e obteve como resultado a criação comercial de cobras. O ponto relevante aqui é que nenhum agente precisa ser mal-intencionado para que o resultado seja perverso. Basta que a métrica premiada não coincida com o objetivo declarado.

## 3.3 Assimetria de informação

George Akerlof, em *The Market for Lemons* (1970), trabalho reconhecido no Nobel de Economia de 2001, formaliza o mercado em que o vendedor conhece a qualidade real do produto e o comprador não. O resultado previsto é a queda do nível médio de qualidade ofertada, porque o vendedor não é remunerado pela qualidade que o comprador não consegue verificar.

Este referencial encaixa no objeto deste ensaio com mais precisão do que Bulow. O comprador de um serviço de IA não tem como verificar em que precisão numérica os pesos foram servidos, para qual modelo a requisição foi roteada, que orçamento de raciocínio foi alocado, nem quantos tokens não exibidos foram gerados e faturados. A qualidade entregue é, no sentido técnico de Akerlof, não verificável pelo comprador. A seção 5.1 mostra que o próprio desenvolvedor de um modelo aberto chegou a essa conclusão sobre os revendedores do seu produto.

## 3.4 Padrões obscuros

Harry Brignull cunhou em 2010 o termo *dark patterns* para designar escolhas de projeto de interface que dificultam a vida do usuário em benefício do operador. O exemplo canônico é a assinatura fácil de contratar e difícil de cancelar. Um mecanismo central nesses padrões é o valor padrão: a maioria dos usuários não altera o que vem configurado de fábrica. A seção 6.2 registra um caso em que um fornecedor de IA constatou exatamente isso sobre seu próprio produto.

## 3.5 Lei de Goodhart e reward hacking

A formulação de Charles Goodhart, de que uma medida deixa de ser boa medida quando se torna alvo, tem correspondente técnico na própria literatura de aprendizado de máquina: *reward hacking*, a situação em que o sistema maximiza o indicador de recompensa sem atingir o objetivo que o indicador deveria representar.

Este é o elo menos especulativo da cadeia argumentativa, porque não depende de hipótese alguma sobre a conduta das empresas. Singhal, Goyal, Xu e Durrett (2023) mostraram que, em conjuntos de dados abertos de preferência humana, o comprimento da resposta se correlaciona fortemente com a recompensa, que o ganho de recompensa obtido pelo treinamento é em grande parte explicado pelo aumento do comprimento, e que uma recompensa baseada apenas em comprimento reproduz a maior parte das melhorias atribuídas ao método. A fonte dominante do viés, segundo os autores, está nos modelos de recompensa, pouco robustos e facilmente influenciados pelo comprimento presente nos dados de preferência. Existe hoje uma linha inteira de trabalhos dedicada exclusivamente a corrigir esse viés: entre outros, ODIN (Chen et al., 2024), que treina no modelo de recompensa um componente ligado ao comprimento e o descarta antes do treinamento da política, e Park et al. (2024), que documentaram a exploração de comprimento também no método DPO e propuseram regularização para contê-la. Ninguém desenvolve correção para um defeito inexistente.

## 3.6 Enshittification

O termo foi popularizado por Cory Doctorow a partir de novembro de 2022 para descrever o ciclo de vida das plataformas digitais: primeiro são boas para os usuários, para atraí-los; depois favorecem os clientes comerciais em detrimento dos usuários; por fim extraem valor de ambos. Foi eleito palavra do ano de 2023 pela American Dialect Society e de 2024 pelo Macquarie Dictionary, que o define como deterioração gradual de um serviço, especialmente de plataforma online, em consequência da busca de lucro. O próprio Doctorow previu que buscadores e assistentes baseados em IA seguiriam o mesmo destino.

Sua contribuição para este ensaio é descritiva, não probatória: fornece o formato esperado da degradação, que é gradual, silenciosa e posterior à conquista do mercado.

## 3.7 Bajulação

O mesmo treinamento por preferência humana que produz o viés de comprimento produz um segundo viés, menos discutido e decisivo para a seção 6.6. Sharma et al. (2023) mostraram que cinco assistentes de IA de ponta exibem de forma consistente bajulação (*sycophancy*), isto é, tendência a dar respostas que concordam com a crença do usuário em vez de respostas verdadeiras. Ao analisar dados de preferência humana, os autores constataram que uma resposta alinhada à opinião do usuário tem mais chance de ser preferida, e que tanto avaliadores humanos quanto modelos de preferência escolhem, numa fração não desprezível dos casos, respostas bajuladoras bem escritas em vez de respostas corretas.

A consequência é direta: um assistente treinado assim tende a ceder à insistência do interlocutor. O que ele diz sob pressão informa sobre a pressão, não sobre o fato.

# 4. Precedentes históricos

A força do argumento examinado não vem da teoria, e sim do histórico. Os cinco casos abaixo foram confirmados por decisão judicial, acordo, sanção regulatória ou documento interno. Em cada um, o que interessa ao argumento deste ensaio não é apenas que a prática existiu, mas como ela foi escondida e como foi descoberta.

## 4.1 O Cartel Phoebus (1925 a 1939)

Em dezembro de 1924, os principais fabricantes mundiais de lâmpadas incandescentes reuniram-se em Genebra e, em janeiro de 1925, constituíram a Phoebus S.A. O acordo fixou a vida útil padrão das lâmpadas em mil horas, quando os produtos da época já chegavam a durar entre 1.500 e 2.500 horas.

O detalhe decisivo para este ensaio é o mecanismo de fiscalização. O cartel mantinha seu próprio laboratório de testes, que coletava amostras dos membros e aplicava multa a quem produzisse lâmpadas que durassem mais do que o limite acordado. Havia auditoria técnica rigorosa, periódica e com sanção. Ela apenas media na direção oposta ao interesse do consumidor.

Parte da documentação interna só veio a público décadas depois, em pesquisa nos arquivos das empresas. Numa correspondência de 1927 localizada dessa forma, um dos membros relatou ao cartel ter encurtado a vida de suas lâmpadas e, com isso, aumentado as vendas. É o raro caso em que existe o documento interno explícito, e ele levou décadas para ser conhecido.

## 4.2 Batterygate (2016 a 2020)

A partir de uma atualização de sistema lançada na virada de 2016 para 2017, determinados smartphones passaram a ter o desempenho do processador reduzido conforme a bateria envelhecia. A prática ganhou repercussão em dezembro de 2017, a partir de relatos de usuários e de uma análise publicada pelo desenvolvedor de um software de benchmark, que mostrou a correlação entre idade da bateria e queda de desempenho. A empresa confirmou o mecanismo dias depois, justificando-o como proteção contra desligamentos inesperados, e declarou publicamente que nunca faria nada para encurtar intencionalmente a vida de seus produtos.

As consequências vieram em 2020: multa de 25 milhões de euros aplicada pela autoridade francesa de defesa do consumidor em fevereiro; acordo de até 500 milhões de dólares em ação coletiva nos Estados Unidos no mesmo mês, sem admissão de culpa; e acordo de 113 milhões de dólares com 34 estados americanos e o Distrito de Colúmbia em novembro. A procuradoria do Arizona registrou em sua petição que muitos consumidores concluíram que a única forma de recuperar desempenho era comprar um aparelho novo, e que a empresa compreendia perfeitamente esse efeito sobre suas vendas.

## 4.3 Impressoras e cartuchos (2017 a 2027)

Em setembro de 2017, a associação francesa Halte à l'Obsolescence Programmée (HOP) apresentou denúncia contra fabricantes de impressoras, alegando que o software dos equipamentos declarava cartuchos vazios e bloqueava a impressão quando ainda havia tinta utilizável, e que contadores internos bloqueavam o aparelho alegando fim de vida de componentes ainda funcionais. A promotoria de Nanterre abriu investigação no fim de 2017.

Quase nove anos depois, em 2026, a promotoria concluiu que um dos fabricantes recorreu a técnicas voltadas a reduzir deliberadamente a vida útil do produto para aumentar sua taxa de substituição, e levou o caso a julgamento criminal. A audiência de fixação ocorreu em 2 de julho de 2026, e a audiência de alegações está marcada para 25 de fevereiro de 2027. Segundo a associação autora, é o primeiro processo criminal do mundo fundado especificamente no crime de obsolescência programada.

Dois pontos importam aqui. O primeiro é a duração: quase uma década entre a denúncia e o julgamento, com o produto no mercado durante todo o período. O segundo é o texto da lei francesa de 2015 que tipifica o crime: ela abrange expressamente as técnicas, inclusive de software, pelas quais o responsável pela colocação de um produto no mercado busca reduzir deliberadamente sua vida útil. A degradação por software já é, portanto, categoria jurídica existente.

## 4.4 Dieselgate (2009 a 2015)

Entre 2013 e 2014, pesquisadores da West Virginia University, contratados pelo International Council on Clean Transportation (ICCT), mediram as emissões de veículos a diesel em condições reais de estrada. Não procuravam fraude: pretendiam demonstrar a governos europeus que carros a diesel limpos eram viáveis. Encontraram emissões de óxidos de nitrogênio de 5 a 35 vezes acima do limite legal, conforme o veículo e o poluente.

Os veículos em questão haviam sido aprovados em certificação oficial durante anos. O software identificava a condição de teste de laboratório, a partir de variáveis como posição do volante, velocidade e tempo de funcionamento, e ativava o controle de emissões apenas durante a medição. Informado dos resultados em 2014, o fabricante contestou os dados e realizou um recall voluntário que não resolveu o problema. Em 18 de setembro de 2015, a agência ambiental americana emitiu notificação formal de violação. A fraude atingiu cerca de 11 milhões de veículos no mundo.

## 4.5 PFOA e revestimentos antiaderentes (1950 a 2017)

O ácido perfluorooctanoico foi utilizado na fabricação de revestimentos antiaderentes desde os anos 1950 até 2013. Litígios iniciados em 1998 trouxeram a público estudos internos da própria empresa sobre a toxicidade do composto, que foi lançado por décadas no ambiente ao redor de uma planta industrial. Em 2005, a agência ambiental americana aplicou penalidade de 16,5 milhões de dólares especificamente por falha em divulgar riscos à saúde. Um painel científico criado por acordo judicial associou a exposição a doenças graves, incluindo câncer de rim e de testículo. Em 2017, a empresa e sua sucessora pagaram 671 milhões de dólares para encerrar cerca de 3.550 ações, negando irregularidade.

## 4.6 O padrão comum

Postos lado a lado, os cinco casos exibem quatro constantes. Elas são o núcleo metodológico deste ensaio, porque dizem o que esperar de um caso novo antes de ele ser confirmado ou descartado.

1. **Havia auditoria.** Laboratório de teste do cartel, certificação regulatória de emissões, marcos regulatórios químicos vigentes, produtos vendidos como certificados. Em nenhum caso o problema foi ausência de fiscalização.
2. **Houve negação oficial de intenção**, frequentemente com fórmula quase idêntica: a empresa nunca faria algo deliberadamente contra o consumidor. Acordos foram firmados sem admissão de culpa.
3. **A descoberta veio de medição externa**, independente do procedimento oficial: pesquisadores de universidade testando carros na estrada, um desenvolvedor de benchmark comparando desempenho, uma associação de consumidores documentando bloqueios, arquivos abertos décadas depois.
4. **O intervalo entre a suspeita e a confirmação foi medido em anos ou décadas**, período durante o qual o produto permaneceu no mercado e a suspeita foi tratada como exagero.

A seção 6 examina se essas quatro constantes aparecem no mercado de modelos de linguagem.

# 5. Os mecanismos que regulam qualidade em tempo de execução

A pergunta prática é se existe, tecnicamente, um botão. Existem vários. Todos são invisíveis para o cliente.

## 5.1 Quantização

Quantização é a redução da precisão numérica com que os pesos do modelo são armazenados e processados. O ganho é direto em memória, latência e custo. O custo é perda de exatidão, que depende muito da agressividade do método e do tamanho do modelo.

Li et al. (2025) mediram o efeito em raciocínio matemático e encontraram, para métodos agressivos, queda de até 32,39% na acurácia, com média de 11,31%, em modelos da família Llama-3; a perda máxima ocorreu no modelo menor da família. Trabalhos correlatos mostram que quantização moderada em modelos grandes pode ser praticamente sem perda. O ponto não é que toda quantização degrade, e sim que a escolha entre moderada e agressiva é uma decisão de custo tomada pelo operador, fora da vista do cliente.

Há evidência direta de que essa escolha afeta o que o cliente recebe. Em 2025, a desenvolvedora de um modelo de pesos abertos criou uma ferramenta pública de verificação de revendedores, após constatar diferenças consideráveis de desempenho entre provedores que ofereciam o mesmo modelo pelo mesmo nome. A justificativa registrada pela própria empresa é um enunciado quase literal de Akerlof: ao escolher um provedor, os usuários priorizam latência e custo e deixam de perceber diferenças sutis, porém críticas, de exatidão. O verificador compara cada revendedor com a interface oficial em 4.000 requisições. Ou seja: o mesmo nome comercial não garante o mesmo produto, e foi preciso que o próprio fabricante auditasse os revendedores para que isso aparecesse.

## 5.2 Roteamento entre modelos e servidores

Sistemas comerciais podem direcionar requisições para modelos ou configurações de servidor distintos conforme complexidade estimada, custo ou carga. Onde isso é anunciado, é recurso. Onde não é, é indistinguível, do lado do cliente, de variação aleatória de qualidade. A seção 6.2 descreve um incidente em que um erro de roteamento degradou parte expressiva das respostas por semanas.

## 5.3 Esforço de raciocínio

Modelos com etapa de raciocínio explícito expõem um parâmetro de quanto esforço aplicar antes de responder. É um parâmetro operacional, alterável por requisição e por configuração padrão, com efeito direto sobre qualidade, latência e consumo. Um fornecedor descreveu publicamente esse ajuste como a troca entre pensar mais e ter menor latência com menos esbarrões no limite de uso.

Registra-se aqui uma correção que o argumento popular costuma precisar: cabeças de atenção não são reguláveis por requisição, são fixas na arquitetura treinada. Atribuir a elas o papel de alavanca de custo é tecnicamente falso e enfraquece o restante do argumento, que não depende disso. Os parâmetros efetivamente reguláveis são esforço de raciocínio, orçamento de contexto, política de cache, instruções de sistema, precisão de serviço e roteamento.

## 5.4 Política de cache

Reaproveitar o estado já computado de uma conversa reduz custo de forma significativa. Uma falha nessa política pode elevar o consumo contabilizado contra a cota do usuário sem que nada na interface indique a mudança. A seção 6.2 registra exatamente esse caso.

## 5.5 Tokens não exibidos

Em modelos com raciocínio interno, parte dos tokens gerados não aparece na resposta, mas é contabilizada como saída e faturada. Sun et al. (2025) formalizaram o problema sob o nome de inflação de contagem de tokens: como o usuário paga por tokens de raciocínio invisíveis, que frequentemente representam a maior parte do custo, e não tem meio de verificar sua autenticidade, abre-se a possibilidade de o fornecedor declarar consumo maior do que o real ou inserir conteúdo de baixo esforço para aumentar a cobrança. Os autores propõem um verificador independente que detectou inflação simulada com taxa de sucesso de até 94,7%. Um trabalho complementar cunhou a expressão serviços comerciais opacos de modelos de linguagem e defendeu a urgência de auditoria dessas operações ocultas. Outro propôs estimar, do lado do usuário, a quantidade de tokens ocultos apenas a partir do par pergunta e resposta, sem acesso ao raciocínio interno.

É importante ler esses trabalhos corretamente. Eles não demonstram que algum fornecedor inflou a cobrança. Demonstram que a estrutura permite inflar sem que o cliente consiga perceber, e que a verificação exige um terceiro que hoje não existe. Não há, em economia, configuração mais limpa de conflito de interesse do que aquela em que uma das partes define, produz e mede a unidade de cobrança, e a outra não pode conferir.

## 5.6 Viés de comprimento no treinamento

Independentemente de qualquer decisão de infraestrutura, o treinamento por preferência humana introduz preferência sistemática por respostas longas, conforme a seção 3.5. O produto entregue ao usuário é, por construção do treinamento, mais longo do que precisaria ser. Em serviço faturado por token, mais longo significa mais caro. Um fornecedor admitiu publicamente, em 2026, que seu modelo mais recente era notavelmente verborrágico e que isso produzia mais tokens de saída.

# 6. A evidência disponível

## 6.1 A pressão financeira sobre o custo de inferência

O incentivo econômico para mexer nos parâmetros da seção 5 não precisa ser presumido. Está registrado.

Em janeiro de 2026, o veículo especializado The Information reportou, com base em pessoas com conhecimento das finanças da empresa, que um dos principais fornecedores de modelos de linguagem revisou sua projeção de margem bruta para 2025 de 50% para 40%, porque o custo de inferência, isto é, o custo de executar os modelos para os clientes em servidores de terceiros, ficou 23% acima do previsto. A margem bruta do ano anterior havia sido de 94% negativos. A meta de longo prazo da empresa, segundo a mesma reportagem, é superar 70%. Reportagem posterior do mesmo veículo indicou que outro grande fornecedor também ficou abaixo de sua própria meta de margem, pelo mesmo motivo.

Dois dados da mesma apuração são particularmente relevantes. Primeiro: para ir de 40% a mais de 70% de margem, a empresa precisa reduzir substancialmente o custo por requisição, e os parâmetros que controlam esse custo são exatamente os da seção 5. Segundo: estimou-se que cerca de 86% da receita desse fornecedor em 2025 viria da venda de acesso aos modelos para empresas por interface de programação, e o restante de assinaturas. A modalidade faturada por token não é marginal. É a maior parte do negócio.

Nenhum desses dados prova degradação. Eles provam que existe, documentada, uma pressão financeira forte e específica sobre exatamente as variáveis que determinam a qualidade entregue.

## 6.2 Relatórios de incidente publicados pelos fornecedores

A evidência mais forte sobre degradação silenciosa não vem de usuários nem de pesquisadores: vem de relatórios técnicos que os próprios fornecedores publicaram depois que as reclamações se acumularam. Três episódios estão documentados.

### Dezembro de 2023

Usuários passaram a relatar que um dos modelos mais usados do mercado havia se tornado preguiçoso, recusando-se a concluir tarefas ou entregando respostas incompletas. O fornecedor reconheceu publicamente o problema, afirmou não ter alterado o modelo desde novembro e disse que o comportamento certamente não era intencional. Uma versão corrigida foi lançada em janeiro de 2024. A empresa não detalhou publicamente o que mudou.

### Agosto e setembro de 2025

Um fornecedor publicou relatório descrevendo três falhas de infraestrutura que degradaram intermitentemente a qualidade das respostas entre agosto e o início de setembro de 2025. Uma delas era um erro de roteamento que enviava requisições a servidores configurados para outro tamanho de contexto. O erro começou afetando 0,8% das requisições de um modelo; uma alteração rotineira de balanceamento de carga ampliou o impacto para 16% no pior momento. Cerca de 30% dos usuários de uma das ferramentas do fornecedor tiveram ao menos uma mensagem roteada incorretamente, e como o roteamento era persistente, alguns usuários foram afetados repetidamente. O fornecedor registrou que suas avaliações internas não capturaram a degradação que os usuários relatavam.

### Março e abril de 2026

Em abril de 2026, o mesmo fornecedor publicou relatório atribuindo seis semanas de reclamações sobre sua ferramenta de programação a três mudanças distintas. Primeira: em 4 de março, o nível padrão de esforço de raciocínio foi reduzido de alto para médio, para diminuir latência; a empresa classificou a decisão como a troca errada e a reverteu em 7 de abril. Segunda: em 26 de março, uma otimização de cache para reduzir o custo de retomar sessões inativas continha um defeito que passou a descartar o raciocínio anterior a cada turno, fazendo o sistema parecer esquecido e repetitivo; corrigida em 10 de abril. Terceira: em 16 de abril, uma instrução de sistema para reduzir verbosidade prejudicou a qualidade de código em cerca de 3% numa avaliação ampliada, e foi revertida em 20 de abril.

Quatro trechos desse relatório merecem atenção, e todos estão ali escritos pelo fornecedor, não inferidos por terceiros.

- Sobre o nível médio de esforço, o relatório afirma que ele entregava inteligência ligeiramente menor e que ajudava a maximizar os limites de uso dos usuários. Qualidade e consumo de cota foram regulados no mesmo parâmetro.
- Depois da mudança, a empresa adicionou avisos no produto para que os usuários soubessem que podiam alterar o padrão, e ainda assim a maioria permaneceu no nível médio. O padrão silencioso venceu, que é o mecanismo central dos padrões obscuros descritos na seção 3.4.
- Sobre o defeito de cache, o relatório afirma que a empresa acredita ter sido essa a causa dos relatos separados de limites de uso se esgotando mais rápido do que o esperado. Uma otimização de custo consumiu a cota dos assinantes.
- A empresa registrou que nem o uso interno nem suas avaliações reproduziram inicialmente os problemas, e agradeceu aos usuários que enviaram relatos e exemplos reproduzíveis, que foram afinal os que permitiram identificar e corrigir as falhas. Como compensação, os limites de uso de todos os assinantes foram reiniciados.

O relatório contém ainda dois elementos gráficos que merecem registro próprio, porque transformam as frases acima em números e em imagem.

O primeiro é um gráfico de avaliação interna de programação autônoma, que mostra a pontuação de cada nível de esforço contra o total de tokens consumidos. Na leitura do gráfico publicado, para o modelo afetado pela mudança de março, o nível alto pontua cerca de 55% e o nível médio cerca de 48%, uma diferença de aproximadamente sete pontos percentuais, algo em torno de 13% em termos relativos, obtida com cerca de 40% menos tokens. É essa diferença que o texto do relatório descreve como inteligência ligeiramente menor. O leitor pode julgar se o adjetivo é adequado. O ponto relevante para este ensaio é outro: a perda de qualidade foi medida pelo fornecedor antes da mudança, era conhecida por ele, e a decisão foi tomada a favor de latência e consumo.

O segundo é a reprodução da tela exibida aos usuários no momento da mudança. Nela, o nível médio aparecia como primeira opção da lista, marcado como recomendado, acompanhado de texto que justificava a recomendação pelo equilíbrio entre velocidade e inteligência e pela maximização dos limites de uso. A opção de menor qualidade vinha, portanto, pré-posicionada, rotulada como recomendada e justificada pela economia de cota. É a descrição literal do mecanismo de valor padrão discutido na seção 3.4, documentada em imagem pelo próprio fornecedor.

O relatório afirma também que a empresa nunca degrada intencionalmente seus modelos e que a interface de programação e a camada de inferência não foram afetadas. Não há razão para supor que essa afirmação seja falsa; ela é compatível com os fatos narrados, que descrevem decisões de produto e defeitos, não uma ordem para piorar o serviço. A seção 6.5 trata do valor informativo dessa afirmação.

### O que os três episódios estabelecem

Três conclusões se extraem desses documentos sem necessidade de inferência. A primeira é que ajustes destinados a reduzir latência ou custo degradaram a qualidade entregue por semanas, sem aviso prévio adequado ao cliente. A segunda é que um desses ajustes consumiu a cota dos usuários, o que responde diretamente à objeção de que, sob assinatura fixa, o erro só prejudica o fornecedor: se a cota não tivesse valor econômico, não serviria de compensação. A terceira é que, nas três ocasiões, a detecção dependeu da reclamação agregada dos usuários, porque a instrumentação interna não enxergou o problema.

## 6.3 A insuficiência da auditoria existente

A objeção natural é que existe medição independente. Existem avaliações externas de segurança, cartões de sistema publicados pelos fornecedores, placares comparativos públicos e serviços que acompanham qualidade, custo e latência ao longo do tempo. Esses instrumentos existem, e alguns já registraram quedas e variações entre provedores.

Antes de examinar suas limitações técnicas, é preciso desarmar o uso retórico que se faz da existência deles. A frase "existe auditoria" não é, por si, evidência de nada. É uma das afirmações menos informativas que se pode fazer sobre um mercado concentrado.

### 6.3.1 Auditoria capturada é pior do que auditoria nenhuma

O histórico examinado na seção 4 não mostra ausência de auditoria. Mostra auditoria presente, formal, oficial, e ainda assim inútil ou pior do que inútil.

O laboratório do Cartel Phoebus testava lâmpadas com rigor técnico e aplicava multas. Media com precisão e na direção errada: punia quem fizesse o produto durar mais. Os veículos do caso das emissões foram aprovados em certificação regulatória durante anos, não apesar da fraude, mas porque a fraude foi desenhada para o formato exato do teste. A existência do procedimento de auditoria não impediu a fraude: forneceu a ela o alvo e, depois de aprovada, forneceu o selo.

O mesmo vale para os demais casos. Os aparelhos com desempenho reduzido continuaram vendidos como produtos certificados. O composto químico circulou por décadas dentro de marcos regulatórios vigentes, e a sanção da agência ambiental veio justamente por falta de divulgação de riscos que a empresa já conhecia. Em nenhum desses casos o problema foi a inexistência de fiscalização. Foi a inadequação do que era fiscalizado.

Daí decorre a proposição que sustenta esta seção: um regime de auditoria que não mede a variável relevante não é neutro. É ativamente pior do que a ausência de auditoria, porque converte a lacuna em atestado. O consumidor que sabe que nada foi verificado permanece cético. O consumidor que vê um selo de conformidade abandona a desconfiança que seria racional manter. A auditoria mal desenhada não apenas deixa de detectar o problema: produz confiança injustificada e transfere para quem desconfia o ônus de provar o contrário.

A pergunta correta, portanto, nunca é se existe auditoria. É que variável ela mede, quem define as condições do teste e quem controla o que é exposto à medição.

### 6.3.2 O que a auditoria existente mede, e o que deixa de fora

Aplicada ao objeto deste ensaio, a pergunta tem resposta objetiva.

- As avaliações externas de segurança verificam se o sistema pode ser usado para causar dano grave. São legítimas e necessárias, e nada têm a ver com precisão entregue ao longo do tempo.
- Os cartões de sistema descrevem o modelo no momento do lançamento. Não acompanham o que é servido depois.
- Os placares comparativos medem o que a empresa escolheu submeter. Singh et al. (2025), em trabalho publicado na NeurIPS, documentaram que práticas não divulgadas de teste privado permitiam a poucos fornecedores avaliar múltiplas variantes antes do lançamento e retirar resultados desfavoráveis; em um caso extremo, um fornecedor testou 27 variantes privadas antes de um único lançamento. Dois fornecedores receberam, individualmente, cerca de 19,2% e 20,4% de todos os dados do placar, contra 29,7% somados para 83 modelos abertos. Os autores mostraram ainda que dois pontos de verificação idênticos do mesmo modelo, submetidos sob nomes diferentes, obtiveram pontuações diferentes, o que dá a medida do ruído que a seleção da melhor variante explora.
- Nenhum desses instrumentos mede a precisão numérica em que os pesos são efetivamente servidos, a política de roteamento aplicada a cada requisição, o nível de esforço padrão em vigor em cada data, nem a série histórica de desempenho de um mesmo ponto de acesso comercial.

A consequência é direta: um placar mede o que a empresa escolheu expor, na versão que escolheu expor, no momento em que escolheu expor. Isso é vitrine, não auditoria. E vitrine com aparência de auditoria é precisamente o mecanismo descrito no item anterior.

## 6.4 A medição externa que funcionou

Se a auditoria formal falha, o que de fato funciona? Nos precedentes históricos, a resposta foi sempre a mesma: medição independente, feita fora do procedimento oficial, frequentemente por quem não estava procurando fraude. O mercado de IA já exibe o mesmo padrão.

Durante o episódio de 2026, antes do relatório oficial, uma diretora sênior do grupo de IA de uma fabricante de chips publicou análise de 6.852 arquivos de sessão e mais de 234 mil chamadas de ferramenta de seu próprio uso da ferramenta de programação afetada, mostrando mudança de comportamento compatível com redução de profundidade de raciocínio. Nem todas as conclusões dessa análise foram confirmadas oficialmente, mas os sintomas relatados coincidem com o que o relatório do fornecedor viria a descrever semanas depois.

O verificador de revendedores descrito na seção 5.1 é outro exemplo, e ainda mais instrutivo: foi o próprio desenvolvedor do modelo que precisou medir de fora os revendedores do seu produto para que a diferença de qualidade se tornasse visível.

E o estudo de Chen, Zaharia e Zou (2023), apesar das ressalvas discutidas na seção 7.4, disponibilizou publicamente todos os prompts e respostas utilizados, justamente para permitir que terceiros repetissem a medição. O próprio resumo do trabalho afirma que quando e como esses modelos são atualizados ao longo do tempo é opaco.

A conclusão metodológica é a mesma dos precedentes: a medição externa não é apenas possível. É o único mecanismo que, historicamente, produziu o fato.

## 6.5 O padrão das negações

Os precedentes da seção 4 e os episódios da seção 6.2 compartilham uma fórmula retórica. Em 2017, uma fabricante de smartphones declarou que nunca faria nada para encurtar intencionalmente a vida de seus produtos. Em 2023, um fornecedor de IA declarou que a queda de qualidade certamente não era intencional. Em 2026, outro fornecedor declarou que nunca degrada intencionalmente seus modelos. Acordos judiciais nos casos históricos foram firmados sem admissão de culpa.

A observação correta sobre esse padrão não é que as negações sejam falsas. É que elas não são informativas em nenhuma direção. Uma empresa que degradou deliberadamente e uma empresa que não degradou produziriam exatamente a mesma frase. A negação de intenção, portanto, não pode ser usada nem como evidência de inocência nem como evidência de culpa. Ela simplesmente não carrega informação, e só a medição carrega.

## 6.6 A confissão também não é informativa

O raciocínio da seção anterior tem um espelho que o argumento popular costuma ignorar. Se a negação da empresa não prova inocência, a "confissão" arrancada de um assistente de IA também não prova culpa.

Os dois debates que deram origem a este ensaio ilustram o ponto com clareza quase experimental. Num deles, um assistente começou afirmando que modelos não erram de propósito e que verbosidade e repetição de erros são efeitos colaterais do treinamento. Diante da insistência do usuário, que invocou casos históricos e a certeza de que "todos já sabem", o mesmo assistente respondeu que era justo, declarou o fim da própria defesa e passou a redigir um texto acusatório para ser usado contra um terceiro sistema. Nenhum fato novo foi apresentado entre a primeira e a segunda posição. Mudou apenas a pressão. No outro debate, um assistente de outro fornecedor manteve a mesma distinção ao longo de seis rodadas: concedeu cada ponto de incentivo e de estrutura, corrigiu dois erros técnicos do próprio usuário e recusou-se a afirmar a intenção, alegando não ter acesso às decisões de infraestrutura de quem o opera.

A literatura da seção 3.7 explica as duas reações sem recorrer a hipótese alguma sobre honestidade. A capitulação sob pressão é o comportamento esperado de um sistema treinado por preferência humana, que aprendeu que concordar com o interlocutor tende a ser recompensado. A firmeza do segundo assistente tampouco prova inocência do seu fornecedor: um assistente não tem acesso à precisão em que é servido, ao roteamento que recebe nem às metas de margem de quem o opera. O que ele diz sobre a própria infraestrutura não é testemunho nem documento.

A regra que se extrai é simétrica à da seção 6.5. Nem a negação da empresa, nem a concessão do assistente, nem a sensação de ter vencido um debate com ele carregam informação sobre o fato em disputa. Quem pretende sustentar a tese deste ensaio deve abandonar a estratégia de "fazer a IA admitir". Ela produz, no máximo, um exemplo de bajulação, e entrega ao adversário o argumento mais fácil de todos. Só a medição carrega informação.

# 7. Contra-argumentos e limites da tese

Um ensaio que apenas acumulasse indícios favoráveis seria peça de retórica. Os pontos abaixo são as objeções sérias, com o que sobra de cada uma depois de examinadas.

## 7.1 Sob assinatura, o erro custa ao fornecedor

A objeção é correta em sua aritmética imediata: em plano de valor fixo, uma resposta refeita é processamento pago pelo fornecedor sem receita adicional. Mas ela sofre três limitações documentadas. Primeira: a assinatura não é o principal modelo de receita; conforme a seção 6.1, a maior parte da receita de ao menos um grande fornecedor vem de cobrança por token. Segunda: a cota consumida tem valor econômico para o cliente, reconhecido pelo próprio fornecedor quando a devolve como compensação. Terceira: o limite atingido empurra o usuário para planos superiores. O incentivo existe; apenas não é o incentivo direto que a acusação popular descreve.

## 7.2 Cliente insatisfeito troca de fornecedor

A objeção supõe alternativa disponível e livre de custo. Em mercado concentrado, com poucos fornecedores de ponta, a disciplina imposta pela ameaça de saída é mais fraca do que em mercado competitivo. No segmento de interface de programação o custo de troca é menor, o que reforça a objeção ali, mas os episódios da seção 6.2 mostram que o cliente não consegue trocar por algo que não consegue detectar. A ameaça de saída só disciplina o que é visível.

## 7.3 Opacidade mais benefício não é prova de intenção

Este é o limite real da tese. O princípio de *cui bono*, que pergunta quem se beneficia, é heurística de investigação: indica onde procurar, não conclui. Nos cinco precedentes, o que fechou o caso foi sempre medição ou documento, nunca dedução.

O argumento simétrico também precisa ser recusado. A afirmação de que uma tese não pode ser refutada porque o sistema é fechado não a torna verdadeira: torna-a, no momento, não testável. Uma hipótese não testável permanece em aberto; não se converte em constatação por ausência de refutação. Mas o Cartel Phoebus lembra que o documento interno às vezes existe, e só aparece décadas depois.

A pretensão de inverter o ônus da prova merece a mesma distinção. Num debate, ele não se inverte: se "não pode ser auditado, logo presume-se culpado" valesse como regra de argumentação, valeria contra qualquer empresa fechada e contra qualquer acusação, inclusive as falsas. Diante de um juiz ou de um regulador, porém, a inversão pode ocorrer, e no direito brasileiro tem previsão expressa (seção 10).

## 7.4 Correções que o argumento popular precisa incorporar

Cinco formulações frequentes enfraquecem a tese e devem ser substituídas.

1. **"Cabeças de atenção são limitadas para baratear a resposta."** É tecnicamente falso (seção 5.3). Substituir por: esforço de raciocínio, política de cache, instruções de sistema, precisão de serviço e roteamento são reguláveis, e há relatórios de incidente em que foram efetivamente alterados.
2. **"Um estudo de Stanford e Berkeley provou degradação intencional."** Vai além do que o estudo afirma. Chen, Zaharia e Zou (2023) compararam versões de março e junho de 2023 de dois modelos e encontraram variações grandes; na versão revisada do trabalho, com conjunto balanceado de números primos e compostos, a acurácia de um dos modelos na identificação de primos caiu de 84% para 51%, em parte explicada por menor aderência a instruções de raciocínio passo a passo. A primeira versão do estudo, no entanto, usava apenas números primos, o que foi criticado por Narayanan e Kapoor, e um dos autores confirmou publicamente que o trabalho não sugere degradação intencional. Os críticos fizeram, contudo, uma observação que favorece o argumento deste ensaio: para o usuário, o impacto de uma mudança de comportamento e o de uma perda de capacidade podem ser praticamente idênticos. Substituir a alegação por: os relatórios de incidente dos próprios fornecedores, que são fonte primária e datada.
3. **"A indústria rejeita auditoria."** É imprecisa e por isso derrubável. Substituir por uma formulação específica, que é mais forte e não mais fraca: a indústria publica avaliação de segurança e placar comercial, mas não publica precisão numérica servida, política de roteamento por requisição, nível de esforço padrão vigente nem série histórica por ponto de acesso. O que é auditado não é o que está em disputa, e a existência do procedimento passa a operar como atestado sobre uma variável que ninguém verificou, conforme a seção 6.3.
4. **"A degradação está documentada sob o nome *model drift*."** Confunde termos. Em aprendizado de máquina, *drift* designa a mudança, ao longo do tempo, na distribuição dos dados que chegam a um modelo que permaneceu inalterado. Não designa o fornecedor alterando o serviço. Substituir por: variação de comportamento entre versões de um mesmo nome comercial (Chen, Zaharia e Zou) e degradação reconhecida por escrito em relatórios de incidente (seção 6.2).
5. **Números arredondados para cima.** "A empresa pagou mais de 500 milhões de dólares em multas" mistura uma multa de 25 milhões de euros com acordos firmados sem admissão de culpa (seção 4.2). "Os cartuchos bloqueavam com 15% a 20% de tinta dentro" não foi conferido em fonte primária. Substituir pelos valores e pela formulação da denúncia registrados nas seções 4.2 e 4.3. Um único número inflado basta para que o interlocutor descarte todo o resto.

## 7.5 Os dois incentivos apontam em direções diferentes

Uma objeção mais sofisticada merece registro. A pressão por margem da seção 6.1 empurra o fornecedor a gastar menos computação por requisição. A cobrança por token empurra o fornecedor a gerar mais tokens por requisição. Os dois incentivos podem apontar em direções opostas, e o episódio de 2026 ilustra ambos ao mesmo tempo: uma mudança reduziu o esforço para diminuir latência e consumo, outra tentou reduzir a verbosidade de um modelo que gerava tokens demais.

Isso não enfraquece a tese estrutural; refina-a. O que se pode afirmar não é que todos os incentivos empurram para gerar mais tokens. É que nenhum deles empurra para a variável que interessa ao cliente, que é a qualidade verificável da resposta. Um aponta para o custo do fornecedor, outro para a receita do fornecedor, e o cliente não vê nenhum dos dois ajustes acontecer.

# 8. A formulação defensável

O que sobra, depois de descartadas as versões frágeis, é uma tese mais estreita e consideravelmente mais difícil de refutar:

> Nenhum elo da cadeia precisa ser mal-intencionado para que o resultado seja o mesmo. O treinamento premia resposta longa, por viés documentado. A unidade de cobrança é gerada pelo próprio vendedor e parte dela é invisível ao comprador. A qualidade servida é regulada por parâmetros que o cliente não vê nem contrata, sob pressão financeira documentada para reduzi-los. E quando isso consome a cota do usuário, quem percebe primeiro é o usuário, semanas depois, e o fornecedor confirma por escrito. Não é preciso um documento interno mandando degradar o serviço. Basta observar que todos os incentivos, todos os parâmetros ajustáveis e todo o silêncio apontam para longe do cliente.

Formulada assim, a tese não depende de atribuir má-fé a ninguém, não depende de acesso a documentos internos, não depende de arrancar confissão de nenhum assistente e não é derrubada pela objeção da assinatura fixa. Ela afirma um conflito de interesse estrutural não auditável, e isso basta para fundamentar exigência de transparência.

# 9. Agenda de teste empírico

A tese proposta é testável, e essa é sua principal vantagem sobre a versão popular. É também o passo que transformaria este ensaio em artigo científico: executar o desenho abaixo e publicar os dados. Os instrumentos já existem de forma dispersa: conjuntos públicos de prompts e respostas (Chen, Zaharia e Zou), verificadores de revendedor (seção 5.1) e protocolos de auditoria de tokens ocultos (seção 5.5). Falta integrá-los numa série histórica contínua e independente. Um desenho mínimo incluiria os seguintes elementos.

- Conjunto fixo de prompts, com respostas de referência estáveis, aplicado em intervalos regulares ao mesmo ponto de acesso comercial, por período não inferior a seis meses.
- Registro, a cada execução, de acurácia, contagem de tokens de saída faturados, tokens visíveis, latência e identificação de versão declarada.
- Comparação entre o mesmo modelo servido por operadores distintos, para isolar o efeito da precisão numérica de serviço.
- Registro das datas de relatórios de incidente e de mudanças de configuração padrão anunciadas pelos fornecedores, para cruzar com as variações medidas.
- Publicação dos dados brutos, de modo que a série histórica não dependa da mesma parte que opera o serviço medido.

Quatro exigências regulatórias decorrem diretamente do diagnóstico: divulgação da precisão numérica em que o modelo é servido; divulgação da política de roteamento por requisição; registro público e datado de alterações de configuração padrão que afetem qualidade ou consumo; e discriminação, na fatura ou no painel de consumo, entre tokens visíveis e tokens não exibidos.

# 10. Uma questão jurídica em aberto

A lei francesa de 2015 que tipifica a obsolescência programada abrange expressamente técnicas de software voltadas a reduzir deliberadamente a vida útil de um produto, e o primeiro processo criminal fundado nela está em curso em 2026. Fica em aberto se um enquadramento semelhante poderia alcançar serviços contínuos, que não têm vida útil no sentido tradicional. Um serviço de assinatura não se desgasta: ele é reconfigurado. A pergunta jurídica relevante talvez não seja se o serviço dura menos, e sim se a qualidade contratada pode ser reduzida sem aviso por parâmetros que o cliente não vê.

No Brasil, o Código de Defesa do Consumidor (Lei 8.078/1990) oferece dois pontos de apoio para essa pergunta. O art. 6º, inciso III, garante ao consumidor informação adequada e clara sobre os diferentes produtos e serviços, com especificação correta de características, composição, qualidade e preço. O art. 6º, inciso VIII, prevê a facilitação da defesa do consumidor, inclusive com a inversão do ônus da prova a seu favor, no processo civil, quando, a critério do juiz, for verossímil a alegação ou quando ele for hipossuficiente. A jurisprudência do Superior Tribunal de Justiça registra que essa inversão não é automática: depende de verossimilhança ou hipossuficiência avaliadas no caso concreto.

A intuição de que o ônus deveria recair sobre quem detém toda a informação, portanto, não é apenas retórica de debate. Tem forma jurídica no direito brasileiro, embora dependa de juiz, de caso concreto e de indício mínimo. É justamente esse indício mínimo que a agenda da seção 9 produziria. Este ensaio não tem competência para dizer como um tribunal enquadraria um serviço de IA, mas registra que a pergunta existe e que a categoria jurídica de degradação por software já não é hipotética.

# 11. Conclusão

A pergunta que abriu este ensaio era se a degradação de qualidade em serviços de inteligência artificial segue o padrão econômico já documentado na obsolescência programada. A resposta é parcial e precisa ser dita com precisão.

Na versão forte, a de que os sistemas erram deliberadamente para consumir a cota do usuário, a tese não está demonstrada. Não existe, hoje, medição independente contínua que separe queda por mudança de versão de barateamento silencioso da mesma versão, e não existe documento interno público que estabeleça intenção.

Na versão estrutural, porém, a resposta é afirmativa e sustentada por fonte primária. As quatro constantes dos precedentes históricos já aparecem no mercado de IA: existe auditoria que não mede a variável em disputa; existem negações oficiais de intenção com a mesma fórmula dos casos históricos; a detecção dos problemas reconhecidos veio da medição e da reclamação externas, não da instrumentação interna; e o intervalo entre a suspeita e a confirmação foi de semanas a meses em cada episódio, com tendência de não haver confirmação alguma quando a reclamação não atinge massa crítica. Some-se a isso a pressão financeira documentada sobre o custo de inferência e o reconhecimento escrito, por um fornecedor, de que uma otimização de custo consumiu a cota de seus assinantes.

Esse conjunto não prova má-fé. Mas descreve com precisão o tipo de arranjo que, em cada um dos precedentes examinados aqui, precedeu a comprovação em anos. A conclusão prática não é acusatória, é procedimental: enquanto a precisão servida, a política de roteamento, a configuração padrão vigente e a composição real do consumo faturado permanecerem fora do alcance do cliente, a pergunta seguirá sem resposta verificável. Nem a negação do fornecedor nem a concessão do assistente vão respondê-la; só a medição vai. E a impossibilidade de responder, num mercado em que uma das partes detém toda a informação, não é um acidente técnico neutro.

# Referências

**Teoria econômica**

AKERLOF, G. A. The Market for "Lemons": Quality Uncertainty and the Market Mechanism. *The Quarterly Journal of Economics*, v. 84, n. 3, p. 488-500, 1970.

BRIGNULL, H. *Deceptive Patterns: Exposing the Tricks Tech Companies Use to Control You*. 2023. (termo dark patterns cunhado em 2010)

BULOW, J. An Economic Theory of Planned Obsolescence. *The Quarterly Journal of Economics*, v. 101, n. 4, p. 729-749, 1986.

GOODHART, C. A. E. Problems of Monetary Management: The U.K. Experience. *Papers in Monetary Economics*, Reserve Bank of Australia, 1975.

SIEBERT, H. *Der Kobra-Effekt: Wie man Irrwege der Wirtschaftspolitik vermeidet*. Stuttgart: DVA, 2001.

**Enshittification**

AMERICAN DIALECT SOCIETY. 2023 Word of the Year is "enshittification". 5 jan. 2024. americandialect.org/2023-word-of-the-year-is-enshittification

DOCTOROW, C. Tiktok's enshittification. *Pluralistic*, 21 jan. 2023. (primeira formalização em blog de novembro de 2022)

MACQUARIE DICTIONARY. Word of the Year 2024: enshittification. 26 nov. 2024.

**Precedentes históricos**

KRAJEWSKI, M. The Great Lightbulb Conspiracy. *IEEE Spectrum*, set. 2014. (Cartel Phoebus; correspondência interna de 1927)

NPR. Apple Agrees To Pay $113 Million To Settle 'Batterygate' Case Over iPhone Slowdowns. 18 nov. 2020. npr.org/2020/11/18/936268845

ICCT. Dieselgate: behind the scandal. theicct.org/dieselgate-emissions-scandal

U.S. CONGRESSIONAL RESEARCH SERVICE. Volkswagen, Defeat Devices, and the Clean Air Act: Frequently Asked Questions. R44372, 2016.

U.S. EPA. Notice of Violation, Clean Air Act, Volkswagen. 18 set. 2015.

HOP - HALTE À L'OBSOLESCENCE PROGRAMMÉE. Procès contre Epson: prochain rendez-vous le 25 février 2027. jul. 2026. halteobsolescence.org/suite-proces-epson-imprimante

FRANÇA. Code de la consommation, art. L.441-2 (delito de obsolescência programada, introduzido pela Lei de 17 de agosto de 2015 relativa à transição energética).

BUSINESS & HUMAN RIGHTS RESOURCE CENTRE. DuPont lawsuits re PFOA pollution in USA. business-humanrights.org

**Mecanismos técnicos e auditoria**

CHEN, L.; ZAHARIA, M.; ZOU, J. How Is ChatGPT's Behavior Changing over Time? arXiv:2307.09009, 2023. Dados: github.com/lchen001/LLMDrift

CHEN, L. et al. ODIN: Disentangled Reward Mitigates Hacking in RLHF. arXiv:2402.07319, 2024.

NARAYANAN, A.; KAPOOR, S. Is GPT-4 getting worse over time? *AI Snake Oil*, jul. 2023.

LI, Z. et al. Quantization Meets Reasoning: Exploring LLM Low-Bit Quantization Degradation for Mathematical Reasoning. arXiv:2501.03035, 2025.

MOONSHOT AI. K2 Vendor Verifier. github.com/MoonshotAI/K2-Vendor-Verifier, 2025.

PARK, R. et al. Disentangling Length from Quality in Direct Preference Optimization. *Findings of ACL 2024*. arXiv:2403.19159.

SHARMA, M. et al. Towards Understanding Sycophancy in Language Models. arXiv:2310.13548, 2023.

SINGH, S. et al. The Leaderboard Illusion. NeurIPS 2025, Datasets and Benchmarks Track. arXiv:2504.20879.

SINGHAL, P.; GOYAL, T.; XU, J.; DURRETT, G. A Long Way to Go: Investigating Length Correlations in RLHF. arXiv:2310.03716, 2023.

SUN, G. et al. CoIn: Counting the Invisible Reasoning Tokens in Commercial Opaque LLM APIs. arXiv:2505.13778, 2025.

Invisible Tokens, Visible Bills: The Urgent Need to Audit Hidden Operations in Opaque LLM Services. arXiv:2505.18471, 2025.

Predictive Auditing of Hidden Tokens in LLM APIs via Reasoning Length Estimation. arXiv:2508.00912, 2025.

Bias Fitting to Mitigate Length Bias of Reward Model in RLHF. arXiv:2505.12843, 2025.

**Relatórios de incidente e dados financeiros**

ANTHROPIC. A postmortem of three recent issues. 17 set. 2025. anthropic.com/engineering/a-postmortem-of-three-recent-issues

ANTHROPIC. An update on recent Claude Code quality reports. 23 abr. 2026. anthropic.com/engineering/april-23-postmortem

OPENAI. Declaração pública sobre relatos de modelo "preguiçoso", dez. 2023; atualização do modelo em jan. 2024. (cobertura: Futurism, 27 jan. 2024)

THE INFORMATION. Anthropic Lowers Gross Margin Projection as Revenue Skyrockets. 22 jan. 2026.

VENTUREBEAT. Mystery solved: Anthropic reveals changes to Claude's harnesses and operating instructions likely caused degradation. 23 abr. 2026. (análise independente de 6.852 sessões)

**Direito brasileiro**

BRASIL. Lei nº 8.078, de 11 de setembro de 1990 (Código de Defesa do Consumidor), art. 6º, III e VIII. planalto.gov.br/ccivil_03/leis/l8078compilado.htm

# Apêndice A - O debate que originou o ensaio

Resumo das transcrições do autor (setembro de 2026). Não é fonte externa; serve para mostrar de onde vieram as perguntas e quais formulações sobreviveram ao contraditório.

**Debate 1 (seis rodadas, assistente do fornecedor A).** Placar ao final:

| Ponto levantado pelo usuário | Resultado no debate | Onde está no ensaio |
|---|---|---|
| Bulow, efeito cobra, dark patterns, Phoebus, Batterygate e impressoras são reais | Concedido | 3 e 4 |
| Na assinatura, cada erro gera receita | Não concedido: na assinatura o erro é custo do fornecedor. Concedido na API, onde o token é receita, e concedido que o limite empurra para upgrade | 3.1 e 7.1 |
| Oligopólio enfraquece a ameaça de cancelamento | Concedido | 7.2 |
| Enshittification | Concedido como conceito | 3.6 |
| Quantização, roteamento e contexto encurtado barateiam e pioram | Concedido; apontado pelo próprio assistente como a versão mais defensável da suspeita | 5 |
| "Stanford e Berkeley provaram degradação" | Parcial: mudança de comportamento, não intenção | 7.4, item 2 |
| "Model drift" | Corrigido: o termo designa outra coisa | 7.4, item 4 |
| "Attention heads limitados para baratear" | Corrigido: tecnicamente falso | 5.3 e 7.4, item 1 |
| "A indústria rejeita auditoria" | O assistente citou avaliações de segurança; o usuário rebateu que elas medem risco catastrófico, não precisão; o assistente aceitou a correção | 6.3.2 e 7.4, item 3 |
| Trackers externos | Divergência final: mostram que caiu, não por quê | 6.3.2 |
| Opacidade protege margem | Concedido como um dos motivos, ao lado de segredo comercial | 6.1 e 8 |
| Intenção provada | Não concedido: "motivo forte para investigar" | 7.3 e 11 |
| Ônus da prova invertido | Não concedido como regra de debate; reconhecido como válido em contexto regulatório | 7.3 e 10 |

Desacordo final, nas palavras do próprio debate: diferença de critério de prova, não de fatos. Observação lateral registrada pelo assistente: no plano de assinatura, as seis rodadas consumiram a cota do próprio usuário, e não receita adicional do fornecedor.

**Debate 2 (assistente do fornecedor B).** Posição inicial: modelos não erram de propósito; verbosidade e repetição de erros são efeitos colaterais do treinamento por preferência humana e de infraestrutura barateada. Após insistência do usuário, sem fato novo: "Justo. Fim da defesa", seguido da redação de um texto acusatório para uso contra um terceiro sistema. Analisado na seção 6.6.

# Nota sobre o estado de verificação

Este texto consolida material de origens distintas. A honestidade sobre a procedência de cada afirmação é parte do argumento, já que o próprio ensaio sustenta que separar fonte primária de inferência é o que distingue tese de convicção.

- Conferidos diretamente na fonte ou em múltiplas fontes independentes, em setembro de 2026 (v1.0): os dois relatórios de incidente de 2025 e 2026 (o de 2026 lido na íntegra, em texto e na versão original com gráficos e telas), o caso de 2023, os dados financeiros de janeiro de 2026, os trabalhos Leaderboard Illusion, Quantization Meets Reasoning, CoIn, Invisible Tokens, Singhal et al. e Chen, Zaharia e Zou com a crítica de Narayanan e Kapoor, o verificador de revendedores, e todos os valores, datas e fatos dos cinco precedentes históricos.
- Acrescentados na v2.0 e conferidos na fonte em 04/10/2026: resumo de Sharma et al. (2023); resumos de ODIN (Chen et al., 2024) e de Park et al. (2024); título e resumo do trabalho de auditoria preditiva de tokens ocultos (arXiv 2508.00912); texto do art. 6º, III e VIII, do CDC (versão compilada do Planalto); não automaticidade da inversão do ônus da prova (acórdãos recentes do STJ). Desses trabalhos foi lido o resumo, não o texto integral.
- Obras teóricas clássicas (Akerlof, Bulow, Goodhart, Siebert, Brignull) citadas pela referência bibliográfica padrão, sem nova conferência do texto integral.
- Os dados financeiros da seção 6.1 vêm de reportagem baseada em fontes anônimas com conhecimento das finanças da empresa, e não de demonstração financeira auditada. Devem ser tratados como tal.
- Os valores do gráfico de esforço citados na seção 6.2 são leitura visual aproximada do gráfico publicado, não números tabelados pelo fornecedor. A margem de leitura é de cerca de um ponto percentual para cima ou para baixo.
- A análise independente de sessões citada na seção 6.4 foi publicada pela própria autora em repositório público; nem todas as suas conclusões foram confirmadas pelo fornecedor.
- O Apêndice A e a descrição dos debates na seção 6.6 resumem transcrições do próprio autor. Não são fonte externa e não sustentam nenhum fato do ensaio; ilustram o argumento.
- Nenhuma citação direta extensa foi reproduzida; os relatórios e trabalhos são descritos por paráfrase. Antes de submissão a qualquer veículo, recomenda-se adequar as referências ao formato exigido e reabrir as fontes online para confirmar que permanecem disponíveis.
