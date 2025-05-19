import csv
from accounts.models import CustomUser

# Caminhos dos arquivos
usuarios_csv_path = 'csv/usuarios.csv'
logins_csv_path = 'csv/logins.csv'

# 1. Importar usuários (com encoding latin1 por causa dos caracteres especiais)
with open(usuarios_csv_path, newline='', encoding='latin1') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')  # usa ; como separador
    for linha in reader:
        email = linha['email'].strip().lower()
        nome = linha['nome'].strip()
        matricula = linha['matricula'].strip()
        serie = linha['serie'].strip()

        if not CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.create_user(
                email=email,
                username=email.split('@')[0],
                nome_completo=nome,
                password='temporario123',
                tipo_usuario='aluno',
                matricula=matricula,
                serie=serie,
            )
            print(f"Usuário criado: {email}")
        else:
            print(f"Usuário já existe: {email}")

# 2. Atualizar senhas reais
with open(logins_csv_path, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')  # usa ; como separador
    for linha in reader:
        email = linha['email'].strip().lower()
        senha = linha['senha'].strip()

        try:
            user = CustomUser.objects.get(email=email)
            user.set_password(senha)
            user.save()
            print(f"Senha atualizada para: {email}")
        except CustomUser.DoesNotExist:
            print(f"Usuário não encontrado para email: {email}")
