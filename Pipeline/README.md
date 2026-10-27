Pipeline de Normalização e Tratamento de Dados



Pipeline desenvolvido para lidar com dados de entrada não padronizados, realizando a normalização e o tratamento dos registros recebidos, com o objetivo de validar os dados e separar registros inconsistentes para análise.



Objetivo do Projeto



O principal objetivo deste primeiro projeto é aprimorar minhas habilidades em Python e tratamento de dados, aplicando conceitos relacionados a ETL/ELT e pipelines de dados. A proposta é desenvolver uma solução prática que simule situações encontradas na rotina de um engenheiro de dados, envolvendo normalização, validação e tratamento de registros inconsistentes.



\-----------------------------------------------------------------------------------------------------------------------------------------------------------------------





Instalação e Execução



Pré-requisitos



Python instalado. Versão utilizada no desenvolvimento: 3.14.6.



Para verificar se o Python está instalado, abra o terminal do Windows (Prompt de Comando ou CMD) e execute:



python --version



Caso o comando anterior não funcione, tente:



py --version



Obtenção do projeto



Clone o repositório do projeto no GitHub e acesse a pasta criada.



Execução



Com o terminal aberto na pasta do projeto, execute:



python pipeline.py



Ou, caso utilize o lançador do Windows:



py pipeline.py



\-----------------------------------------------------------------------------------------------------------------------------------------------------------------------



Regras e Fluxo dos Dados



1\. Função pipeline\_trata\_dados()



A função principal é responsável por coordenar o processamento dos registros, executar as validações e consolidar os resultados.



Cópia dos dados



Os registros recebidos são copiados utilizando deepcopy(), permitindo que as alterações sejam realizadas na cópia, preservando os dados originais.



Normalização dos status



Durante a iteração com o loop for, os status são padronizados utilizando os métodos strip() e lower(), removendo espaços nas extremidades e convertendo os caracteres para letras minúsculas.



Validações iniciais



Os registros são encaminhados para a quarentena quando apresentam alguma das seguintes condições:



Valor ausente (None).



Status igual a cancelada.



Status fora do conjunto de valores reconhecidos (aprovada e cancelada).



Valor do tipo booleano (bool).



Conversão dos valores



Dentro do bloco try/except, a condição if verifica se o valor é uma string ou um inteiro. Se uma dessas condições for atendida, o valor é convertido para Decimal.



Valores que já são do tipo Decimal permanecem nesse formato, sem necessidade de conversão adicional.



Caso ocorra um erro durante a conversão, como InvalidOperation ou TypeError, o registro é encaminhado para a quarentena e o processamento continua com o próximo registro.



Direcionamento dos registros



Após as validações e a conversão, os registros com status aprovada são encaminhados para a função acumulador\_vendas(), responsável por verificar os valores e atualizar os indicadores de vendas.



2\. Função acumulador\_vendas()



Essa função recebe o registro, o total acumulado de vendas, a quantidade de vendas aprovadas e a lista de registros reprovados.



Se o valor do registro for maior que zero, ele é somado ao acumulador vendas, e a variável quantidade é incrementada em uma unidade.



Se o valor for menor ou igual a zero, o registro é encaminhado para a quarentena.



Ao final, a função retorna os valores atualizados de vendas e quantidade para a função principal.



3\. Função quarentena()



Essa função adiciona à lista reprovados todos os registros que não atendem às regras de validação estabelecidas.



A lista permite consultar posteriormente os registros rejeitados e analisar possíveis inconsistências nos dados de entrada.



4\. Função relatorio\_final()



Responsável por consolidar os resultados do processamento em um relatório textual.



A função recebe o total de vendas aprovadas, a quantidade de registros aprovados e a quantidade de registros reprovados, retornando um resumo formatado dessas informações.



5\. Consolidação dos resultados



Após o processamento dos registros, a função principal utiliza len(reprovados) para calcular a quantidade de registros armazenados na lista de reprovados. Esse número é atribuído à variável qtde\_reprovados.



Em seguida, a função relatorio\_final() é chamada, e o resultado é armazenado na variável final.



Por fim, o pipeline retorna dois elementos:



final: relatório com os resultados do processamento.



reprovados: lista contendo os registros rejeitados.



Na chamada da função, esses retornos são atribuídos às variáveis relatorio e reprovado, respectivamente.



A função print() pode ser utilizada para exibir o relatório ou consultar a lista de registros reprovados.





Exemplo de Saída



Após executar o pipeline com o conjunto de dados de teste, o relatório apresenta o seguinte resultado:



Vendas aprovadas: R$1026.51

Aprovados: 9

Reprovados: 11



O resultado demonstra a consolidação dos valores aprovados e a contabilização dos registros encaminhados para a quarentena durante o processamento.

