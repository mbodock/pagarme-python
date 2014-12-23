Transações
==========

Antes de continuar, não esqueça de `checar a documentação do pagar.me <https://pagar.me/docs/transactions/>`_.

Não esqueça de setar sua api_key.

=========================
Criando dados de Metadata
=========================

Você pode enviar dados adicionais para a futura transação usando o metadata.

  >>> from pagarme.metadata import MetaData
  >>> metadata = MetaData(order_id=1, user_id=1)

=========================
Criando dados do Customer
=========================

É interessante que você envie os dados do cliente ao realizar a transação.

Se você estiver com o antifraude ligado, esses dados são obrigatórios.

  >>> from pagarme.customer import Customer
  >>> customer = Customer(
  ...     name='John Appleseed',
  ...     document_number='92545278157',
  ...     email='jappleseed@apple.com',
  ...     address_street='Av. Brigadeiro Faria Lima',
  ...     address_neighborhood='Jardim Paulistano',
  ...     address_zipcode='01452000',
  ...     address_street_number='2941',
  ...     address_complementary='8º andar',
  ...     phone_ddd='11',
  ...     phone_number='30713261'
  ... )


==============================================
Criando uma transação usando cartão de crédito
==============================================

Para realizar transações com cartão, você deve `capturar os dados do cartão <https://pagar.me/docs/capturing-card-data/>`_ ou `usar um card_id <https://pagar.me/docs/cards/#storing-a-card>`_.

  >>> from pagarme.transaction import Transaction
  >>> card_hash = 'card_hash'
  >>> transaction = Transaction(
  ...     amount='10000',
  ...     card_hash=card_hash,
  ...     customer=customer,
  ...     metadata=metadata,
  ...     postback_url='http://requestb.in/18j98r31',
  ...     soft_descriptor='Pagamento 1'
  ... )
  >>> transaction.charge()
  >>> transaction.data
  {u'date_updated': u'2014-12-23T20:05:02.000Z', u'ip': u'179.179.108.26', u'boleto_barcode': None, u'cost': 0, u'refuse_reason': None, u'id': 173714, u'card_holder_name': u'Jose da Silva', u'postback_url': u'http://requestb.in/18j98r31', u'boleto_expiration_date': None, u'nsu': None, u'payment_method': u'credit_card', u'card_brand': u'visa', u'tid': None, u'card_last_digits': u'4448', u'metadata': {u'order_id': u'1', u'user_id': u'1'}, u'status': u'processing', u'authorization_code': None, u'object': u'transaction', u'phone': {u'id': 13126, u'ddi': u'55', u'object': u'phone', u'number': u'30713261', u'ddd': u'11'}, u'referer': u'api_key', u'address': {u'city': u'S\xe3o Paulo', u'neighborhood': u'Jardim Paulistano', u'street_number': u'2941', u'complementary': u'8\xba andar', u'country': u'Brasil', u'object': u'address', u'zipcode': u'01452000', u'state': u'SP', u'street': u'Av. Brigadeiro Faria Lima', u'id': 13236}, u'status_reason': u'acquirer', u'subscription_id': None, u'card': {u'holder_name': u'Jose da Silva', u'valid': True, u'last_digits': u'4448', u'date_updated': u'2014-12-21T01:15:22.000Z', u'brand': u'visa', u'object': u'card', u'first_digits': u'490172', u'fingerprint': u'2KnrHzAFkjPE', u'date_created': u'2014-12-21T01:15:21.000Z', u'id': u'card_ci3xq3kyu0000yd16rihoplu6'}, u'soft_descriptor': u'Pagamento 1', u'customer': {u'name': u'John Appleseed', u'gender': None, u'document_number': u'92545278157', u'object': u'customer', u'id': 13683, u'born_at': None, u'date_created': u'2014-12-21T01:15:21.000Z', u'document_type': u'cpf', u'email': u'jappleseed@apple.com'}, u'amount': 10000, u'boleto_url': None, u'antifraud_score': None, u'installments': u'1', u'date_created': u'2014-12-23T20:05:02.000Z', u'acquirer_response_code': None, u'card_first_digits': u'490172'}


Uma boa dica é usar a lib python-dateutil para converter os formatos de data.

  >>> # pip install python-dateutil
  >>> from dateutil.parser import parse
  >>> parse(transaction.data['date_updated'])
  datetime.datetime(2014, 12, 23, 20, 5, 2, tzinfo=tzutc())

Você pode criar uma transação passando o card_id no lugar do card_hash.

  >>> transaction = Transaction(
  ...     amount='10000',
  ...     card_id='card_ci3xq3kyu0000yd16rihoplu6',
  ...     customer=customer,
  ...     metadata=metadata,
  ...     postback_url='http://requestb.in/18j98r31',
  ...     soft_descriptor='Pagamento 1'
  ... )
  >>> transaction.charge()
  >>> transaction.data
  {u'date_updated': u'2014-12-23T20:10:03.000Z', u'ip': u'179.179.108.26', u'boleto_barcode': None, u'cost': 0, u'refuse_reason': None, u'id': 173715, u'card_holder_name': u'Jose da Silva', u'postback_url': u'http://requestb.in/18j98r31', u'boleto_expiration_date': None, u'nsu': None, u'payment_method': u'credit_card', u'card_brand': u'visa', u'tid': None, u'card_last_digits': u'4448', u'metadata': {u'order_id': u'1', u'user_id': u'1'}, u'status': u'processing', u'authorization_code': None, u'object': u'transaction', u'phone': {u'id': 13126, u'ddi': u'55', u'object': u'phone', u'number': u'30713261', u'ddd': u'11'}, u'referer': u'api_key', u'address': {u'city': u'S\xe3o Paulo', u'neighborhood': u'Jardim Paulistano', u'street_number': u'2941', u'complementary': u'8\xba andar', u'country': u'Brasil', u'object': u'address', u'zipcode': u'01452000', u'state': u'SP', u'street': u'Av. Brigadeiro Faria Lima', u'id': 13236}, u'status_reason': u'acquirer', u'subscription_id': None, u'card': {u'holder_name': u'Jose da Silva', u'valid': True, u'last_digits': u'4448', u'date_updated': u'2014-12-21T01:15:22.000Z', u'brand': u'visa', u'object': u'card', u'first_digits': u'490172', u'fingerprint': u'2KnrHzAFkjPE', u'date_created': u'2014-12-21T01:15:21.000Z', u'id': u'card_ci3xq3kyu0000yd16rihoplu6'}, u'soft_descriptor': u'Pagamento 1', u'customer': {u'name': u'John Appleseed', u'gender': None, u'document_number': u'92545278157', u'object': u'customer', u'id': 13683, u'born_at': None, u'date_created': u'2014-12-21T01:15:21.000Z', u'document_type': u'cpf', u'email': u'jappleseed@apple.com'}, u'amount': 10000, u'boleto_url': None, u'antifraud_score': None, u'installments': u'1', u'date_created': u'2014-12-23T20:10:03.000Z', u'acquirer_response_code': None, u'card_first_digits': u'490172'}


Você pode optar por não passar o postback_url e ter o status final da transação (a requisição pode demorar um pouco).

  >>> transaction = Transaction(
  ...     amount='10000',
  ...     card_id='card_ci3xq3kyu0000yd16rihoplu6',
  ...     customer=customer,
  ...     metadata=metadata,
  ...     soft_descriptor='Pagamento 1'
  ... )
  >>> transaction.charge()
  >>> transaction.data
  {u'date_updated': u'2014-12-23T20:13:36.000Z', u'ip': u'179.179.108.26', u'boleto_barcode': None, u'cost': 260, u'refuse_reason': None, u'id': 173716, u'card_holder_name': u'Jose da Silva', u'postback_url': None, u'boleto_expiration_date': None, u'acquirer_name': u'development', u'nsu': u'1419365616183', u'payment_method': u'credit_card', u'card_brand': u'visa', u'tid': u'1419365616183', u'card_last_digits': u'4448', u'metadata': {u'order_id': u'1', u'user_id': u'1'}, u'status': u'paid', u'authorization_code': u'940334', u'object': u'transaction', u'phone': {u'id': 13126, u'ddi': u'55', u'object': u'phone', u'number': u'30713261', u'ddd': u'11'}, u'referer': u'api_key', u'address': {u'city': u'S\xe3o Paulo', u'neighborhood': u'Jardim Paulistano', u'street_number': u'2941', u'complementary': u'8\xba andar', u'country': u'Brasil', u'object': u'address', u'zipcode': u'01452000', u'state': u'SP', u'street': u'Av. Brigadeiro Faria Lima', u'id': 13236}, u'status_reason': u'acquirer', u'subscription_id': None, u'card': {u'holder_name': u'Jose da Silva', u'valid': True, u'last_digits': u'4448', u'date_updated': u'2014-12-21T01:15:22.000Z', u'brand': u'visa', u'object': u'card', u'first_digits': u'490172', u'fingerprint': u'2KnrHzAFkjPE', u'date_created': u'2014-12-21T01:15:21.000Z', u'id': u'card_ci3xq3kyu0000yd16rihoplu6'}, u'soft_descriptor': u'Pagamento 1', u'customer': {u'name': u'John Appleseed', u'gender': None, u'document_number': u'92545278157', u'object': u'customer', u'id': 13683, u'born_at': None, u'date_created': u'2014-12-21T01:15:21.000Z', u'document_type': u'cpf', u'email': u'jappleseed@apple.com'}, u'amount': 10000, u'boleto_url': None, u'antifraud_score': 52.67, u'installments': 1, u'date_created': u'2014-12-23T20:13:36.000Z', u'acquirer_response_code': u'00', u'card_first_digits': u'490172'}
  >>> transaction.data['status']
  u'paid'


===================================
Criando uma transação usando boleto
===================================

Para boleto, é interessante sempre usar o postback_url, para ser notificado quando o mesmo for pago.

  >>> transaction = Transaction(
  ...     amount='10000',
  ...     payment_method='boleto',
  ...     customer=customer,
  ...     metadata=metadata,
  ...     postback_url='http://requestb.in/18j98r31',
  ... )
  >>> transaction.charge()
  >>> transaction.data
  {u'date_updated': u'2014-12-23T20:19:56.000Z', u'ip': u'179.179.108.26', u'boleto_barcode': u'1234 5678', u'cost': 0, u'refuse_reason': None, u'id': 173718, u'card_holder_name': None, u'postback_url': u'http://requestb.in/18j98r31', u'boleto_expiration_date': u'2014-12-30T02:00:00.000Z', u'acquirer_name': u'development', u'nsu': None, u'payment_method': u'boleto', u'card_brand': None, u'tid': None, u'card_last_digits': None, u'metadata': {u'order_id': u'1', u'user_id': u'1'}, u'status': u'waiting_payment', u'authorization_code': None, u'object': u'transaction', u'phone': {u'id': 13126, u'ddi': u'55', u'object': u'phone', u'number': u'30713261', u'ddd': u'11'}, u'referer': u'api_key', u'address': {u'city': u'S\xe3o Paulo', u'neighborhood': u'Jardim Paulistano', u'street_number': u'2941', u'complementary': u'8\xba andar', u'country': u'Brasil', u'object': u'address', u'zipcode': u'01452000', u'state': u'SP', u'street': u'Av. Brigadeiro Faria Lima', u'id': 13236}, u'status_reason': u'acquirer', u'subscription_id': None, u'card': None, u'soft_descriptor': None, u'customer': {u'name': u'John Appleseed', u'gender': None, u'document_number': u'92545278157', u'object': u'customer', u'id': 13683, u'born_at': None, u'date_created': u'2014-12-21T01:15:21.000Z', u'document_type': u'cpf', u'email': u'jappleseed@apple.com'}, u'amount': 10000, u'boleto_url': u'https://pagar.me/', u'antifraud_score': None, u'installments': 1, u'date_created': u'2014-12-23T20:19:56.000Z', u'acquirer_response_code': None, u'card_first_digits': None}


=====================================
Consultando os dados de uma transação
=====================================

Para consultar os dados de uma transação, basta passar o id da mesma.

  >>> transaction = Transaction()
  >>> transaction.find_by_id(173715)
  >>> transaction.data
  {u'date_updated': u'2014-12-23T20:10:04.000Z', u'ip': u'179.179.108.26', u'boleto_barcode': None, u'cost': 260, u'refuse_reason': None, u'id': 173715, u'card_holder_name': u'Jose da Silva', u'postback_url': u'http://requestb.in/18j98r31', u'boleto_expiration_date': None, u'acquirer_name': u'development', u'nsu': 1419365403759, u'payment_method': u'credit_card', u'card_brand': u'visa', u'tid': 1419365403759, u'card_last_digits': u'4448', u'metadata': {u'order_id': u'1', u'user_id': u'1'}, u'status': u'paid', u'authorization_code': u'621741', u'object': u'transaction', u'phone': {u'id': 13126, u'ddi': u'55', u'object': u'phone', u'number': u'30713261', u'ddd': u'11'}, u'referer': u'api_key', u'address': {u'city': u'S\xe3o Paulo', u'neighborhood': u'Jardim Paulistano', u'street_number': u'2941', u'complementary': u'8\xba andar', u'country': u'Brasil', u'object': u'address', u'zipcode': u'01452000', u'state': u'SP', u'street': u'Av. Brigadeiro Faria Lima', u'id': 13236}, u'status_reason': u'acquirer', u'subscription_id': None, u'card': {u'holder_name': u'Jose da Silva', u'valid': True, u'last_digits': u'4448', u'date_updated': u'2014-12-21T01:15:22.000Z', u'brand': u'visa', u'object': u'card', u'first_digits': u'490172', u'fingerprint': u'2KnrHzAFkjPE', u'date_created': u'2014-12-21T01:15:21.000Z', u'id': u'card_ci3xq3kyu0000yd16rihoplu6'}, u'soft_descriptor': u'Pagamento 1', u'customer': {u'name': u'John Appleseed', u'gender': None, u'document_number': u'92545278157', u'object': u'customer', u'id': 13683, u'born_at': None, u'date_created': u'2014-12-21T01:15:21.000Z', u'document_type': u'cpf', u'email': u'jappleseed@apple.com'}, u'amount': 10000, u'boleto_url': None, u'antifraud_score': 11.04, u'installments': 1, u'date_created': u'2014-12-23T20:10:03.000Z', u'acquirer_response_code': u'00', u'card_first_digits': u'490172'}
