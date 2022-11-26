from api.models import *

# clean table
Essay.objects.filter().delete()
Question.objects.filter().delete()
Answer.objects.filter().delete()
# Users.objects.filter().delete()