from .processo_cadastrar_form import CadastrarProcessoForm
from ...tables.processo.processo_modelo import Processo
from ...utils.flash_errors import flash_errors
from ...utils.zelda_modelo import ZeldaModelo
from ...utils.files import flash_errors_extensao

from flask import render_template, flash, redirect, url_for

class ProcessoCadastrarNegocio:

    def exibir():
        form = CadastrarProcessoForm()

        if form.validate_on_submit():
            processo = Processo()
            processo.descricao = form.processo_descricao.data
            processo.tipo = form.processo_tipo.data
            processo.salva()

            return redirect(url_for('processo_cadastrar'))
        else:
            flash_errors(form)

        return render_template('processo_criar.html', form=form)