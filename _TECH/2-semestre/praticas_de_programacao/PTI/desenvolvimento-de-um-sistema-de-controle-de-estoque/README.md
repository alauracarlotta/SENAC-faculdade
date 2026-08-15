# 📦 Sistema de Gerenciamento de Estoque (CLI)

> Projeto desenvolvido como atividade acadêmica (PTI) para a disciplina de Algoritmos e Programação de Computadores.

Este sistema em linha de comando (CLI) permite cadastrar, validar, visualizar e calcular o saldo de estoque de produtos comercializados, garantindo a integridade dos dados por meio de validações rigorosas com expressões regulares e tratamento de exceções.

---

## 🚀 Funcionalidades

- **Cadastrar Produto:**
  - Validação de código de barras (EAN-13): aceita até 13 dígitos numéricos, preenche automaticamente com zeros à direita e impede códigos duplicados.
  - Validação de Nome: exige ao menos 3 letras (suporta caracteres acentuados via Unicode).
  - Validação de Preço e Quantidade: impede a inserção de valores e quantidades negativas, formatando a saída para o padrão de moeda brasileira (R$ XX,XX).
- **Visualizar Estoque:**
  - Apresenta os produtos cadastrados em uma tabela estilizada no terminal (`fancy_grid`).
- **Calcular Total em Estoque:**
  - Retorna o somatório total da quantidade de itens de todos os produtos cadastrados.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **Python 3.12+**
- [tabulate](https://pypi.org/project/tabulate/): Formatação visual de tabelas no terminal.
- [regex](https://pypi.org/project/regex/): Suporte avançado a Expressões Regulares com suporte a propriedades Unicode (`\p{L}`).
- **time:** Controle de fluxo e pausas no terminal.

---

## 🔧 Como Executar o Projeto

1. **Clone ou baixe o repositório:**
   	```bash
   	git clone https://github.com/alauracarlotta/SENAC-faculdade.git
   	cd _TECH/2-semestre/praticas_de_programacao/PTI/desenvolvimento-de-um-sistema-de-controle-de-estoque
	```

2. **Crie e ative o ambiente virtual:**
	```bash
	python -m venv venv

	# No Windows:
	venv\Scripts\activate

	# No Linux/macOS:
	source venv/bin/activate
	```

3. **Instale as dependências:**
	```bash
	pip install -r requirements.txt
	```

4. **Execute a aplicação:**
    ```bash
	python index.py
	```

---

## 📌 Acompanhamento & Issues

O desenvolvimento do projeto e as tarefas pendentes podem ser acompanhados diretamente na issue principal do repositório:

- 🔗 **Issue de Acompanhamento:** [Acompanhe as tarefas e próximos passos aqui](https://github.com/alauracarlotta/SENAC-faculdade/issues/3).

---

## 🧪 Regras de Validação Demonstradas

| Campo | Regra / Restrição |
| :--- | :--- |
| **Código** | Apenas dígitos numéricos (até 13 caracteres, preenchido com zeros à direita via `ljust`); sem duplicatas. |
| **Nome** | Mínimo 3 caracteres; exige pelo menos 3 letras (`\p{L}`). |
| **Preço** | Apenas números não negativos; aceita vírgula ou ponto decimal. |
| **Quantidade** | Apenas números inteiros maiores que zero. |

---

## 📝 Autor

❤️ _[Sobre 'A Laura Carlota'](https://github.com/alauracarlotta)_

Sou jundiaiense de nascimento e paulistana de coração. Curiosa por natureza, adoro aprender e dificilmente desisto de entender alguma coisa. Escolhi a tecnologia porque ela me desafia todos os dias. Fora das telas, gosto de ler, costurar, andar de patins e maratonar séries. Valorizo pessoas, boas conversas e ambientes colaborativos. Estou construindo minha carreira com dedicação e muita vontade de evoluir.
