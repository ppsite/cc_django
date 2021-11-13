from rest_framework.viewsets import ModelViewSet

from media.serializers import ExternalImage, ExternalImageSerializer


class ExternalImageViewSets(ModelViewSet):
    queryset = ExternalImage.objects.all()
    serializer_class = ExternalImageSerializer

    def create(self, request, *args, **kwargs):
        request.data.update({'owner': request.user.id, 'image': request.data['files']})
        return super(ExternalImageViewSets, self).create(request, args, kwargs)
