from models import Posts,Comment,Users
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.middleware import csrf
from django.shortcuts import render_to_response
import random


def login(request):
   username = "wellcomes"
   password = "password"
   username = request.POST.get(
                'username'
            , '')
   password  = request.POST.get(
                'password'
            , '')
   request.session['username'] = username
   request.session['password'] = password
   user = Users.objects.all()
   objects = Posts.objects.all()
   comments = Comment.objects.all()
   for c in user:
       if c.name == username and c.password == password:
           username = request.session['username']
           return render(request, 'post.html',{"username" : username,"comments" : comments,"objects" : objects})

   else:
       return render(request,'index.html')

   return render(request, 'index.html')
def loggedin(request):
    return render(request, 'login.html')
def delete(request):
    return render(request,'delete.html')
def deletepost(request):
    postid = "postid"
    postid = request.POST.get(
        'postid'
        , '')
    username = request.POST.get('username','')
    request.session['username'] = username
    request.session['postid'] = postid
    objects = Posts.objects.all()
    comments = Comment.objects.all()
    if username == "":
        return render(request, 'login.html')
    elif username == "guestuser":
        return render(request, 'login.html')

    res = 'deleting'
    for e in objects:
        if e.postid == postid:

              res += "<br> delete <br>"
              res += e.post+ "<br>"

              e.delete()
    return render(request, 'post.html',{"username" :username,"comments":comments, "objects":objects})
def post(request):
    objects = Posts.objects.all()
    comments = Comment.objects.all()
    username = request.POST.get('username','')
    request.session['username'] = username
    if username == "":
        return render(request, 'login.html')
    elif username == "guestuser":
        return render(request, 'login.html')
    return render(request,'post.html',{"objects": objects, "comments": comments})
def deletecomment(request):
    return render(request, 'view.html')

def newpost(request):

    postid = "wellcomes"
    post = "password"
    username = "usdjdh"

    postid = random.sample(xrange(1,10000000), 1)

    post = request.POST.get(
        'post'
        , '')
    username = request.POST.get(
        'username'
        , '')
    request.session['postid'] = postid
    request.session['post'] = post
    request.session['username'] = username
    if username == "":
        return render(request, 'login.html')
    elif username == "guestuser":
        return render(request, 'login.html')
    elif post != "":
     dream = Posts(
        postid=postid,
        post=post,
        username=username,
     )
     dream.save()
    objects = Posts.objects.all()
    comments = Comment.objects.all()
    return render(request, 'post.html',{"username": username, "objects": objects, "comments": comments})

def comment(request):
    postid = "wellcomes"
    commentid = "password"
    comment = "coHHJ"
    postid = request.POST.get(
        'postid'
        , '')
    commentid = random.sample(xrange(1,10000000), 1)
    comment = request.POST.get(
        'comment'
        , '')
    username = "guestuser"
    request.session['postid'] = postid
    request.session['commentid'] = commentid
    request.session['comment'] = comment
    request.session['username'] = username
    objects = Posts.objects.all()
    comments = Comment.objects.all()

    if comment !="":
     dr = Comment(
         postid = postid,
         commentid = commentid,
         comment = comment,
         username = username,
     )
     dr.save()
    return render(request, 'loggedin.html', {"objects": objects, "comments": comments})
def viewpost(request):

    objects = Posts.objects.all()
    comments = Comment.objects.all()
    res = '<br>display<br>'
    #for e in objects:
        #res += 'post id'
        #res += e.postid
        #res += e.post

        #for b in a:
         #if b.postid == e.postid:
            #res += '<br>comment id<br><b>'
            #res += b.commentid+ "</b><br> comment :<br>"
            #res += b.comment+ "<br>"



            #return HttpResponse(res)
        #return HttpResponse(res)
    return render(request,'loggedin.html',{"objects":objects,"comments":comments})


def viewcomment(request):
        objects = Posts.objects.all()
        comments = Comment.objects.all()
        users = Users.objects.all()


        postid = request.POST.get(
            'postid'
            , '')

        username = request.POST.get(
            'username'
            , '')
        commentid = request.POST.get(
            'commentid'
            , '')
        request.session['postid'] = postid
        request.session['commentid'] = commentid
        request.session['username'] = username
        if username == "":
            return render(request,'login.html')
        elif username == "guestuser":
            return render(request, 'login.html')
        for e in comments:
            res = '<br>displaying comment<br>'



            if e.postid == postid:
                if e.commentid == commentid:
                  res += "<br> delete <br>"
                  res += e.comment+ "<br>"
                  e.delete()

        return render(request, 'post.html', {"username" : username,"objects": objects, "comments": comments})
def view(request):

    objects = Posts.objects.all()
    comments = Comment.objects.all()
    res = '<br>display<br>'
    #for e in objects:
        #res += 'post id'
        #res += e.postid
        #res += e.post

        #for b in a:
         #if b.postid == e.postid:
            #res += '<br>comment id<br><b>'
            #res += b.commentid+ "</b><br> comment :<br>"
            #res += b.comment+ "<br>"



            #return HttpResponse(res)
        #return HttpResponse(res)
    return render(request,'delete.html',{"objects":objects,"comments":comments})
def display(request):

    objects = Posts.objects.all()
    comments = Comment.objects.all()

    res = '<br>display<br>'
    #for e in objects:
        #res += 'post id'
        #res += e.postid
        #res += e.post

        #for b in a:
         #if b.postid == e.postid:
            #res += '<br>comment id<br><b>'
            #res += b.commentid+ "</b><br> comment :<br>"
            #res += b.comment+ "<br>"



            #return HttpResponse(res)
        #return HttpResponse(res)
    return render(request,'view.html',{"objects":objects,"comments":comments})
def commentpost(request):
    postid = "wellcomes"
    commentid = "password"
    comment = "coHHJ"
    postid = request.POST.get(
        'postid'
        , '')
    commentid = random.sample(xrange(1,10000000), 1)
    comment = request.POST.get(
        'comment'
        , '')
    username = request.POST.get(
        'username'
        , '')

    request.session['postid'] = postid
    request.session['commentid'] = commentid
    request.session['comment'] = comment
    request.session['username'] = username
    objects = Posts.objects.all()
    comments = Comment.objects.all()
    if username == "":
        return render(request, 'login.html')
    elif username == "guestuser":
        return render(request, 'login.html')
    elif comment !="":
     dr = Comment(
         postid = postid,
         commentid = commentid,
         comment = comment,
         username = username,
     )
     dr.save()
    return render(request, 'post.html', {"username" : username, "objects": objects, "comments": comments})
def register(request):
    name = "wellcomes"
    commentid = "password"
    comment = "coHHJ"
    name = request.POST.get(
        'name'
        , '')
    email = request.POST.get(
        'email'
        , '')
    password = request.POST.get(
        'password'
        , '')

    request.session['name'] = name
    request.session['email'] = email
    request.session['password'] = password
    objects = Posts.objects.all()
    comments = Comment.objects.all()
    user = Users.objects.all()
    for c in user:
        if c.name == name or c.email == email:
            return render(request, 'register.html')

    else:

            dr = Users(
                name=name,
                email=email,
                password=password,

            )
            dr.save()
            return render(request, 'login.html')
def account(request):
    return render(request,'register.html')
def logout(request):
    del request.session['username']
    return render(request,'login.html')