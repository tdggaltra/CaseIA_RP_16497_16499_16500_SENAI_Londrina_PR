# users/management/commands/create_default_user.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Cria o usuário padrão para testes'

    def handle(self, *args, **options):
        if not User.objects.filter(email='admin@admin.com').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password='Senai@2025',
                first_name='Administrador',
                last_name='Sistema'
            )
            self.stdout.write(self.style.SUCCESS('Usuário padrão criado com sucesso!'))
        else:
            self.stdout.write(self.style.WARNING('Usuário padrão já existe.'))