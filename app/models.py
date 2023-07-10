from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Subscribe(models.Model):
    email = models.EmailField(max_length=60)
    date = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=2200, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)  # modifica el metodo save() y agrega funcionalidad

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    tags = models.ManyToManyField(Tag, blank=True, related_name='post')
    view_count = models.IntegerField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Comments(models.Model):
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    course = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    """Campo que referencia a otro comentario del mismo modelo. Es utilizado para
    representar una respuesta a otro comentario (comentario "padre"). Si se elimina
    el comentario padre, no se toma ninguna acción automáticamente (DO_NOTHING).
    Este campo puede ser nulo en la base de datos y en formularios, lo que significa
    que un comentario puede ser creado sin necesariamente ser una respuesta a otro."""
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='replies')