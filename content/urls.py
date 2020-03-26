from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include, path
from nitadda import settings
from . import views

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^meetOurTeam/$', views.Meet_Our_Team),
                  url(r'^upvote/$', views.Upvote),
                  url('upload_note/', views.UploadNote, name='Upload_Note'),
                  url('approvenote/(?P<noteid>\w+)', views.Approve_Note, name='Approve_Note'),
                  url(r'^deletenote/(?P<noteid>\w+)', views.Delete_Note, name='Delete_Note'),
                  url(r'^shownotes/(?P<noteid>\w+)', views.Display_Pdf, name='Display_Pdf'),
                  url(r'^shownote/(?P<courseid>\w+)', views.Show_Note, name='Show_Note'),
                  url(r'^showsubjectnote/(?P<subjectid>\w+)', views.Show_Subject_Note, name='Show_Subject_Note'),
                  url(r'getSubjects/', views.getSubjects),
                  url('login/', views.admin_login, name='admin_login'),
                  url('logout/', views.admin_logout, name='admin_logout'),
                  url(r'^add_course$', views.Add_Course, name='Add_Course'),
                  url(r'^add_subject$', views.Add_Subject, name='Add_Subject'),
                  url(r'^course$', views.course_list, name='course_list'),
                  # url(r'^all_note$', views.Get_Note, name='Get_Note'),
                  url(r'^all_subject_note$', views.Get_Subject_Note, name='Get_Subject_Note'),
                  url(r'^all_course$', views.Get_Course, name='Get_Course'),
                  url(r'^all_subject$', views.Get_Subject, name='Get_Subject'),
                  # url(r'^course/(?P<pk>\d+)/$', views.course_detail, name='course_detail'),

                  url(r'^show_liked_notes$', views.Show_Liked_Notes, name='Show_Liked_Notes'),
                  url(r'^show_uploaded_notes$', views.Show_Uploaded_Notes, name='Show_Uploaded_Notes'),
                  # url(r'^recent_note/(?P<courseid>\w+)', views.Recent_Note, name='Recent_Note'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
