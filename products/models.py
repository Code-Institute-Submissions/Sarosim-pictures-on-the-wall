from django.db import models

# Create your models here.


class Category(models.Model):
    """Artwork (product) categories model """
    category_name = models.CharField(max_length=32, default='')
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"


class Badge(models.Model):
    """ Badges for Artists (eg. hobby, advanced, master, pro...) """
    badge_name = models.CharField(max_length=16)
    badge_logo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.badge_name


class Artist(models.Model):
    """ Model for the Artists uploading their artwork to the site """
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    artist_name = models.CharField(max_length=16)
    # artis_name is the display name for the artists, named in this format to match other filter name structures
    avatar = models.ImageField(upload_to='images')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    address = models.CharField(max_length=64, default='')
    wants_marketing = models.BooleanField(default=True)
    wants_newsletter = models.BooleanField(default=True)

    def __str__(self):
        return self.artist_name


class Technology(models.Model):
    """ Model for valiable printing technologies. Each artwork is assigned to all relevant print technologies"""
    technology_name = models.CharField(max_length=32)
    technology_description = models.TextField

    def __str__(self):
        return self.technology_name

    class Meta:
        verbose_name_plural = "Technologies"


class Room(models.Model):
    """ Model for assigning artwork to certain room types """
    room_name = models.CharField(max_length=16, default='')

    def __str__(self):
        return self.room_name


class Product(models.Model):
    """The Artwork (Product) model, contains all the artworks """
    title = models.CharField(max_length=32, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images', default='cube.png')
    base_repro_fee = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    room = models.ManyToManyField(Room)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default='')
    max_print_size = models.CharField(max_length=16, default='')
    available_technologies = models.ManyToManyField(Technology)
    num_of_orders = models.IntegerField(default=0)
    num_of_views = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# delete this from production version, it is just for GitPod to avoid 'Problems':
    objects = models.Manager()


class Rating(models.Model):
    """ Model for Products ratings: """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    rating = models.IntegerField()
    #userid (of the rater to prevent double rating) --- TO BE ADDED LATER


class Size(models.Model):
    """ Model for exact picture sizes in cm or inch """
    size_name = models.CharField(max_length=16, default='10 x 15 cm')
    longer_side = models.DecimalField(max_digits=6, decimal_places=2, default=15)
    shorter_side = models.DecimalField(max_digits=6, decimal_places=2, default=10)

    def __str__(self):
        return self.size_name

class Format(models.Model):
    """ Model for Picutre formats, aka aspect ratio """
    format_name = models.CharField(max_length=16, default='')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.format_name

class Hashtag(models.Model):
    """ Model for Products ratings: """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    hashtag = models.CharField(max_length=32, default='#ilovephotography')

    def __str__(self):
        return self.hashtag