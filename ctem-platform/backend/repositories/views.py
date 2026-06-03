from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Repository
from .serializers import RepositorySerializer


def repository_list(request):

    repositories = Repository.objects.all()

    return render(
        request,
        "repositories/list.html",
        {
            "repositories": repositories
        }
    )


class RepositoryApiView(APIView):

    def get(self, request):

        repos = Repository.objects.all()

        return Response(
            RepositorySerializer(
                repos,
                many=True
            ).data
        )

    def post(self, request):

        serializer = RepositorySerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data
            )

        return Response(
            serializer.errors,
            status=400
        )