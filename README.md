# API da Clínica

Esta API foi desenvolvida para permitir o acesso à disponibilidade dos profissionais de saúde de uma clínica. Os usuários podem consultar especialidades médicas e obter informações sobre os profissionais de saúde, incluindo seus nomes e disponibilidades.

## Funcionalidades

- **Listar Especialidades**: Retorna todas as especialidades médicas disponíveis.
- **Listar Profissionais**: Permite consultar profissionais por especialidade e/ou nome.

## Pré-requisitos

Antes de iniciar, certifique-se de que o Python está instalado em seu sistema. Python pode ser baixado aqui: [Python Downloads](https://www.python.org/downloads/)

## Configuração

Para configurar o ambiente necessário para rodar a aplicação, siga os passos abaixo:

### Clonando o Repositório

Primeiro, clone o repositório para o seu computador local usando o comando:

```bash
git clone https://github.com/gususa/API_CLINICA
cd API_CLINICA
```

### Configurando o Ambiente Virtual

Crie um ambiente virtual para gerenciar as dependências:

```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Unix ou MacOS
source venv/bin/activate
```

### Instalando Dependências

Instale todas as dependências necessárias com o seguinte comando:

```bash
pip install -r requirements.txt
```

## Executando a Aplicação

Para iniciar a aplicação, execute o seguinte comando no diretório do projeto:

```bash
python app.py
```

A aplicação estará acessível via navegador ou cliente API no endereço: `http://localhost:5000/`

## Uso da API

### Acessando as Especialidades

Você pode listar todas as especialidades disponíveis acessando:

```
GET http://localhost:5000/especialidades
```

### Acessando os Profissionais

Para listar profissionais, com a possibilidade de filtrar por especialidade ou nome, use:

```
GET http://localhost:5000/profissionais?especialidade=Cardiologia&nome=Ricardo
```

## Suporte

Para obter suporte, entre em contato com [austgus@gmail.com].
```
