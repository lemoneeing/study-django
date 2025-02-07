from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    """Snippet Serializer """
    owner = serializers.ReadOnlyField(source='owner.username')
    # ReadOnlyField 를 사용하면 직렬화됮 표현에서는 owner 가 사용되지만 역직력화 형태(ex. Snippet 객체의 update) 에서는 사용되지 않음.
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        
        instance.save()
        
        return instance


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all()) 
    # 역참조 관계인 Snippet 을 User의 직렬화 필드에 포함 하기 위해 명시적으로 선언(안하면 User 직렬화에서 snippet 은 빠지게 됨.)
    # PrimaryKeyRelatedField 를 사용하면 직력화 후 snippets 을 Snippet 객체의 pk 로 표현한다.

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']