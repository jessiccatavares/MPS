from ...cursor import db


class Processo:

    def __init__(self, processo_id = None):
        
        self.__processo_id = None
        self.descricao = None
        self.tipo = None

        if processo_id is not None:

            data = db.get_processo(processo_id)
            if data is not None:

                self.__processo_id = processo_id
                self.descricao = data['processo_descricao']
                self.tipo =   data['processo_tipo']


    def get_id(self):
        return self.__processo_id

    def salva(self):
        if self.get_id() is not None:
            db.edita_processo(self)
        else:
            self.__processo_id = db.cadastra_processo(self)

    def serializa(self):
        return {
                "id": self.get_id(),
                "descricao": self.descricao,
                "tipo": self.tipo
                }