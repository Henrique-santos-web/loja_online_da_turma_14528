### 🎯 Desafios e Melhorias Futuras

Se você já terminou a versão base do projeto, aqui estão algumas missões para elevar o nível do seu código! Marque os itens conforme for completando:

#### Nível 1: Melhorias na Experiência do Usuário (UX no Terminal)
- [ ] **Limpar o Terminal:** Importe a biblioteca `os` e crie uma função para limpar a tela a cada nova opção escolhida (`os.system('cls' if os.name == 'nt' else 'clear')`).
- [ ] **Pausa para Leitura:** Adicione um `input("\nPressione ENTER para continuar...")` ou use a biblioteca `time` (`time.sleep(2)`) para dar tempo ao usuário de ler as mensagens.
- [ ] **Validações Robustas (Tratamento de Exceções):** Adicione blocos `try/except` e loops `while` para forçar o usuário a digitar o valor correto ao inserir dados numéricos.

#### Nível 2: Limpeza e Organização de Código (Refatoração)
- [ ] **Separar a Lógica do `main()`:** Crie funções separadas para cada ação (ex: `def cadastrar_roupa(carrinho):`) para deixar o código mais limpo e profissional.
- [ ] **Tratamento de Strings:** Melhore a busca utilizando métodos de string como `.strip()` e `.lower()` para que "Camiseta" e " camiseta " sejam reconhecidos como o mesmo produto.

#### Nível 3: Novas Regras de Negócio (Evoluindo o E-commerce)
- [ ] **Novas Categorias de Produtos:** Crie novas classes que herdem de `Produto` (ex: `Alimento`, `Livro`), adicione atributos exclusivos e sobrescreva o método de exibir detalhes usando Polimorfismo.
- [ ] **Gerenciamento de Quantidades:** Modifique o carrinho para agrupar itens iguais e adicionar um atributo de quantidade.
- [ ] **Identificadores Únicos (IDs):** Importe a biblioteca `uuid` e gere um ID único para cada produto, atualizando o método de remoção para buscar por ID.
- [ ] **Validação no Construtor:** Lance um erro (`raise ValueError`) dentro do `__init__` para impedir a criação de produtos com preço negativo.

#### Nível 4: O "Boss" Final - Persistência de Dados
- [ ] **Salvar e Carregar em JSON:** Crie métodos utilizando a biblioteca nativa `json` para salvar o carrinho antes de fechar o programa e carregá-lo automaticamente ao iniciar.

---

### 🚀 Como executar o projeto

Certifique-se de ter o Python 3 instalado na sua máquina. Abra o terminal na pasta do projeto e execute:

```bash
python main.py
