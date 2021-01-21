from rest_framework import serializers
from .models import Branch, Bank


class BranchSerializer(serializers.ModelSerializer):
    """
    Serializes the branch queryset
    """
    class Meta:
        model = Branch
        fields = "__all__"
        depth = 1