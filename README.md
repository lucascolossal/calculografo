```markdown
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
- Distância até o local ajusta o valor
- Urgência na entrega tem custo
- Trabalho chato também tem custo
- Nível de inserção no mercado local (0–10) calibra o valor-hora base
- Um teto de segurança evita que a combinação de fatores gere um número
  fora da realidade comercial e você perca o contrato

## Como usar

Execute no terminal com Python 3 e responda as perguntas.

```bash
python v1_terminal/calculografo.py
```

## Estrutura

```
calculografo/
├── v1_terminal/
│   └── calculografo.py   # V1 — motor de cálculo por terminal
├── proposta.py           # V1.5 — classe Proposta
├── motor.py              # V1.5 — classe Motor
└── main.py               # V1.5 — entrada e orquestração
```

## Roadmap

- V1 — motor de cálculo por terminal *(v1_terminal/)*
- V1.5 — refatoração para arquitetura orientada a objetos *(atual)*
- V2 — [Calculógrafo API](https://github.com/lucascolossal/calculografo-api) — REST com histórico de propostas
- V3 — precificação por pacotes fixos
- V4 — dados de mercado por localidade

## Autor

Lucas Colossal
Técnico em informática desde 2013. Fotógrafo freelancer desde 2019.
Estudante de ADS em transição de carreira para TI.
Este projeto é parte desse processo.
```
