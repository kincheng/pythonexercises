from django.shortcuts import render

posts = [
	{
		'author' : 'CoreyMS',
		'title' : 'blog post 1',
		'content' : 'first post content',
		'date_posted' : 'August 27th, 2018'
	},
	{
		'author' : 'Kin C',
		'title' : 'blog post 2',
		'content' : 'second post content',
		'date_posted' : 'August 28th, 2018'
	}
]

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : "About"})