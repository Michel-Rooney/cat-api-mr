from django.db import models



class Cat(models.Model):
    CAT_COLOR = [
        ('pr', 'preto'),
        ('br', 'branco'),
        ('ci', 'cinza'),
        ('ma', 'marrom'),
        ('gr', 'gengibre'),
        ('li', 'listrado'),
        ('am', 'amarelo'),
        ('ve', 'vermelho'),
        ('az', 'azul'),
        ('lar', 'laranja'),
        ('ro', 'rosa'),
        ('ro', 'roxo'),
        ('ver', 'verde'),
        ('ma', 'malhado'),
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
