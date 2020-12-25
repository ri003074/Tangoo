from rest_framework import serializers
from .models import Tangoo


class TangooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tangoo
        fields = ('id', 'phrase_en', 'phrase_ja', 'word_en', 
                  's_counter', 'c_counter', 'supplement')