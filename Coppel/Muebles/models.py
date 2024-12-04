from django.db import models


class area1(models.Model): #Modelo para agregar articulos y posterior mandar a traer mediante el ManyToMany
    articulo = models.CharField(max_length=30, blank=False)
    sku = models.IntegerField(blank=False)
    img = models.ImageField(upload_to='imagenes/', blank=True, null=True)

    def __str__(self):
        return f"{self.sku} - {self.articulo}"
    
    class Meta: 
        verbose_name_plural = "Area 1"


class area2(models.Model):
    articulo = models.CharField(max_length=30, blank=False)
    sku = models.IntegerField(blank=False)
    img = models.ImageField(upload_to='imagenes/', blank=True, null=True) # modelos para agregar imagenes mediante pillow unicamente crear carpeta imagenes en raiz del proyecto donde se alojaran las imagenes 

    def __str__(self):
        return f"{self.sku} - {self.articulo}"
    
    class Meta: 
        verbose_name_plural = "Area 2"
    

class area3(models.Model):
    articulo = models.CharField(max_length=30, blank=False)
    sku = models.IntegerField(blank=False)
    img = models.ImageField(upload_to='imagenes/', blank=True, null=True)

    def __str__(self):
        return f"{self.sku} - {self.articulo}"
    
    class Meta: 
        verbose_name_plural = "Area 3"

class area4(models.Model):
    articulo = models.CharField(max_length=30, blank=False)
    sku = models.IntegerField(blank=False)
    img = models.ImageField(upload_to='imagenes/', blank=True, null=True)

    def __str__(self):
        return f"{self.sku} - {self.articulo}"
    
    class Meta: 
        verbose_name_plural = "Area 4"

class area5(models.Model):
    articulo = models.CharField(max_length=30, blank=False)
    sku = models.IntegerField(blank=False)
    img = models.ImageField(upload_to='imagenes/', blank=True, null=True) #metodo para mandar a traer otras clases para la seleccion de inventarios 

    def __str__(self):
        return f"{self.sku} - {self.articulo}"
    
    class Meta: 
        verbose_name_plural = "Area 5"
    






class inventario1(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    colaborador = models.IntegerField(blank=False, verbose_name="Numero de colaborador")  #verbosename para modificar el nombre de mis clases o modelos 
    fecha = models.DateField()
    sku = models.ManyToManyField(area1, blank=False)

    def __str__(self):
        return f"{self.nombre} - {self.colaborador} - {self.sku}" # metodo self para dar un buen diseño a los campos agregados y modificaciones que se hagan en la plataforma 
    
    class Meta:
        verbose_name_plural = "Inventario Area 1"
        ordering = ['-fecha'] #class meta me modifica el nombre de mi clase y no agrege la "s" al final de las clases 
        


class inventario2(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    colaborador = models.IntegerField(blank=False, verbose_name="Numero de colaborador")
    fecha = models.DateField()
    sku = models.ManyToManyField(area2, blank=False)

    def __str__(self):
        return f"{self.nombre} - {self.colaborador} - {self.sku}"
    
    class Meta:
        verbose_name_plural = "Inventario Area 2"
        ordering = ['-fecha']



class inventario3(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    colaborador = models.IntegerField(blank=False, verbose_name="Numero de colaborador")
    fecha = models.DateField()
    sku = models.ManyToManyField(area3, blank=False)

    def __str__(self):
        return f"{self.nombre} - {self.colaborador} - {self.sku}"
    
    class Meta:
        verbose_name_plural = "Inventario Area 3"
        ordering = ['-fecha']



class inventario4(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    colaborador = models.IntegerField(blank=False, verbose_name="Numero de colaborador")
    fecha = models.DateField()
    sku = models.ManyToManyField(area4, blank=False)

    def __str__(self):
        return f"{self.nombre} - {self.colaborador} - {self.sku}"
    
    class Meta:
        verbose_name_plural = "Inventario Area 4"
        ordering = ['-fecha']
        


class inventario5(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    colaborador = models.IntegerField(blank=False, verbose_name="Numero de colaborador")
    fecha = models.DateField()
    sku = models.ManyToManyField(area5, blank=False)

    def __str__(self):
        return f"{self.nombre} - {self.colaborador} - {self.sku}"
    
    class Meta:
        verbose_name_plural = "Inventario Area 5"
        ordering = ['-fecha']  # Orden descendente por fecha



