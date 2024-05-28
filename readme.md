<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciador de Software</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2 {
            color: #333;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            padding: 5px 0;
        }
    </style>
</head>
<body>
    <h1>Gerenciador de Software</h1>

    <p>Bem-vindo ao repositório do Gerenciador de Software! Este projeto é uma aplicação destinada a auxiliar na organização e gestão de softwares instalados em seu sistema.</p>

    <h2>Índice</h2>
    <ul>
        <li><a href="#descrição">Descrição</a></li>
        <li><a href="#funcionalidades">Funcionalidades</a></li>
        <li><a href="#pré-requisitos">Pré-requisitos</a></li>
        <li><a href="#instalação">Instalação</a></li>
        <li><a href="#como-usar">Como usar</a></li>
        <li><a href="#contribuição">Contribuição</a></li>
        <li><a href="#licença">Licença</a></li>
        <li><a href="#contato">Contato</a></li>
    </ul>

    <h2 id="descrição">Descrição</h2>
    <p>O Gerenciador de Software é uma ferramenta que permite aos usuários visualizar, organizar e gerenciar os softwares instalados em seus computadores de forma eficiente. Com uma interface intuitiva, ele facilita a identificação e controle dos programas, oferecendo uma melhor experiência de gestão.</p>

    <h2 id="funcionalidades">Funcionalidades</h2>
    <ul>
        <li>Listar todos os softwares instalados</li>
        <li>Pesquisar softwares por nome</li>
        <li>Adicionar novos softwares manualmente</li>
        <li>Remover softwares</li>
        <li>Atualizar informações dos softwares</li>
        <li>Exportar lista de softwares para arquivo</li>
    </ul>

    <h2 id="pré-requisitos">Pré-requisitos</h2>
    <p>Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:</p>
    <ul>
        <li><a href="https://www.python.org/downloads/" target="_blank">Python 3</a></li>
        <li><a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a></li>
    </ul>
    <p>Além disso, é recomendável o uso de um ambiente virtual para a instalação das dependências do projeto.</p>

    <h2 id="instalação">Instalação</h2>
    <p>Siga os passos abaixo para instalar e configurar o projeto em sua máquina:</p>
    <pre>
        <code>
1. Clone este repositório:
    git clone https://github.com/Cutieri/Gerenciador-de-Software.git

2. Navegue até o diretório do projeto:
    cd Gerenciador-de-Software

3. Crie um ambiente virtual:
    python -m venv venv

4. Ative o ambiente virtual:
    - No Windows:
      venv\Scripts\activate
    - No Linux/Mac:
      source venv/bin/activate

5. Instale as dependências:
    pip install -r requirements.txt
        </code>
    </pre>

    <h2 id="como-usar">Como usar</h2>
    <p>Após a instalação, você pode iniciar a aplicação com o seguinte comando:</p>
    <pre><code>python main.py</code></pre>
    <p>A interface do Gerenciador de Software será exibida, permitindo que você comece a gerenciar seus softwares imediatamente.</p>

    <h2 id="contribuição">Contribuição</h2>
    <p>Contribuições são sempre bem-vindas! Se você tem sugestões de melhorias, novas funcionalidades ou correções de bugs, por favor, siga os passos abaixo:</p>
    <pre>
        <code>
1. Faça um fork deste repositório.
2. Crie uma branch para sua feature ou correção de bug (git checkout -b feature/nome-da-feature).
3. Commit suas alterações (git commit -m 'Adiciona nova feature').
4. Faça o push para a branch (git push origin feature/nome-da-feature).
5. Abra um Pull Request.
        </code>
    </pre>

    <h2 id="licença">Licença</h2>
    <p>Este projeto está licenciado sob a licença MIT - veja o arquivo <a href="LICENSE" target="_blank">LICENSE</a> para mais detalhes.</p>

    <h2 id="contato">Contato</h2>
    <p>Em caso de dúvidas, sugestões ou problemas, sinta-se à vontade para entrar em contato:</p>
    <ul>
        <li>GitHub: <a href="https://github.com/Cutieri" target="_blank">Cutieri</a></li>
        <li>Email: <a href="mailto:seu-email@exemplo.com">seu-email@exemplo.com</a></li>
    </ul>
</body>
</html>
