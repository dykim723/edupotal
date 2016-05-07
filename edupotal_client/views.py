from django.shortcuts import render

def post_list(request):
	return render(request, 'edupotal_client/post_list.html', {})
