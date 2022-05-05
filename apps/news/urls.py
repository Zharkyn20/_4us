from .views import PostViewSet


"""
This variable used in zeonProject/urls as News' app's urls.
Then registering in Api Root
"""
routeList = (
    (r'posts', PostViewSet),
)