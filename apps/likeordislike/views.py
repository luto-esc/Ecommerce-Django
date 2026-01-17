from django.shortcuts import render
from .models import ProductLikesorDislikes

def getlikeordislike(request, pk):
	user = request.user
	user_id_lod = user.id
	likeordislike_user_id_list = ProductLikesorDislikes.objects.values_list('user_id', flat=True)

	if user_id_lod in likeordislike_user_id_list:
		lod_like = ProductLikesorDislikes.objects.filter(likes = likes)
