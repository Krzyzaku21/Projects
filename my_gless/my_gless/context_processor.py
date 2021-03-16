from auth_users.models import Register


# def register_photo(request):
#     reg_image = Register['image_add']
#     context = {
#         'reg_image': reg_image,
#     }
#     return context

from django.template import RequestContext

request_context = RequestContext(request)
# reg_image = Register['image_add']
reg_image = Register.objects.all()
request_context.push({"reg_image": reg_image})
