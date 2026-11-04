from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from catalogo.models import Categoria, LugarPatrimonial


class Command(BaseCommand):

    def handle(self, *args, **options):
        edificios, _ = Categoria.objects.get_or_create(
            nombre='Edificios históricos',
            defaults={'descripcion': 'Construcciones de valor histórico y arquitectónico.'})
        monumentos, _ = Categoria.objects.get_or_create(
            nombre='Monumentos',
            defaults={'descripcion': 'Obras conmemorativas en espacios públicos.'})
        murales, _ = Categoria.objects.get_or_create(
            nombre='Murales',
            defaults={'descripcion': 'Arte mural de valor patrimonial.'})

        lugares = [
            ('Palacio de La Moneda', 'Sede de la Presidencia de la República.',
             'Santiago', 1805, 'https://www.monumentos.gob.cl/sites/default/files/styles/16x9_grande/public/image-monumentos/mh_00027_2017_av_009.jpg?h=920929c4&itok=xNOHTyVR', edificios),
            ('Teatro Municipal de Santiago', 'Principal teatro de ópera y ballet del país.',
             'Santiago', 1857, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU4XpSyATzujQGkfn1UfCeNyoz1PjIVzzUOrkyTEjPdQ&s=10', edificios),
            ('Ascensor Concepción', 'Uno de los funiculares históricos de Valparaíso.',
             'Valparaíso', 1883, 'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/74/Ascensor_2.JPG/1280px-Ascensor_2.JPG?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail', edificios),
            ('Monumento a los Héroes de Iquique', 'Homenaje a los caídos en el Combate Naval de Iquique.',
             'Valparaíso', 1886, 'https://upload.wikimedia.org/wikipedia/commons/6/6b/Monumento_a_los_H%C3%A9roes_de_Iquique_%28Plaza_Sotomayor%29.jpg?utm_source=es.wikipedia.org&utm_campaign=index&utm_content=original', monumentos),
            ('Mural Presencia de América Latina', 'Mural de gran formato en la Universidad de Concepción.',
             'Concepción', 1965, 'https://noticias.udec.cl/wp-content/uploads/2021/09/mural2-1024x557.png', murales),
        ]
        for nombre, descripcion, ubicacion, anio, imagen, categoria in lugares:
            LugarPatrimonial.objects.update_or_create(
                nombre=nombre,
                defaults={
                    'descripcion': descripcion,
                    'ubicacion': ubicacion,
                    'anio_construccion': anio,
                    'imagen': imagen ,
                    'categoria': categoria,
                })

        grupo, _ = Group.objects.get_or_create(name='Gestores')
        permisos = Permission.objects.filter(
            content_type__app_label='catalogo',
            codename__in=['add_lugarpatrimonial', 'change_lugarpatrimonial'])
        grupo.permissions.set(permisos)

        self.stdout.write(self.style.SUCCESS('Datos y grupo "Gestores" listos.'))