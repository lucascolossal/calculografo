# Calculógrafo

Precificar trabalho fotográfico é, via de regra, um exercício de chute. 
O Calculógrafo existe para mudar isso.

Desenvolvido por um fotógrafo freelancer que cansou de cobrar no feeling,
o sistema traduz variáveis reais do trabalho — esforço, logística, urgência 
e mercado local — num cálculo replicável. Você responde as perguntas, 
ele faz a matemática.

## Como funciona

O sistema pergunta sobre a proposta e aplica modificadores em cascata 
sobre um valor-hora base:

- Horas de campo (captura) e horas de ateliê (edição) têm pesos diferentes
- Distância até o local ajusta o valor (P/M/G)
- Urgência na entrega tem custo
- Trabalho chato também tem custo
- Nível de inserção no mercado local (0-10) calibra o valor-hora base
- Um teto de segurança evita que a combinação de fatores gere um número 
  fora da realidade comercial e você perca o contrato

## Como usar

Execute no terminal com Python 3 e responda as perguntas.

```bash
python calculografo.py
```

## Roadmap

- V1 (atual): motor de cálculo por hora via terminal
- V2: bifurcação para precificação por pacotes fixos
- V3: validação rigorosa de entradas
- V4: separação de interface e motor lógico, GUI

## Autor

Lucas Colossal
Técnico em informática desde 2013. Fotógrafo freelancer desde 2019.
Estudante de ADS em transição de carreira para TI.
Este projeto é parte desse processo.
