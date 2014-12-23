POSTBack
========

Antes de continuar, não esqueça de `checar a documentação do pagar.me <https://pagar.me/docs/advanced/#validando-a-origem-de-um-postback>`_.

Não esqueça de setar sua api_key.


=================================
Validando a origem de um POSTback
=================================

Para validar, basta passar um dicionário com os campos que foram passados via POSTback.

  >>> from pagarme.postback import PostBack
  >>> postback_data = {
  ...     'old_status': 'waiting_payment',
  ...     'event': 'transaction_status_changed',
  ...     'desired_status': 'paid',
  ...     'fingerprint': 'b4f0bc081343830fddedd61c6996dcb608df6d1c',
  ...     'object': 'transaction',
  ...     'current_status': 'paid',
  ...     'id': 173675
  ... }
  >>> postback = PostBack(postback_data)
  >>> postback.is_valid()
  True
