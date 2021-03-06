from django.conf.urls import url
from gotquiz import views
from django.contrib import admin
from django.conf.urls import include



urlpatterns = [
	url(r"^$", views.startpage, name="start_page"),
	url(r"^quiz/([0-9]+)/$", views.quiz, name="quiz_page"),
	url(r"^quiz/([0-9]+)/question/([0-9]+)/$", views.question, name="question_page"),
	url(r"^quiz/([0-9]+)/completed/$", views.completed, name="completed_page"),
	url(r"^admin/", include(admin.site.urls)),
	url(r"^quiz/([0-9]+)/question/([0-9]+)/answer/$", views.answer, name="answer_page"),
]

