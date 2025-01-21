# Bot do Telegram - Guia de Configuração e Utilização

Este documento explica o passo a passo necessário para configurar e executar o bot do Telegram. 

## Pré-requisitos

Antes de começar, certifique-se de que você possui:

1. **Conta no Telegram**:
   - Você deve ter uma conta ativa no Telegram.
2. **Python Instalado**:
   - Tenha o Python 3.7 ou superior instalado em sua máquina.
3. **Bibliotecas Necessárias**:
   - Instale as bibliotecas usando o comando:
     ```bash
     pip install pyrogram tgcrypto
     ```

---

## Passo 1: Obter as Credenciais do Telegram

### Acessar o Telegram Developer Portal
1. Acesse o site [Telegram Core](https://my.telegram.org/auth).
2. Faça login com o seu número de telefone.
3. Vá até a aba **API Development Tools**.
4. Crie um novo aplicativo:
   - **App title**: Escolha um nome para o seu aplicativo.
   - **Short name**: Escolha um nome curto.
   - O site gerará o **API ID** e **API Hash**. Salve essas informações, pois serão usadas no código.

---

## Passo 2: Configurar o Código do Bot

1. Abra o arquivo de código do bot e localize as seguintes linhas para configuração:

   ```python
   api_id = "SEU_API_ID"
   api_hash = "SEU_API_HASH"
   phone_number = "+55SEU_NUMERO"  # Inclua o código do país (exemplo: +55 para Brasil)
