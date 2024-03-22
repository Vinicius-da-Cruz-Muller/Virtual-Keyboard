# Virtual Keyboard
 
Teclado Virtual para sites.

* Este teclado gera os números em posições aleatórias, que vão ficar variando entre os acessos do usuário. Assim, mesmo que você consiga saber quais botões o usuário utilizou, você não tem certeza da senha correta.

* Ao acessar de novo a página algum tempo depois, teremos outro teclado. Teremos novamente 64 combinações, mas nem todas essas combinações são iguais às do conjunto anterior.

# Arquitetura e stack

Detalhes da stack e integrações:

- `Implementação em Python 3`: Linguagem de programação amplamente usada em aplicações da Web, desenvolvimento de software, ciência de dados e machine learning (ML).
- `Uso do framework Flask`: Framework web para Python. Utilizado neste projeto principalmente para criação de rotas entre as páginas.
- `Persistência de dados em MySQL`: Uso da biblioteca mysql-connector-python. MySQL oferece recursos de segurança robustos, incluindo autenticação, autorização e criptografia de dados, para proteger seus dados contra acesso não autorizado e ataques.
- `Uso do algoritmo bcrypt`: Algoritmo de hash e criptografia. Uso da biblioteca bcrypt.

# Execução do código

Para executar o serviço é necessário configurar as variáveis de ambiente:

# Alterações e testes

Toda alteração no código deve ser realizada respeitando o processo de Git Flow definido.
#
Os testes automatizados são executados através da ferramenta pytest.
