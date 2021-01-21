from django.shortcuts import render
from django.conf import settings
from .models import Bank, Branch
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import BranchSerializer
from django.db.models import Q
import json
import os



class ListBranch(ListAPIView):
    """
    Lists branches based on the branch name
    """
    serializer_class = BranchSerializer

    def list(self, request, *args, **kwargs):
        branch_name = request.GET.get('q')
        queryset = Branch.objects.filter(branch__icontains=branch_name)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class SearchBranch(ListAPIView):
    """
    Lists branches by searching on every column
    """
    serializer_class = BranchSerializer

    def list(self, request, *args, **kwargs):
        query = request.GET.get('q')
        queryset = Branch.objects.filter(Q(branch__icontains=query)
        |Q(ifsc__icontains = query)|Q(address__icontains = query)|
        Q(state__icontains = query)|Q(district__icontains = query)|
        Q(city__icontains = query)|Q(bank_id__name__icontains = query))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BranchDetail(RetrieveAPIView):
    """
    Retrieve Branch Details
    """
    serializer_class = BranchSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = Branch.objects.get(id = kwargs['id'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class SearchBranchCity(ListAPIView):
    """
    Lists branches by searching on city
    """
    serializer_class = BranchSerializer

    def list(self, request, *args, **kwargs):
        query = request.GET.get('q')
        queryset = Branch.objects.filter(Q(city__icontains = query))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@api_view()
def invert_favourite(request):
    """
    Marks the object as favourite
    """
    id = request.GET.get('id')
    try:
        branch = Branch.objects.get(id=id)
    except:
        return Response({"result":"Not Found"})
    branch.favourite = not branch.favourite
    branch.save()
    return Response({"result":"done"})

class FavouriteBranchReturn(ListAPIView):
    """
    Lists branches by searching on every column
    """
    serializer_class = BranchSerializer

    def list(self, request, *args, **kwargs):
        query = request.GET.get('q')
        queryset = Branch.objects.filter(favourite=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)