from django.conf.urls import url

from {{ cookiecutter.project_slug }}.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

app_name = "users"
urlpatterns = [
    url(regex=r"^$", view=user_list_view.as_view(), name="list"),
    url(regex=r"^~redirect/$", view=user_redirect_view.as_view(), name="redirect"),
    url(regex=r"^~update/$", view=user_update_view.as_view(), name="update"),
    url(
        regex=r"^(?P<username>[\w.@+-]+)/$",
        view=user_detail_view.as_view(),
        name="detail",
    ),
]
