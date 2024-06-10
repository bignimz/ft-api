from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .models import FamilyMember, Relationship
from .serializers import FamilyMemberSerializer, RelationshipSerializer

# Family Members Endpoints
class FamilyMembersList(generics.ListCreateAPIView):
    queryset = FamilyMember.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = FamilyMemberSerializer

class FamilyMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FamilyMember.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FamilyMemberSerializer

class FamilyMemberCreate(generics.CreateAPIView):
    queryset = FamilyMember.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    serializer_class = FamilyMemberSerializer

    def perform_create(self, serializer):
        # Get the parent member ID from the request data
        parent_id = self.request.data.get('parent', None)
        
        # Create the new family member
        new_member = serializer.save()

        if parent_id:
            # Create a relationship between the new member and the parent
            Relationship.objects.create(parent_id=parent_id, child=new_member)

class FamilyMemberUpdate(generics.UpdateAPIView):
    queryset = FamilyMember.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = FamilyMemberSerializer

class FamilyMemberDelete(generics.DestroyAPIView):
    queryset = FamilyMember.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = FamilyMemberSerializer

# Relationships Endpoints
class RelationshipsList(generics.ListCreateAPIView):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

class RelationshipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

class RelationshipCreate(generics.CreateAPIView):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

class RelationshipUpdate(generics.UpdateAPIView):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

class RelationshipDelete(generics.DestroyAPIView):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
