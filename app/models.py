from django.db import models


class Cat(models.Model):
    CAT_COLOR = [
        ('pr', 'Preto'),
        ('br', 'Pranco'),
        ('ci', 'Cinza'),
        ('ma', 'Marrom'),
        ('gr', 'Gengibre'),
        ('li', 'Listrado'),
        ('am', 'Amarelo'),
        ('ve', 'Vermelho'),
        ('az', 'Azul'),
        ('lar', 'Laranja'),
        ('ro', 'Rosa'),
        ('ro', 'Roxo'),
        ('ver', 'Verde'),
        ('ma', 'Malhado'),
    ]

    CAT_BREED = (
        ('si', 'Siamês'),
        ('pe', 'Persa'),
        ('mc', 'Maine Coon'),
        ('ra', 'Ragdoll'),
        ('be', 'Bengal'),
        ('ab', 'Abyssinian'),
        ('sf', 'Scottish Fold'),
        ('sp', 'Sphynx'),
        ('bs', 'British Shorthair'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    # image = models.ImageField(upload_to='img/cat')
    color = models.CharField(max_length=3, choices=CAT_COLOR)
    breed = models.CharField(max_length=2, choices=CAT_BREED)

    def __str__(self):
        return self.name
