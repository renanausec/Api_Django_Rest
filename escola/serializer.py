from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento'] #posso usar __all__ também para disponibilizar todos os dados ao invés de escrever um por um. o fields é um filtro do que eu quero disponibilizar para minha API

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] #adiciona todos os campos excluindo um ou mais campos de aparecerem lá (se deixar ele vazio, mostra tudo tambem)

#para conseguir ver as matriculas de um aluno e depois ver todos alunos matriculados em cada curso faremos o seguinte:

class ListaMatriculasAlunosSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome') #isso traz lá do nosso models.py diretamente o nome do Aluno
    class Meta:
        model = Matricula
        fields = ['aluno_nome']