# AWS Lambda SES Email

## Descrição

Esta função AWS Lambda envia um e-mail usando o Amazon Simple Email Service (SES). A função é escrita em Python e utiliza a biblioteca `boto3` para interagir com o SES.

## Funcionalidades da Lambda

Esta função Lambda é capaz de enviar um e-mail para um destinatário especificado usando o Amazon SES. Os detalhes do e-mail, como destinatário, assunto e corpo do e-mail, podem ser especificados no evento de entrada.

## Entrada Esperada

A função pode receber um JSON contendo os seguintes campos:
- `recipient_email`: (opcional) O e-mail do destinatário.
- `subject`: (opcional) O assunto do e-mail.
- `body_text`: (opcional) O corpo do e-mail em texto simples.
- `body_html`: (opcional) O corpo do e-mail em HTML.

Se esses campos não forem fornecidos, valores padrão serão usados.

## Saída Esperada

A função retorna um status code 200 se o e-mail for enviado com sucesso, ou 500 se houver um erro. Em caso de erro, uma mensagem descritiva é retornada.

## Dependências Externas

- `boto3`: A biblioteca oficial da AWS para Python.

## Instruções para Execução

1. **Verifique os Endereços de E-mail no SES**:
   - Verifique o endereço de e-mail do remetente e do destinatário no Amazon SES.

2. **Criar a Função Lambda**:
   - Crie uma nova função Lambda no console AWS.
   - Adicione o código fonte contido no arquivo `lambda_function.py`.
   - Configure a variável de ambiente `SENDER_EMAIL` com o e-mail verificado do remetente.
   - Configure as permissões da função para permitir o envio de e-mails usando SES.

3. **Configurar Permissões**:
   - A função Lambda precisa de permissões para enviar e-mails usando SES. Anexe uma política de IAM que permita a ação `ses:SendEmail`.

4. **Testar a Função Lambda**:
   - Use o console do AWS Lambda para configurar um evento de teste com um payload JSON.

## Testando e Depurando

### Logs do CloudWatch
A função Lambda registra logs no Amazon CloudWatch. Verifique os logs para depurar problemas.

### Eventos de Teste
Configure eventos de teste no console do Lambda para simular diferentes entradas e validar o comportamento da função.

## Exemplo de Evento de Teste

Para enviar um e-mail dinâmico, você pode usar o seguinte evento de teste:

```json
{
  "recipient_email": "matheusblasquessantos@gmail.com",
  "subject": "Test Email from AWS Lambda",
  "body_text": "This is a test email sent from an AWS Lambda function.",
  "body_html": "<html><head></head><body><h1>Test Email from AWS Lambda</h1><p>This is a test email sent from an AWS Lambda function.</p></body></html>"
}
