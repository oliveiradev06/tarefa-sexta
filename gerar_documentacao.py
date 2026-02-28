#!/usr/bin/env python3
"""
Script para gerar documentação completa do projeto em formato Word (.docx)
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import datetime

def add_code_paragraph(doc, text):
    """Adiciona um parágrafo formatado como código"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = 'Courier New'
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(51, 51, 51)
    # Adicionar fundo cinza claro ao parágrafo
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.right_indent = Inches(0.5)
    return p

def add_horizontal_line(paragraph):
    """Adiciona uma linha horizontal ao parágrafo"""
    p = paragraph._element
    pPr = p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), 'auto')
    pBdr.append(bottom)
    pPr.append(pBdr)

def create_documentation():
    """Cria o documento Word com a documentação completa do projeto"""

    doc = Document()

    # Configurar margens
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # ===== CAPA =====
    title = doc.add_heading('DOCUMENTAÇÃO DO PROJETO', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title.runs[0]
    title_run.font.color.rgb = RGBColor(0, 51, 102)

    subtitle = doc.add_heading('Sistema de Autenticação Fullstack', level=2)
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle_run = subtitle.runs[0]
    subtitle_run.font.color.rgb = RGBColor(51, 102, 153)

    doc.add_paragraph()

    # Informações do projeto
    info_table = doc.add_table(rows=5, cols=2)
    info_table.style = 'Light Grid Accent 1'

    info_data = [
        ('Projeto:', 'Fullstack Auth (Docker + Clean Architecture)'),
        ('Versão:', '1.0.0'),
        ('Data:', datetime.now().strftime('%d/%m/%Y')),
        ('Tecnologias:', 'React, Node.js, Express, MySQL, Docker'),
        ('Arquitetura:', 'Clean Architecture (Uncle Bob)')
    ]

    for i, (key, value) in enumerate(info_data):
        info_table.rows[i].cells[0].text = key
        info_table.rows[i].cells[1].text = value
        # Negrito na primeira coluna
        info_table.rows[i].cells[0].paragraphs[0].runs[0].font.bold = True

    doc.add_page_break()

    # ===== SUMÁRIO =====
    doc.add_heading('SUMÁRIO', level=1)
    toc_items = [
        '1. Visão Geral do Projeto',
        '2. Arquitetura do Sistema',
        '3. Tecnologias Utilizadas',
        '4. Requisitos do Sistema',
        '5. Funcionalidades Implementadas',
        '6. Estrutura do Projeto',
        '7. Endpoints da API',
        '8. Como Executar',
        '9. Kanban da Equipe',
        '10. Documento de Requisitos - Login'
    ]

    for item in toc_items:
        p = doc.add_paragraph(item, style='List Number')
        p.paragraph_format.left_indent = Inches(0.5)

    doc.add_page_break()

    # ===== 1. VISÃO GERAL =====
    doc.add_heading('1. VISÃO GERAL DO PROJETO', level=1)

    doc.add_heading('1.1. Descrição', level=2)
    p = doc.add_paragraph(
        'Este projeto é uma aplicação fullstack completa de autenticação de usuários, '
        'desenvolvida seguindo os princípios de Clean Architecture propostos por Robert C. Martin (Uncle Bob). '
        'A aplicação permite que usuários se registrem, façam login e acessem recursos protegidos através '
        'de autenticação JWT (JSON Web Tokens).'
    )

    doc.add_heading('1.2. Objetivos', level=2)
    objectives = [
        'Implementar sistema de autenticação seguro e robusto',
        'Aplicar princípios de Clean Architecture para manutenibilidade',
        'Utilizar containerização com Docker para facilitar deploy',
        'Separar responsabilidades em camadas bem definidas',
        'Garantir segurança através de criptografia e tokens JWT'
    ]
    for obj in objectives:
        doc.add_paragraph(obj, style='List Bullet')

    doc.add_page_break()

    # ===== 2. ARQUITETURA =====
    doc.add_heading('2. ARQUITETURA DO SISTEMA', level=1)

    doc.add_heading('2.1. Clean Architecture', level=2)
    p = doc.add_paragraph(
        'O backend foi desenvolvido seguindo os princípios de Clean Architecture, '
        'organizando o código em camadas concêntricas com dependências apontando '
        'para o centro (regras de negócio).'
    )

    doc.add_heading('2.2. Camadas do Backend', level=2)

    layers = [
        ('Domain (Domínio)', 'Contém as entidades e regras de negócio centrais. Define erros de domínio e '
         'interfaces que serão implementadas pelas camadas externas.'),
        ('Application (Aplicação)', 'Casos de uso da aplicação (registerUser, loginUser, getMe). '
         'Orquestra o fluxo de dados entre camadas sem conhecer detalhes de implementação.'),
        ('Infrastructure (Infraestrutura)', 'Implementações concretas: repositório Prisma para banco de dados, '
         'providers para JWT e hashing de senhas.'),
        ('Interfaces', 'Camada de apresentação: controllers HTTP, middlewares, rotas Express. '
         'Adaptadores que convertem requisições HTTP em chamadas de casos de uso.')
    ]

    for layer_name, layer_desc in layers:
        doc.add_heading(layer_name, level=3)
        doc.add_paragraph(layer_desc)

    doc.add_heading('2.3. Injeção de Dependências', level=2)
    p = doc.add_paragraph(
        'O arquivo container.js é responsável pela composição e injeção de dependências, '
        'garantindo que as camadas internas não dependam de detalhes de implementação.'
    )

    doc.add_page_break()

    # ===== 3. TECNOLOGIAS =====
    doc.add_heading('3. TECNOLOGIAS UTILIZADAS', level=1)

    doc.add_heading('3.1. Frontend', level=2)
    frontend_tech = [
        ('React 18.3.1', 'Biblioteca JavaScript para construção de interfaces'),
        ('Vite 5.4.11', 'Build tool moderna e rápida'),
        ('TailwindCSS 3.4.17', 'Framework CSS utility-first'),
        ('PostCSS 8.4.49', 'Processador CSS'),
        ('Autoprefixer 10.4.20', 'Plugin PostCSS para prefixos de navegadores')
    ]

    table = doc.add_table(rows=len(frontend_tech) + 1, cols=2)
    table.style = 'Light Grid Accent 1'
    table.rows[0].cells[0].text = 'Tecnologia'
    table.rows[0].cells[1].text = 'Descrição'

    for i, (tech, desc) in enumerate(frontend_tech, 1):
        table.rows[i].cells[0].text = tech
        table.rows[i].cells[1].text = desc
        table.rows[i].cells[0].paragraphs[0].runs[0].font.bold = True

    doc.add_paragraph()

    doc.add_heading('3.2. Backend', level=2)
    backend_tech = [
        ('Node.js', 'Runtime JavaScript do lado servidor'),
        ('Express 4.21.2', 'Framework web minimalista'),
        ('Prisma 6.4.1', 'ORM moderno para Node.js'),
        ('MySQL', 'Sistema de gerenciamento de banco de dados'),
        ('JWT (jsonwebtoken 9.0.2)', 'Autenticação baseada em tokens'),
        ('bcryptjs 2.4.3', 'Criptografia de senhas'),
        ('cors 2.8.5', 'Middleware para Cross-Origin Resource Sharing'),
        ('cookie-parser 1.4.7', 'Parser de cookies'),
        ('dotenv 16.4.7', 'Carregamento de variáveis de ambiente'),
        ('nodemon 3.1.9', 'Monitor de desenvolvimento com hot-reload')
    ]

    table = doc.add_table(rows=len(backend_tech) + 1, cols=2)
    table.style = 'Light Grid Accent 1'
    table.rows[0].cells[0].text = 'Tecnologia'
    table.rows[0].cells[1].text = 'Descrição'

    for i, (tech, desc) in enumerate(backend_tech, 1):
        table.rows[i].cells[0].text = tech
        table.rows[i].cells[1].text = desc
        table.rows[i].cells[0].paragraphs[0].runs[0].font.bold = True

    doc.add_paragraph()

    doc.add_heading('3.3. DevOps', level=2)
    devops_items = [
        'Docker - Containerização da aplicação',
        'Docker Compose - Orquestração de múltiplos containers'
    ]
    for item in devops_items:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_page_break()

    # ===== 4. REQUISITOS =====
    doc.add_heading('4. REQUISITOS DO SISTEMA', level=1)

    doc.add_heading('4.1. Pré-requisitos', level=2)
    prereq = [
        'Docker (versão 20.10 ou superior)',
        'Docker Compose (versão 1.29 ou superior)',
        'Node.js 18+ (para desenvolvimento local sem Docker)',
        'npm ou yarn (para desenvolvimento local sem Docker)'
    ]
    for item in prereq:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading('4.2. Portas Utilizadas', level=2)
    ports_table = doc.add_table(rows=4, cols=2)
    ports_table.style = 'Light Grid Accent 1'
    ports_table.rows[0].cells[0].text = 'Serviço'
    ports_table.rows[0].cells[1].text = 'Porta'

    ports = [
        ('Frontend', '8080'),
        ('Backend API', '4000'),
        ('MySQL', '3307')
    ]

    for i, (service, port) in enumerate(ports, 1):
        ports_table.rows[i].cells[0].text = service
        ports_table.rows[i].cells[1].text = port
        ports_table.rows[i].cells[0].paragraphs[0].runs[0].font.bold = True

    doc.add_page_break()

    # ===== 5. FUNCIONALIDADES =====
    doc.add_heading('5. FUNCIONALIDADES IMPLEMENTADAS', level=1)

    functionalities = [
        ('Registro de Usuários (Sign Up)', [
            'Validação de formato de e-mail',
            'Senha com mínimo de 8 caracteres',
            'Criptografia de senha com bcrypt',
            'Verificação de e-mail duplicado',
            'Mensagens de erro descritivas'
        ]),
        ('Login de Usuários (Sign In)', [
            'Autenticação com e-mail e senha',
            'Geração de token JWT',
            'Armazenamento de token em cookie httpOnly',
            'Validação de credenciais',
            'Tratamento de erros de autenticação'
        ]),
        ('Autenticação JWT', [
            'Tokens com expiração configurável',
            'Middleware de autenticação',
            'Proteção de rotas privadas',
            'Refresh de tokens via cookie'
        ]),
        ('Gerenciamento de Sessão', [
            'Endpoint para obter dados do usuário autenticado (GET /api/auth/me)',
            'Logout com limpeza de cookies',
            'Validação de token em cada requisição protegida'
        ])
    ]

    for func_name, features in functionalities:
        doc.add_heading(func_name, level=2)
        for feature in features:
            doc.add_paragraph(feature, style='List Bullet')

    doc.add_page_break()

    # ===== 6. ESTRUTURA =====
    doc.add_heading('6. ESTRUTURA DO PROJETO', level=1)

    doc.add_heading('6.1. Estrutura Geral', level=2)
    add_code_paragraph(doc, '''tarefa-sexta/
├── frontend/           # Aplicação React
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
├── backend/            # API Node.js
│   ├── src/
│   ├── prisma/
│   ├── package.json
│   └── .env.example
├── docker-compose.yml  # Orquestração de containers
├── README.md
└── requisitos/         # Documentação de requisitos''')

    doc.add_heading('6.2. Estrutura do Backend (Clean Architecture)', level=2)
    add_code_paragraph(doc, '''backend/src/
├── domain/              # Camada de Domínio
│   ├── entities/       # Entidades de negócio
│   ├── errors/         # Erros de domínio
│   └── repositories/   # Interfaces de repositórios
├── application/         # Camada de Aplicação
│   └── use-cases/      # Casos de uso
│       ├── registerUser.js
│       ├── loginUser.js
│       └── getMe.js
├── infrastructure/      # Camada de Infraestrutura
│   ├── database/       # Implementação Prisma
│   └── providers/      # JWT, Hash providers
├── interfaces/          # Camada de Interface
│   ├── http/
│   ├── controllers/    # Controllers HTTP
│   └── middlewares/    # Middlewares Express
├── routes/             # Definição de rotas
├── config/             # Configurações
├── container.js        # Injeção de dependências
└── server.js           # Entry point''')

    doc.add_page_break()

    # ===== 7. ENDPOINTS =====
    doc.add_heading('7. ENDPOINTS DA API', level=1)

    p = doc.add_paragraph('Base URL: ')
    run = p.add_run('http://localhost:4000/api/auth')
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 102, 204)

    doc.add_paragraph()

    endpoints = [
        {
            'method': 'POST',
            'path': '/register',
            'description': 'Registra um novo usuário',
            'body': '{\n  "email": "user@example.com",\n  "password": "senha123"\n}',
            'response': '{\n  "success": true,\n  "user": {\n    "id": 1,\n    "email": "user@example.com"\n  }\n}'
        },
        {
            'method': 'POST',
            'path': '/login',
            'description': 'Autentica um usuário existente',
            'body': '{\n  "email": "user@example.com",\n  "password": "senha123"\n}',
            'response': '{\n  "success": true,\n  "user": {\n    "id": 1,\n    "email": "user@example.com"\n  }\n}\n(Token armazenado em cookie httpOnly)'
        },
        {
            'method': 'GET',
            'path': '/me',
            'description': 'Retorna dados do usuário autenticado (requer autenticação)',
            'body': 'N/A (Requer cookie com token JWT)',
            'response': '{\n  "success": true,\n  "user": {\n    "id": 1,\n    "email": "user@example.com"\n  }\n}'
        },
        {
            'method': 'POST',
            'path': '/logout',
            'description': 'Faz logout do usuário e limpa o cookie',
            'body': 'N/A',
            'response': '{\n  "success": true,\n  "message": "Logout realizado"\n}'
        }
    ]

    for endpoint in endpoints:
        doc.add_heading(f"{endpoint['method']} {endpoint['path']}", level=2)

        p = doc.add_paragraph()
        p.add_run('Descrição: ').font.bold = True
        p.add_run(endpoint['description'])

        if endpoint['body'] != 'N/A':
            doc.add_paragraph()
            p = doc.add_paragraph()
            p.add_run('Request Body:').font.bold = True
            add_code_paragraph(doc, endpoint['body'])

        doc.add_paragraph()
        p = doc.add_paragraph()
        p.add_run('Response:').font.bold = True
        add_code_paragraph(doc, endpoint['response'])

        doc.add_paragraph()

    doc.add_page_break()

    # ===== 8. COMO EXECUTAR =====
    doc.add_heading('8. COMO EXECUTAR', level=1)

    doc.add_heading('8.1. Executar com Docker (Recomendado)', level=2)

    p = doc.add_paragraph()
    p.add_run('1. Clone o repositório').font.bold = True
    add_code_paragraph(doc, 'git clone <url-do-repositorio>')
    add_code_paragraph(doc, 'cd tarefa-sexta')

    p = doc.add_paragraph()
    p.add_run('2. Suba todos os serviços com Docker Compose').font.bold = True
    add_code_paragraph(doc, 'docker compose up --build')

    p = doc.add_paragraph()
    p.add_run('3. Aguarde a inicialização').font.bold = True
    doc.add_paragraph(
        'As migrações do Prisma serão aplicadas automaticamente no boot do backend.'
    )

    p = doc.add_paragraph()
    p.add_run('4. Acesse a aplicação').font.bold = True
    access_items = [
        'Frontend: http://localhost:8080',
        'Backend API: http://localhost:4000',
        'MySQL: localhost:3307'
    ]
    for item in access_items:
        doc.add_paragraph(item, style='List Bullet')

    p = doc.add_paragraph()
    p.add_run('5. Para parar os containers').font.bold = True
    add_code_paragraph(doc, 'docker compose down')

    p = doc.add_paragraph()
    p.add_run('6. Para parar e limpar dados do banco').font.bold = True
    add_code_paragraph(doc, 'docker compose down -v')

    doc.add_heading('8.2. Executar sem Docker (Desenvolvimento Local)', level=2)

    p = doc.add_paragraph()
    p.add_run('Backend:').font.bold = True
    backend_commands = [
        'cd backend',
        'cp .env.example .env',
        'npm install',
        'npm run prisma:generate',
        'npm run prisma:migrate',
        'npm run dev'
    ]
    for cmd in backend_commands:
        add_code_paragraph(doc, cmd)

    doc.add_paragraph()

    p = doc.add_paragraph()
    p.add_run('Frontend:').font.bold = True
    frontend_commands = [
        'cd frontend',
        'cp .env.example .env',
        'npm install',
        'npm run dev'
    ]
    for cmd in frontend_commands:
        add_code_paragraph(doc, cmd)

    doc.add_page_break()

    # ===== 9. KANBAN =====
    doc.add_heading('9. KANBAN DA EQUIPE - TELA DE LOGIN', level=1)

    kanban_sections = [
        ('📌 Backlog', [
            'Criar layout da tela de login',
            'Definir regras de negócio',
            'Implementar validação de e-mail',
            'Implementar criptografia de senha',
            'Criar recuperação de senha'
        ]),
        ('🚧 Em Andamento', [
            'Desenvolvimento do formulário de login'
        ]),
        ('🔍 Em Validação', [
            'Testes de autenticação',
            'Validação do bloqueio após 5 tentativas'
        ]),
        ('✅ Concluído', [
            'Levantamento de requisitos',
            'História do usuário definida'
        ])
    ]

    for section_name, items in kanban_sections:
        doc.add_heading(section_name, level=2)
        for item in items:
            doc.add_paragraph(item, style='List Bullet')

    doc.add_page_break()

    # ===== 10. REQUISITOS - LOGIN =====
    doc.add_heading('10. DOCUMENTO DE REQUISITOS - TELA DE LOGIN', level=1)

    doc.add_heading('10.1. Síntese da Funcionalidade', level=2)
    doc.add_paragraph(
        'A funcionalidade de login permite que usuários autenticados acessem o sistema web com segurança.'
    )

    doc.add_heading('10.2. História do Usuário', level=2)
    user_story = doc.add_paragraph()
    user_story.add_run('Como').font.italic = True
    user_story.add_run(' usuário do sistema,\n')
    user_story.add_run('Quero').font.italic = True
    user_story.add_run(' inserir meu e-mail e senha\n')
    user_story.add_run('Para').font.italic = True
    user_story.add_run(' acessar minha conta com segurança.')

    doc.add_heading('10.3. Regras de Negócio', level=2)
    business_rules = [
        ('RN01', 'O usuário deve possuir cadastro prévio'),
        ('RN02', 'O e-mail deve estar em formato válido'),
        ('RN03', 'A senha deve conter no mínimo 8 caracteres'),
        ('RN04', 'Após 5 tentativas inválidas, a conta será bloqueada por 15 minutos'),
        ('RN05', 'As senhas devem ser armazenadas com criptografia')
    ]

    for code, rule in business_rules:
        p = doc.add_paragraph()
        p.add_run(f'{code}: ').font.bold = True
        p.add_run(rule)

    doc.add_heading('10.4. Requisitos Funcionais', level=2)
    functional_reqs = [
        ('RF01', 'O sistema deve exibir campos de e-mail e senha'),
        ('RF02', 'O sistema deve permitir inserção de credenciais'),
        ('RF03', 'O sistema deve validar os dados informados'),
        ('RF04', 'O sistema deve permitir acesso com credenciais válidas'),
        ('RF05', 'O sistema deve exibir mensagem de erro para credenciais inválidas'),
        ('RF06', 'O sistema deve permitir recuperação de senha')
    ]

    for code, req in functional_reqs:
        p = doc.add_paragraph()
        p.add_run(f'{code}: ').font.bold = True
        p.add_run(req)

    doc.add_heading('10.5. Requisitos Não Funcionais', level=2)
    non_functional_reqs = [
        ('RNF01', 'O login deve responder em até 2 segundos'),
        ('RNF02', 'O sistema deve garantir segurança dos dados'),
        ('RNF03', 'A interface deve ser responsiva'),
        ('RNF04', 'O sistema deve ter disponibilidade mínima de 99,5%')
    ]

    for code, req in non_functional_reqs:
        p = doc.add_paragraph()
        p.add_run(f'{code}: ').font.bold = True
        p.add_run(req)

    doc.add_heading('10.6. Critérios de Aceitação', level=2)
    acceptance_criteria = [
        ('CA01', 'Dado que o usuário informe dados válidos, quando clicar em entrar, então o acesso deve ser permitido'),
        ('CA02', 'Dado que o usuário informe dados inválidos, então deve aparecer mensagem de erro'),
        ('CA03', 'Dado 5 tentativas incorretas, então a conta deve ser bloqueada temporariamente'),
        ('CA04', 'Dado que o usuário clique em "Esqueci minha senha", então deve ser redirecionado para recuperação')
    ]

    for code, criterion in acceptance_criteria:
        p = doc.add_paragraph()
        p.add_run(f'{code}: ').font.bold = True
        p.add_run(criterion)

    # ===== RODAPÉ =====
    doc.add_page_break()
    footer = doc.add_paragraph()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = footer.add_run(f'Documentação gerada em {datetime.now().strftime("%d/%m/%Y às %H:%M")}')
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(128, 128, 128)

    # Salvar documento
    filename = 'Documentacao_Projeto_Fullstack_Auth.docx'
    doc.save(filename)
    print(f'✅ Documento gerado com sucesso: {filename}')
    return filename

if __name__ == '__main__':
    try:
        create_documentation()
    except Exception as e:
        print(f'❌ Erro ao gerar documento: {e}')
        import traceback
        traceback.print_exc()
