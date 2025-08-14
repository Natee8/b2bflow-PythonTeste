```bash
1. Clonar o repositório:

git clone https://github.com/Natee8/b2bflow-PythonTeste.git

cd BACKEND

2. Criar um ambiente virtual e instalar dependencias:

   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt

3. Configurar o `.env` (caso necessario):

SUPABASE_URL=SEU_SUPABASE_URL
SUPABASE_KEY=SEU_SUPABASE_KEY
ZAPI_INSTANCE_ID=SEU_INSTANCE_ID
ZAPI_INSTANCE_TOKEN=SEU_INSTANCE_TOKEN
ZAPI_CLIENT_TOKEN=SEU_CLIENT_TOKEN

Criar tabela Peoples no Supabase com as colunas:
name (string)
phone (string)

## Execução
python main.py


B2BFlow - Envio Automático de Mensagens

Criar um código em Python que leia pessoas cadastradas no Supabase e envie, via Z-API, a mensagem exata:
"Olá {{nome_contato}}, tudo bem com você?"

Regras do desafio
- Use Python + Supabase + Z-API (todas têm plano gratuito).
- Os contatos devem vir do banco no Supabase.
- Envie a mensagem para 3 números diferentes (ou 1, se não tiver 3).
- Personalize {{nome_contato}} com o campo salvo no banco


```
