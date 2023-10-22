def data_bd(data):
  # print(data)
  data_split = data.split("/")
  if len(data_split) > 1:
    return '\''+data_split[2]+"-"+data_split[1]+"-"+data_split[0]+" 00:00:00"+'\''
  else:
    if len(data) > 0:
      return '\''+data+'\''
    else:
      return 'null';


f = open("TOTAL 2018 - 2020.csv", "r")
g = open("bd_registro_inpi.txt", "w")

g.write(f"DROP TABLE rsw_registro;\n")
g.write(f"DROP TABLE rsw_reg_linguagem;\n")
g.write(f"DROP TABLE rsw_reg_campo_aplicacao;\n")
g.write(f"DROP TABLE rsw_reg_tipo_programa;\n")
g.write(f"DROP TABLE rsw_reg_nome_titular;\n")
g.write(f"DROP TABLE rsw_reg_nome_autor;\n\n")

g.write(f"CREATE TABLE rsw_registro ( id int, numero_registro varchar(12), data_deposito datetime, titulo_programa text, nome_procurador text, numero_rpi text, data_publicacao_rpi datetime, numero_despacho text, descricao_depacho varchar(512), complemento_despacho text, data_lancamento datetime, data_protocolo_externo datetime, primary key (id));\n")
g.write(f"CREATE TABLE rsw_reg_linguagem ( numero_registro varchar(12), linguagem varchar(256), primary key(numero_registro, linguagem) );\n")
g.write(f"CREATE TABLE rsw_reg_campo_aplicacao ( numero_registro varchar(12), campo_aplicacao varchar(5), primary key(numero_registro, campo_aplicacao) );\n")
g.write(f"CREATE TABLE rsw_reg_tipo_programa ( numero_registro varchar(12), tipo_programa varchar(5), primary key(numero_registro, tipo_programa) );\n")
g.write(f"CREATE TABLE rsw_reg_nome_titular ( numero_registro varchar(12), nome_titular varchar(512), primary key(numero_registro, nome_titular) );\n")
g.write(f"CREATE TABLE rsw_reg_nome_autor ( numero_registro varchar(12), nome_autor varchar(512), primary key(numero_registro, nome_autor) );\n\n")

ctrRegistro = []
ctrLinguagem = []
ctrCampoAplicacao = []
ctrTipoPrograma = []
ctrNomeTitular = []
ctrNomeAutor = []
i = 0
for x in f:
  # pulando a primeira linha
  if i == 0:
    i += 1
    continue

  vLinha = x.split('|')
  # print(vLinha)
  Numero_Registro = vLinha[0].strip()
  Data_Deposito = vLinha[1].strip()
  Linguagem = vLinha[2].replace(' ', '')
  Campo_Aplicacao = vLinha[3].replace(' ', '')
  Titulo_Programa = vLinha[4].replace("\"",'').strip()
  Tipo_Programa = vLinha[5].replace(' ', '')
  Nome_Titular = vLinha[6].replace("'"," ").strip()
  Nome_Autor = vLinha[7].replace("'"," ").strip()
  Nome_Procurador = vLinha[8].replace("'"," ").strip()
  Numero_RPI = vLinha[9].strip()
  Data_Publicacao_RPI = vLinha[10].strip()
  Numero_Despacho = vLinha[11].strip()
  Descricao_Despacho = vLinha[12].strip()
  Complemento_Despacho = vLinha[13].strip()
  Data_Lancamento = vLinha[14].strip()
  Data_Protocolo_Externo = vLinha[15].strip()
  # Codigo_Sigilo_Programa = vLinha[16] # .replace('\n', '')

  vetorLinguagem = Linguagem.split('/')
  vetorLinguagem = list(dict.fromkeys(vetorLinguagem))
  vetorCampo_Aplicacao = Campo_Aplicacao.split('/')
  vetorCampo_Aplicacao = list(dict.fromkeys(vetorCampo_Aplicacao))
  vetorTipo_Programa = Tipo_Programa.split('/')
  vetorTipo_Programa = list(dict.fromkeys(vetorTipo_Programa))
  vetorNome_Titular = Nome_Titular.split('/')
  vetorNome_Titular = [ii.strip() for ii in vetorNome_Titular]
  vetorNome_Titular = list(dict.fromkeys(vetorNome_Titular))
  vetorNome_Autor = Nome_Autor.split('/')
  vetorNome_Titular = [ii.strip() for ii in vetorNome_Autor]
  vetorNome_Autor = list(dict.fromkeys(vetorNome_Autor))

  # print(Numero_Registro)
  # if Numero_Registro == '512018000328':
  #   print(vetorNome_Titular)

  g.write(f"INSERT INTO rsw_registro VALUES ({i}, '{Numero_Registro}','{Data_Deposito}','{Titulo_Programa}','{Nome_Procurador}','{Numero_RPI}',{data_bd(Data_Publicacao_RPI)},'{Numero_Despacho}','{Descricao_Despacho}','{Complemento_Despacho}',{data_bd(Data_Lancamento)},{data_bd(Data_Protocolo_Externo)}); \n")
  i += 1

  # LINGUAGEM #
  if Numero_Registro not in ctrLinguagem:
    ctrLinguagem.append(Numero_Registro)
    # g.write("-- TABELA LINGUAGEM --")
    if len(vetorLinguagem) == 1:
      # print(Linguagem)
      g.write(f"INSERT INTO rsw_reg_linguagem VALUES ('{Numero_Registro}', '{Linguagem}'); \n")
    else:
      for item in vetorLinguagem:
        # print(item)
        g.write(f"INSERT INTO rsw_reg_linguagem VALUES ('{Numero_Registro}', '{item}'); \n")
    # i += 1
    # if i == 10: break
  # else:
  #   print('Tentou repetir para LINGUAGEM '+Numero_Registro)

  # CAMPO APLICAÇÃO #

  if Numero_Registro not in ctrCampoAplicacao:
    ctrCampoAplicacao.append(Numero_Registro)
    if len(vetorCampo_Aplicacao) == 1:
      g.write(f"INSERT INTO rsw_reg_campo_aplicacao VALUES ('{Numero_Registro}', '{Campo_Aplicacao}'); \n")
    else:
      for item in vetorCampo_Aplicacao:
        g.write(f"INSERT INTO rsw_reg_campo_aplicacao VALUES ('{Numero_Registro}', '{item}'); \n")
  # else:
  #   print('Tentou repetir para CAMPO APLICACAO '+Numero_Registro)

  # TIPO PROGRAMA #
  if Numero_Registro not in ctrTipoPrograma:
    ctrTipoPrograma.append(Numero_Registro)
    if len(vetorTipo_Programa) == 1:
      g.write(f"INSERT INTO rsw_reg_tipo_programa VALUES ('{Numero_Registro}', '{Tipo_Programa}'); \n")
    else:
      for item in vetorTipo_Programa:
        g.write(f"INSERT INTO rsw_reg_tipo_programa VALUES ('{Numero_Registro}', '{item}'); \n")
  # else:
  #   print('Tentou repetir para TIPO PROGRAMA '+Numero_Registro)

  # NOME DO TITULAR: #
  if Numero_Registro not in ctrNomeTitular:
    ctrNomeTitular.append(Numero_Registro)
    if len(vetorNome_Titular) == 1:
      g.write(f"INSERT INTO rsw_reg_nome_titular VALUES ('{Numero_Registro}', '{Nome_Titular.replace(' ', '|').replace('||', ' ').replace('|', '').strip()}'); \n")
    else:
      for item in vetorNome_Titular:
        g.write(f"INSERT INTO rsw_reg_nome_titular VALUES ('{Numero_Registro}', '{item.replace(' ', '|').replace('||', ' ').replace('|', '').strip()}'); \n")
  # else:
  #   print('Tentou repetir para NOME TITULAR '+Numero_Registro)

  # NOME DO TITULAR: #
  if Numero_Registro not in ctrNomeAutor:
    ctrNomeAutor.append(Numero_Registro)
    if len(vetorNome_Autor) == 1:
      g.write(f"INSERT INTO rsw_reg_nome_autor VALUES ('{Numero_Registro}', '{Nome_Autor.replace(' ', '|').replace('||', ' ').replace('|', '').strip()}'); \n")
    else:
      for item in vetorNome_Autor:
        g.write(f"INSERT INTO rsw_reg_nome_autor VALUES ('{Numero_Registro}', '{item.replace(' ', '|').replace('||', ' ').replace('|', '').strip()}'); \n")
  # else:
  #   print('Tentou repetir para NOME AUTOR '+Numero_Registro)
g.close()
f.close()