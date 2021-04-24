from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS

from tutorial.quickstart.models import Tweet


class IsTweetAuthorOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj: Tweet):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user and
            request.user.is_authenticated and
            obj.author == request.user
        )
