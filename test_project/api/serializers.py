from .models import *
from rest_framework import serializers

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        music = Music.objects.all()
        model = Music
        fields = '__all__'


class MusicBodySerializer(serializers.Serializer):
    singer = serializers.CharField(help_text="가수명")
    title = serializers.CharField(help_text="곡 제목")
    category = serializers.ChoiceField(help_text="곡 범주", choices=('JPOP', 'POP', 'CLASSIC', 'ETC'))
    star_rating = serializers.IntegerField(help_text="1~3 이내 지정 가능. 숫자가 클수록 좋아하는 곡")


class MusicQuerySerializer(serializers.Serializer):
    title = serializers.CharField(help_text="곡 제목으로 검색", required=False)
    star_rating = serializers.ChoiceField(help_text="곡 선호도로 검색", choices=(1, 2, 3), required=False)
    singer = serializers.CharField(help_text="가수명으로 검색", required=True)
    category_1 = serializers.ChoiceField(help_text="카테고리로 검색", choices=('JPOP', 'POP', 'CLASSIC', 'ETC'), required=False)
    category_2 = serializers.ChoiceField(help_text="카테고리로 검색", choices=('JPOP', 'POP', 'CLASSIC', 'ETC'), required=False)
    category_3 = serializers.ChoiceField(help_text="카테고리로 검색", choices=('JPOP', 'POP', 'CLASSIC', 'ETC'), required=False)
    category_4 = serializers.ChoiceField(help_text="카테고리로 검색", choices=('JPOP', 'POP', 'CLASSIC', 'ETC'), required=False)
    created_at = serializers.DateTimeField(help_text="입력한 날짜를 기준으로 그 이전에 추가된 곡들을 검색", required=False)
