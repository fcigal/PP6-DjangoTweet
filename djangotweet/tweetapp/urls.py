from django.urls import path
from . import views

app_name = "tweetapp"

urlpatterns = [
    path('',views.tweetlist, name='tweetlist'), # atilsamacioglu/tweetapp/
    path('/tweetadd',views.tweetadd, name='tweetadd'), # atilsamacioglu/tweetapp/tweetadd
    path('/addtweetbyform',views.addtweetbyform, name="addtweetbyform"), # atilsamacioglu/tweetapp/addtweetbyform
    path('/addtweetbymodelform',views.addtweetbymodelform, name="addtweetbymodelform"), # atilsamacioglu/tweetapp/addtweetbymodelform
    path('signup/',views.SignUpView.as_view(), name="signup"),
    path('deletetweet/<int:id>', views.deletetweet, name="deletetweet")
]
