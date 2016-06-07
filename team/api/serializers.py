from rest_framework import serializers
from ..models import Kid



class KidSerializer(serializers.ModelSerializer):
	class Meta:
		model = Kid
		fields = ('team','name','last_name','slug')

