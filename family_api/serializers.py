from rest_framework import serializers
from .models import FamilyMember, Relationship, FamilyTree

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'

class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = '__all__'


class FamilyTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyTree
        fields = '__all__'