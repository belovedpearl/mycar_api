from django.db import models
from django.contrib.auth.models import User

CAR_BODYTYPES = (
    ("Hatchbacks", "Hatchbacks"),
    ("Convertible", "Convertible"),
    ("SUV", "SUV"),
    ("Electric", "Electric"),
    ("Sports car", "Sports car"),
    ("Hybrid", "Hybrid"),
    ("Vintage", "Vintage"),
    ("Muscle", "Muscle"),
    ("Limousine", "Limousine"),
    ("Others", "Others"),
)

class Post(models.Model):
    """
    Define the model post
    No default image set as user has to provide an image to male a post
    Orders posts in descending order of creation
    Returns post id, make and model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    body_types = models.CharField(
        max_length=50, choices= CAR_BODYTYPES, default="Hatchbacks"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.make} {self.model}'

