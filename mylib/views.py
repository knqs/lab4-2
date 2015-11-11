#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mylib.models import *
import datetime,string
# Create your views here.
def index(req):
	if req.POST:
		post = req.POST
		price = string.atof(post["price"])
		isbn = post["isbn"]
		try:
			author = Author.objects.get(Name = post["author"])
		except:
			return render_to_response('addauthor.html',{"messages":"对不起，作者不存在，请先创建作者信息"})
		if len(Book.objects.filter(ISBN = isbn)) > 0:
			return render_to_response('addbook.html',{"messages":"对不起，该书的isbn已经存在"})
		try:
			author.book_set.create(Price = string.atof(post["price"]), ISBN = isbn, Title = post["title"], Publisher = post["publisher"], PublishDate = datetime.datetime.strptime(post["YYYY"]+"-"+post["MM"]+"-"+post["DD"], "%Y-%m-%d").date())
		except:
			return render_to_response('addbook.html',{"messages":"对不起，请重试"})
		return render_to_response('addbook.html',{"messages":"恭喜，书籍加入成功"})
	return render_to_response('addbook.html',{})

def addauthor(req):
	if req.POST:
		post = req.POST
		try:
			author = Author.objects.get(Name = post["name"])
			return render_to_response('addauthor.html',{"info":"作者已经存在！"})
		except:
			try:
				author1 = Author(Name = post["name"], Age = post["age"], Country = post["country"])
				author1.save()
				return render_to_response('addauthor.html',{"info":"恭喜，作者加入成功"})
			except:
				return render_to_response('addauthor.html',{"info":"Age 格式错误"})
	return render_to_response('addauthor.html')

def search(req):
	if req.POST:
		post = req.POST
		try:
			if(len(Author.objects.filter(Name = post["search"])) > 0):
				messages = Author.objects.get(Name = post["search"]).book_set.all()
				if len(messages) <= 0:
					return render_to_response("search.html",{"Tips":"作者暂无图书"}) 
				return render_to_response("search.html",{"messages":messages})
			else:
				return render_to_response("search.html",{"Tips":"该作者不存在"})
		except:
			return render_to_response("search.html",{"Tips":"出错了，请重新查找"})
	return render_to_response("search.html")
def showdetails(req ,id):
	if req.POST:
		post = req.POST
		if post["delete"] == "Delete":
			book = Book.objects.get(ISBN = id)
			book.delete()
			return render_to_response("details.html",{"info":"删除成功"})
		else:
			messages = Book.objects.get(ISBN = id)
			ISBN = messages.ISBN
			return render_to_response("modify.html",{"messages":messages,"ISBN":ISBN})
		book = Book.objects.get(ISBN = id)
		return render_to_response("details.html",{"book":book})
	book = Book.objects.get(ISBN = id)
	return render_to_response("details.html",{"book":book})
def changebook(req):
	if req.POST:
		post = req.POST
		isbn = post["isbn"]
		try:
			author = Author.objects.get(Name = post["author"])
		except:
			return render_to_response('addauthor.html',{"Tips":"对不起，作者不存在，请先创建作者信息"})
		book = Book.objects.get(ISBN = isbn)
		book.Author = post["author"]
		book.Publisher = post["publisher"]
		book.PublishDate = datetime.datetime.strptime(post["YYYY"]+"-"+post["MM"]+"-"+post["DD"], "%Y-%m-%d").date()
		book.Price = post["price"]
		book.save()
		return render_to_response('modify.html',{"Tips":"恭喜，书籍修改成功"})
	return render_to_response('modify.html',{})