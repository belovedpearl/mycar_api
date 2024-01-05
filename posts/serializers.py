from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer used for the model Post.
    Includes fields for the post information such as owner, owner's profile details,
    and a method field to check if the user is the post owner.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source = 'owner.profile.id')
    location = serializers.ReadOnlyField(source = 'owner.profile.location')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
 
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = '__all__'
   
        # fields = [
        # 'id', 'owner', 'is_owner', 'profile_id',
        #  'profile_image', 'make', 'model',
        #   'year', 'description', 'image',
        # ]
