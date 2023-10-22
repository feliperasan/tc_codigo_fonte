-- Visualizando Informações na Tabela de Registros
SELECT * FROM rsw_registro;

/**
	Filtrando informações por ano para finalidade de colher a quantidade de
    "Expedição do Certificado de Registro" por ano, e criando uma nova tabela com
    as colunas dos anos e descrição do despacho.
*/
SELECT data_publicacao_rpi, COUNT(*) AS `2018`
FROM rsw_registro
WHERE YEAR(data_publicacao_rpi) = 2018 AND descricao_despacho LIKE "Expedição do Certificado de Registro";

SELECT DISTINCT data_publicacao_rpi, COUNT(*) AS `2019`
FROM rsw_registro
WHERE YEAR(data_publicacao_rpi) = 2019 AND descricao_despacho LIKE "Expedição do Certificado de Registro";

SELECT data_publicacao_rpi, COUNT(*) AS `2020`
FROM rsw_registro
WHERE YEAR(data_publicacao_rpi) = 2020 AND descricao_despacho LIKE "Expedição do Certificado de Registro";


CREATE TABLE quantidade_ano (
  	descricao_despacho VARCHAR(512),
	ano YEAR,
  	quantidade INT
);

/*
	Inserido informações a tabela criada nomeada de "quantidade_ano".
*/

INSERT INTO quantidade_ano(descricao_despacho, ano, quantidade) 
VALUES ("Expedição do Certificado de Registro", 2018, 2407),
("Expedição do Certificado de Registro", 2019, 2999),
("Expedição do Certificado de Registro", 2020, 2907),
("Expedição do Certificado de Registro", 2021, 37);

-- Criando csv da tabela quantidade_ano.
SELECT * FROM quantidade_ano
INTO OUTFILE '/home/felipe/Documentos/data-csv/quantidade_ano.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';


/* ------ EXTRAÍNDO RANKING DE TECNOLOGIAS ------ */
-- Atualizando Informações
UPDATE rsw_reg_linguagem SET linguagem = "C#" WHERE linguagem = "C-SHARP";
UPDATE rsw_reg_linguagem SET linguagem = "SWIFT" WHERE linguagem = "SWIFT...";
UPDATE rsw_reg_linguagem SET linguagem = "T-SQL" WHERE linguagem = "T-SQL...";
-- Deletando Informações
DELETE FROM rsw_reg_linguagem WHERE linguagem LIKE "...";

-- Extraíndo csv de Tecnologias
SELECT *, COUNT(*) AS qtd
FROM rsw_reg_linguagem
GROUP BY linguagem
ORDER BY qtd DESC
INTO OUTFILE '/home/felipe/Documentos/data-csv/linguagem.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';


/* ------ CAMPO DE APLICAÇÃO DE SOFTWARES REGISTRADOS ------ */
SELECT *, COUNT(*) AS qtd
FROM rsw_reg_campo_aplicacao
GROUP BY campo_aplicacao
ORDER BY qtd DESC
INTO OUTFILE '/home/felipe/Documentos/data-csv/campo_aplicacao.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/* ------ TIPO DE PROGRAMA DE SOFTWARES REGISTRADOS ------ */
SELECT *, COUNT(*) AS qtd
FROM rsw_reg_tipo_programa
GROUP BY tipo_programa
ORDER BY qtd DESC
INTO OUTFILE '/home/felipe/Documentos/data-csv/tipo_programa.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/* ------ NOME DO TITULAR ------ */
-- Excluíndo linha de titular 512018000138 ... 56
DELETE FROM rsw_reg_nome_titular WHERE nome_titular LIKE "...";

SELECT *, COUNT(*) AS qtd
FROM rsw_reg_nome_titular
WHERE nome_titular LIKE '%UNIVERSIDADE%' OR nome_titular LIKE '%CENTRO%' OR nome_titular LIKE '%FUNDACAO%'
OR nome_titular LIKE '%TECNOLOGIA%'
GROUP BY nome_titular
ORDER BY qtd DESC;
INTO OUTFILE '/home/felipe/Documentos/data-csv/nome_titular.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/* ------ EXTRAINDO TITULO DO PROGRAMA ------ */
SELECT id, titulo_programa AS keywords, COUNT(*) AS searches
FROM rsw_registro
WHERE descricao_despacho LIKE "Expedição do Certificado de Registro"
GROUP BY titulo_programa
ORDER BY searches DESC
INTO OUTFILE '/home/felipe/Documentos/data-csv/titulo_programa.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/* ----- DELETANDO INFORMAÇÕES 2021 ----- */
DELETE FROM rsw_registro WHERE YEAR(data_publicacao_rpi) = 2021;

/* ------ REGISTROS POR MÊS DE CADA ANO ------ */
SELECT DATE_FORMAT(data_publicacao_rpi, "%m/%Y"), COUNT(*) AS quantidade
FROM rsw_registro
WHERE descricao_despacho LIKE "Expedição do Certificado de Registro"
GROUP BY DATE_FORMAT(data_publicacao_rpi, "%m/%Y")
ORDER BY DATE_FORMAT(data_publicacao_rpi, "%m/%Y")
INTO OUTFILE '/home/felipe/Documentos/data-csv/publicacao_mes_ano.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';


/* TECNOLOGIAS SELECT POR QUANTIDADE */
SELECT * , COUNT(*) AS qtd
FROM rsw_reg_linguagem
GROUP BY linguagem
ORDER BY qtd DESC;

/*----- TIPOS DE PROGRAMAS POR QUANTIDADE -----*/
SELECT *, COUNT(*) AS qtd
FROM rsw_reg_tipo_programa
GROUP BY tipo_programa
ORDER BY qtd DESC;


-- INFORMAÇÕES QUE NÃO FORAM UTILIZADAS NA PESQUISA, APENAS PARA NÍVEL DE CURIOSIDADE.

/*----- VERIFICANDO INFORMAÇÕES DO CAMPO DE APLICAÇÃO QUE COMEÇAM COM IF ------*/
SELECT *, COUNT(*) AS qtd
FROM rsw_reg_campo_aplicacao
where campo_aplicacao LIKE "IF%"
GROUP BY campo_aplicacao
ORDER BY qtd DESC;

/* ------ NOME DOS AUTORES QUE REGISTRARAM SOFTWARES ------ */
-- Extraíndo CSV
SELECT *, COUNT(*) AS qtd
FROM rsw_reg_nome_autor
GROUP BY nome_autor
ORDER BY qtd DESC
INTO OUTFILE '/home/felipe/Documentos/data-csv/nome_autor.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/*--- INNER JOINS PARA VERIFICAR AS TECNOLOGIAS QUE CADA CAMPO DE APLICAÇÃO FAZ USO ---*/
SELECT DISTINCT rsw_reg_linguagem.linguagem, rsw_reg_campo_aplicacao.campo_aplicacao, COUNT(*) as qtd
FROM rsw_reg_linguagem
INNER JOIN rsw_reg_campo_aplicacao
ON rsw_reg_linguagem.numero_registro = rsw_reg_campo_aplicacao.numero_registro
GROUP BY linguagem
ORDER BY qtd DESC;

/*--- INNER JOINS PARA VERIFICAR AS TECNOLOGIAS QUE CADA TIPO DE PROGRAMA FAZ USO ---*/
SELECT rsw_reg_linguagem.linguagem, rsw_reg_tipo_programa.tipo_programa, COUNT(*) as qtd
FROM rsw_reg_linguagem
INNER JOIN rsw_reg_tipo_programa
ON rsw_reg_linguagem.numero_registro = rsw_reg_tipo_programa.numero_registro
GROUP BY linguagem
ORDER BY qtd DESC;