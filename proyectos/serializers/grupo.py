from rest_framework import serializers
from proyectos.models import Grupo

class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupo
        fields = ['id', 'nombre_grupo']
