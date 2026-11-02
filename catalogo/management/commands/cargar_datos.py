from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from catalogo.models import Categoria, LugarPatrimonial


class Command(BaseCommand):
    help = 'Carga datos de prueba y crea el grupo "Gestores" con permisos'

    def handle(self, *args, **options):
        # 1. Categorías
        edificios, _ = Categoria.objects.get_or_create(
            nombre='Edificios históricos',
            defaults={'descripcion': 'Construcciones de valor histórico y arquitectónico.'})
        monumentos, _ = Categoria.objects.get_or_create(
            nombre='Monumentos',
            defaults={'descripcion': 'Obras conmemorativas en espacios públicos.'})
        murales, _ = Categoria.objects.get_or_create(
            nombre='Murales',
            defaults={'descripcion': 'Arte mural de valor patrimonial.'})

        # 2. Lugares (nombre, descripción, ubicación, año, semilla de imagen, categoría)
        lugares = [
            ('Palacio de La Moneda', 'Sede de la Presidencia de la República.',
             'Santiago', 1805, 'moneda', edificios),
            ('Teatro Municipal de Santiago', 'Principal teatro de ópera y ballet del país.',
             'Santiago', 1857, 'teatro', edificios),
            ('Ascensor Concepción', 'Uno de los funiculares históricos de Valparaíso.',
             'Valparaíso', 1883, 'concepcion', edificios),
            ('Monumento a los Héroes de Iquique', 'Homenaje a los caídos en el Combate Naval de Iquique.',
             'Valparaíso', 1886, 'heroes', monumentos),
            ('Mural Presencia de América Latina', 'Mural de gran formato en la Universidad de Concepción.',
             'Concepción', 1965, 'mural', murales),
        ]
        for nombre, descripcion, ubicacion, anio, semilla, categoria in lugares:
            LugarPatrimonial.objects.get_or_create(
                nombre=nombre,
                defaults={
                    'descripcion': descripcion,
                    'ubicacion': ubicacion,
                    'anio_construccion': anio,
                    'imagen': f'https://picsum.photos/seed/{semilla}/600/400',
                    'categoria': categoria,
                })

        # 3. Grupo "Gestores" con permisos de agregar y editar lugares
        grupo, _ = Group.objects.get_or_create(name='Gestores')
        permisos = Permission.objects.filter(
            content_type__app_label='catalogo',
            codename__in=['add_lugarpatrimonial', 'change_lugarpatrimonial'])
        grupo.permissions.set(permisos)

        self.stdout.write(self.style.SUCCESS('Datos y grupo "Gestores" listos.'))