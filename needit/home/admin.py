from django.contrib import admin
from home.models import Post, Friend, AllMsg

class PostAdmin(admin.ModelAdmin):
	def post_info(self, obj):
		return obj.post

	post_info.short_description = 'Content'
	
admin.site.register(Post, PostAdmin)
admin.site.register(Friend)
admin.site.register(AllMsg)