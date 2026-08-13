#
#& GERENCIAMENTO DE MÓDULOS COM PIP

#^ ATUALIZA PIP PARA AVERSÃO MAIS RECENTE
# python -m pip install --upgrade pip


#^ VERSÃO
# pip --version


#^ INSTALAÇÃO DE PACOTES
# pip install requests

# pip  install  requests==2.31.0 #* => VERSÃO ESPECÍFICA

# pip  install  ./meu_pacote/  #* => A PARTIR DE PASTAS LOCAIS
# pip install https://exemplo.com/arquivo.tar.gz
# pip install pacote_exemplo-1.0.0-py3-none-any.whl

# pip list  #* => VERIFICA PACOTES INSTALADOS

# pip show nome-do-pacote  #* => DETALHES DE UM PACOTE ESPECÍFICO

# pip list –outdated  #* => VERIFICA PACOTES DESATUALIZADOS

# pip install --upgrade nome-do-pacote  #* => ATUALIZAR PATOTE

# pip uninstall nome-do-pacote  #* => REMOVE UM PACOTE


#^ DEPENDÊNCIAS
#? Outro aspecto importante é a geração de um arquivo com as dependências de um
#? ambiente para garantir que a execução de um aplicativo ou serviço seja
#? realizada nas mesmas condições. Para isso, é comum utilizar um arquivo
#? chamado requirements.txt, o qual pode ser gerado pela opção freeze, apontando
#? a saída do arquivo para ser gravado em requirements.txt

# pip freeze > requirements.txt

# pip install -r requirements.txt  #* INSTALA DEPENDÊNCIAS DO requirements.txt
