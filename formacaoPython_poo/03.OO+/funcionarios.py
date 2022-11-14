class Funcionario:
    def registrarHoras(self, horas):
        print('Horas registradas!')

    def mostrarTarefas(self):
        print('Apresentar tarefas.')


class Caelum(Funcionario):
    def mostrarTarefas(self):
        print('Apresentar tarefas Caelumer.')

    def buscarCursoMes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos do mês atual!')


class Alura(Funcionario):
    def mostrarTarefas(self):
        print('Apresentar tarefas Alurete.')

    def buscarPerguntasSemResposta(self):
        print('Mostrando perguntas não respondidas do fórum!')


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


jose = Junior()
jose.buscarPerguntasSemResposta()

luan = Pleno()
luan.buscarPerguntasSemResposta()
luan.buscarCursoMes()
luan.mostrarTarefas()