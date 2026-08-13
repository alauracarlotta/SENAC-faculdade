# CRIANDO OS SEUS PRÓPRIOS MÓDULOS

## ?Além de consumir pacotes criados por outros desenvolvedores, o Python também permite que você crie seus próprios módulos e os torne instaláveis via pip. Essa prática é útil tanto para organizar seus projetos quanto para compartilhar bibliotecas com outras pessoas ou times.

### Um pacote Python precisa seguir uma estrutura mínima para ser reconhecido corretamente. Por exemplo:

```m
|/meu_pacote/
|----meu_pacote/	 #Diretório com o código fonte
|----|----init  .py
| modulo.py
| README.md
| setup.py
| pyproject.toml
| LICENSE
```

Cada arquivo dentro da estrutura de pastas possui diferente papéis, como segue:

    • init.py: indica que o diretório é um pacote Python.

    • setup.py: define metadados e instruções de instalação.

    • pyproject.toml: especifica as dependências de build (recomendado para novas versões do Python).

    • README.md: documentação básica.

    • LICENSE: tipo de licença (MIT, GPL etc.).


### Para versões anteriores do Python, é utilizando o arquivo setup.py para configurar a instalação, definir metadados e instalar as dependências, conforme a seguir.

```python
from setuptools import setup, find_packages

setup(
    name="meu_pacote",
    version="0.1.0",
    description="Um pacote de exemplo para demonstração com pip",
    author="Seu Nome",
 
    author_email="seu@email.com",

    packages=find_packages(),
    install_requires=[],	# dependências, se houver
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
```

### Explicando a composição do arquivo setup.py:

    • setuptools: é uma biblioteca que substitui o antigo distutils e oferece ferramentas mais modernas e flexíveis para empacotar projetos Python.

    • find_packages(): detecta automaticamente todos os pacotes e subpacotes dentro de seu projeto (ou seja, diretórios com  init . py). Isso evita a necessidade de listá-los manualmente.


### Na função setup(), existem os seguintes parâmetros:

    • name: nome do pacote como ele será reconhecido no pip e no PyPI. Evite espaços e caracteres especiais.

    • version: versão atual de seu pacote. É uma boa prática seguir o versionamento semântico (ex: MAJOR.MINOR.PATCH).

    • description: uma descrição curta e clara do que seu pacote faz.

    • author / author_email: informações sobre quem criou o pacote. Isso é exibido no PyPI e ajuda a identificar o responsável.

    • packages: lista dos diretórios que contêm código-fonte. find_packages() busca automaticamente por eles. Você também pode passar uma lista manual, como [‘meu_pacote’].

    • install_requires: lista de pacotes que seu projeto depende para funcionar corretamente. Eles serão instalados automaticamente com seu pacote.

    • classifiers: metadados padronizados utilizados pelo PyPI para classificar e descrever seu pacote. Eles ajudam na busca por pacotes com características específicas.


> ## Importante

* Muitos projetos usam o pyproject.toml como padrão moderno. O setup.py ainda é aceito, mas pode ser substituído gradualmente.

* Nos casos em que se opte pelo uso do arquivo pyproject.toml, segue um exemplo de preenchimento:

Exemplo 2

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend  =  "setuptools.build_meta"

[project]
name = "meu_pacote"
version = "0.1.0"
description = "Um pacote de exemplo para demonstração com pip"
authors = [{
	name = "Seu Nome", email = "seu@email.com"
}]
license = { text = "MIT" }
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
	"requests>=2.25",
	"pandas>=1.0,<2.0"
]

[project.urls]
"Homepage"  =  "https://github.com/seunome/meu_pacote"
"Documentação" = "https://meu-pacote.readthedocs.io"
```


### Explicando a composição do arquivo pyproject.toml:

    • [build-system]
    • Define o backend de empacotamento e suas dependências mínimas.
    • setuptools e wheel são os mais comuns.
    • O setuptools>=61.0 é necessário para suportar o novo formato via pyproject.toml.
    • [project]
    • Metadados do pacote: nome, versão, descrição, autor, licença etc.
    • requires-python: especifica a versão mínima do Python.
    • dependencies: lista de pacotes necessária para o funcionamento do projeto.
    • [project.urls] (opcional)
    • URLs úteis: site do projeto, documentação, repositório GitHub etc.


### Para empacotar a solução e instalar, o próximo passo é gerar o arquivo de distribuição, através do comando:

```python
python -m build
```

### Para instalá-lo localmente, deve ser usado o comando pip buscando arquivos para a instalação local com o comando:

```python
pip install .
```


### O pacote também pode ser publicado no PyPI através do comando twine, de maneira que qualquer pessoa possa instalar seu pacote remotamente:

```
twine upload dist/*
```

# *PARA SABER MAIS*

Publicar pacotes no PyPI (Python Package Index) é o passo final para compartilhar seu código Python com a comunidade de forma padronizada e acessível via pip install. Para isso, é necessário ter uma conta no PyPI, criar um arquivo pyproject.toml ou setup.py(opens in a new tab) com os metadados do pacote, gerar os arquivos de distribuição usando a ferramenta build e, por fim, fazer o upload com o twine. Com esses passos, qualquer pessoa poderá instalar seu pacote diretamente do PyPI, o que facilita a reutilização de código, a colaboração entre desenvolvedores e a disseminação de soluções úteis de forma segura e organizada.
