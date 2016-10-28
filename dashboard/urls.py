from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name="login"),
    url(r'^index/$', views.IndexView.as_view(), name="index"),
    url(r'^blank/$', views.BlankView.as_view(), name="blank"),
    url(r'^buttons/$', views.ButtonsView.as_view(), name="buttons"),
    url(r'^flot/$', views.FlotView.as_view(), name="flot"),
    url(r'^forms/$', views.FormsView.as_view(), name="forms"),
    url(r'^grid/$', views.GridView.as_view(), name="grid"),
    url(r'^icons/$', views.IconsView.as_view(), name="icons"),
    url(r'^morris/$', views.MorrisView.as_view(), name="morris"),
    url(r'^notifications/$', views.NotificationsView.as_view(), name="notifications"),
    url(r'^panels/$', views.PanelsView.as_view(), name="panels"),
    url(r'^tables/$', views.TablesView.as_view(), name="tables"),
    url(r'^typography/$', views.TypographyView.as_view(), name="typography"),

    url(r'^quizavg/$', views.QuizAvgView.as_view(), name="quizavg"),
    url(r'^studentavg/$', views.StudentAvgView.as_view(), name="studentavg"),
]
