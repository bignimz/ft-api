from django.urls import path
from .views import FamilyMembersList, FamilyMemberDetail, FamilyMemberCreate, FamilyMemberUpdate, FamilyMemberDelete, RelationshipsList, RelationshipDetail, RelationshipCreate, RelationshipUpdate, RelationshipDelete

urlpatterns = [
    # Family Members Endpoints
    path('family-members/', FamilyMembersList.as_view(), name='family-members-list'),
    path('family-members/<int:pk>/', FamilyMemberDetail.as_view(), name='family-member-detail'),
    path('family-members/add/', FamilyMemberCreate.as_view(), name='family-member-create'),
    path('family-members/<int:pk>/update/', FamilyMemberUpdate.as_view(), name='family-member-update'),
    path('family-members/<int:pk>/delete/', FamilyMemberDelete.as_view(), name='family-member-delete'),

    # Relationships Endpoints
    path('relationships/', RelationshipsList.as_view(), name='relationships-list'),
    path('relationships/<int:pk>/', RelationshipDetail.as_view(), name='relationship-detail'),
    path('relationships/add/', RelationshipCreate.as_view(), name='relationship-create'),
    path('relationships/<int:pk>/update/', RelationshipUpdate.as_view(), name='relationship-update'),
    path('relationships/<int:pk>/delete/', RelationshipDelete.as_view(), name='relationship-delete'),
]