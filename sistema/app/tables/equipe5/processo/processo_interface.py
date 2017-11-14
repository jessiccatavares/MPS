from flask_mysqldb import MySQL

class ProcessoInterface:

    def __init__(self, app):
        self.mysql = MySQL(app)

    def execute_query(self, query, insert=False):
        cur = self.mysql.connection.cursor()
        cur.execute(query)
        if insert:
            self.mysql.connection.commit()
        else:
            data = cur.fetchall()
            cur.close()
            return data

    # CRUD - PROCESSO

    def cadastra_processo(self, processo):
        self.execute_query("insert into processo (processo_descricao, processo_tipo) values ('{}')".format(processo_descricao,processo_tipo), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from processo")
        return data[0]['last']

    #def cadastra_lotacao(self, funcionario_id, lotacao):
    #    self.execute_query("insert into lotacao (funcionario_id, setor_id)  values('{}', '{}')" .format(funcionario_id, lotacao.get_setor().get_id()), True)

    '''def get_lotacao_ativa(self, funcionario_id):
        data = self.execute_query("select * from lotacao where lotacao.funcionario_id = '{}' order by lotacao.lotacao_id desc limit 1".format(funcionario_id))

        if len(data) < 1:
            return None

        return data[0]'''

    def get_processos_ids(self):
        data = self.execute_query("select processo_id from processo")
        return data

    def edita_processo(self, processo):
        self.execute_query("update processo set processo_descricao = '{}',processo_tipo = '{}' where processo_id = '{}'".format(processo.descricao,processo.tipo, processo.get_id()), True)

    def deleta_processo(self, processo_id):
        self.execute_query("update processo set processo_situacao = 1 where processo_id = '{}'".format(processo_id), True)

    def get_processo(self, processo_id):
        data = self.execute_query("select * from processo where processo_id = '{}' limit 1".format(processo_id))
        if len(data) < 1:
            return None
        return data[0]
