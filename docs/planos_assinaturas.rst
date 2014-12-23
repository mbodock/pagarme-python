Planos e Assinaturas
====================

Antes de continuar, não esqueça de `checar a documentação do pagar.me <https://pagar.me/docs/plans-subscriptions/>`_.

Não esqueça de setar sua api_key.

=====================
Criando um novo plano
=====================

  >>> from pagarme.subscription import Plan
  >>> plan = Plan(
  ...     amount='10000',
  ...     days=30,
  ...     name='Meu Plano',
  ...     trial_days=10,
  ...     charges=10,
  ...     installments=1
  ... )
  >>> plan.create()
  >>> plan.data
  {u'name': u'Meu Plano', u'color': None, u'object': u'plan', u'days': 30, u'payment_methods': [u'boleto', u'credit_card'], u'charges': u'10', u'amount': 10000, u'installments': u'1', u'trial_days': 10, u'date_created': u'2014-12-23T20:55:07.000Z', u'id': 10849}


================================
Consultando os dados de um plano
================================

  >>> plan = Plan()
  >>> plan.find_by_id(10849)
  >>> plan.data
  {u'name': u'Meu Plano', u'color': None, u'object': u'plan', u'days': 30, u'payment_methods': [u'boleto', u'credit_card'], u'charges': u'10', u'amount': 10000, u'installments': u'1', u'trial_days': 10, u'date_created': u'2014-12-23T20:55:07.000Z', u'id': 10849}


============================================
Criando uma assinatura com cartão de crédito
============================================

Os passos para criação de uma nova assinatura são bem parecidos com o da transação, considere o card_hash e customer que foram usados nas transações para os próximos exemplos. Lembrando que para as assinaturas você pode usar o metadata da mesma forma.

Usando o card_hash.

  >>> subscription = Subscription(
  ...     plan_id=10849,
  ...     card_hash=card_hash,
  ...     customer=customer,
  ...     postback_url='http://requestb.in/y3jcvey3'
  ... )
  >>> subscription.create()
  >>> subscription.data
  {u'status': u'trialing', u'customer': {u'name': u'John Appleseed', u'gender': None, u'document_number': u'92545278157', u'object': u'customer', u'id': 13683, u'born_at': None, u'date_created': u'2014-12-21T01:15:21.000Z', u'document_type': u'cpf', u'email': u'jappleseed@apple.com'}, u'postback_url': u'http://requestb.in/y3jcvey3', u'phone': {u'id': 13126, u'ddi': u'55', u'object': u'phone', u'number': u'30713261', u'ddd': u'11'}, u'payment_method': u'credit_card', u'object': u'subscription', u'current_transaction': None, u'current_period_end': u'2015-01-02T21:04:18.555Z', u'current_period_start': u'2014-12-23T21:04:18.555Z', u'charges': 0, u'plan': {u'name': u'Meu Plano', u'color': None, u'object': u'plan', u'days': 30, u'payment_methods': [u'boleto', u'credit_card'], u'charges': 10, u'amount': 10000, u'installments': 1, u'trial_days': 10, u'date_created': u'2014-12-23T20:55:07.000Z', u'id': 10849}, u'card_brand': u'visa', u'address': {u'city': u'S\xe3o Paulo', u'neighborhood': u'Jardim Paulistano', u'street_number': u'2941', u'complementary': u'8\xba andar', u'country': u'Brasil', u'object': u'address', u'zipcode': u'01452000', u'state': u'SP', u'street': u'Av. Brigadeiro Faria Lima', u'id': 13236}, u'date_created': u'2014-12-23T21:04:18.000Z', u'card_last_digits': u'4448', u'id': 12241, u'card': {u'holder_name': u'Jose da Silva', u'valid': True, u'last_digits': u'4448', u'date_updated': u'2014-12-21T01:15:22.000Z', u'brand': u'visa', u'object': u'card', u'first_digits': u'490172', u'fingerprint': u'2KnrHzAFkjPE', u'date_created': u'2014-12-21T01:15:21.000Z', u'id': u'card_ci3xq3kyu0000yd16rihoplu6'}, u'metadata': None}

Agora usando o card_id.

  >>> subscription = Subscription(
  ...     plan_id=10849,
  ...     card_id='card_ci3xq3kyu0000yd16rihoplu6',
  ...     customer=customer,
  ...     postback_url='http://requestb.in/y3jcvey3'
  ... )
  >>> subscription.create()
  >>> subscription.data
  {u'status': u'trialing', u'customer': {u'name': u'John Appleseed', u'gender': None, u'document_number': u'92545278157', u'object': u'customer', u'id': 13683, u'born_at': None, u'date_created': u'2014-12-21T01:15:21.000Z', u'document_type': u'cpf', u'email': u'jappleseed@apple.com'}, u'postback_url': u'http://requestb.in/y3jcvey3', u'phone': {u'id': 13126, u'ddi': u'55', u'object': u'phone', u'number': u'30713261', u'ddd': u'11'}, u'payment_method': u'credit_card', u'object': u'subscription', u'current_transaction': None, u'current_period_end': u'2015-01-02T21:07:34.484Z', u'current_period_start': u'2014-12-23T21:07:34.484Z', u'charges': 0, u'plan': {u'name': u'Meu Plano', u'color': None, u'object': u'plan', u'days': 30, u'payment_methods': [u'boleto', u'credit_card'], u'charges': 10, u'amount': 10000, u'installments': 1, u'trial_days': 10, u'date_created': u'2014-12-23T20:55:07.000Z', u'id': 10849}, u'card_brand': u'visa', u'address': {u'city': u'S\xe3o Paulo', u'neighborhood': u'Jardim Paulistano', u'street_number': u'2941', u'complementary': u'8\xba andar', u'country': u'Brasil', u'object': u'address', u'zipcode': u'01452000', u'state': u'SP', u'street': u'Av. Brigadeiro Faria Lima', u'id': 13236}, u'date_created': u'2014-12-23T21:07:34.000Z', u'card_last_digits': u'4448', u'id': 12242, u'card': {u'holder_name': u'Jose da Silva', u'valid': True, u'last_digits': u'4448', u'date_updated': u'2014-12-21T01:15:22.000Z', u'brand': u'visa', u'object': u'card', u'first_digits': u'490172', u'fingerprint': u'2KnrHzAFkjPE', u'date_created': u'2014-12-21T01:15:21.000Z', u'id': u'card_ci3xq3kyu0000yd16rihoplu6'}, u'metadata': None}


=================================
Criando uma assinatura com boleto
=================================

Da mesma forma da transação, é uma boa prática sempre usar o postback_url para assinaturas com boleto.

  >>> subscription = Subscription(
  ...     plan_id=10849,
  ...     payment_method='boleto',
  ...     customer=customer,
  ...     postback_url='http://requestb.in/y3jcvey3'
  ... )
  >>> subscription.create()
  >>> subscription.data
  {u'status': u'trialing', u'customer': {u'name': u'John Appleseed', u'gender': None, u'document_number': u'92545278157', u'object': u'customer', u'id': 13683, u'born_at': None, u'date_created': u'2014-12-21T01:15:21.000Z', u'document_type': u'cpf', u'email': u'jappleseed@apple.com'}, u'postback_url': u'http://requestb.in/y3jcvey3', u'phone': {u'id': 13126, u'ddi': u'55', u'object': u'phone', u'number': u'30713261', u'ddd': u'11'}, u'payment_method': u'boleto', u'object': u'subscription', u'current_transaction': {u'date_updated': u'2014-12-23T21:10:13.000Z', u'ip': u'179.179.108.26', u'boleto_barcode': u'1234 5678', u'cost': 0, u'refuse_reason': None, u'id': 173719, u'card_holder_name': None, u'postback_url': None, u'boleto_expiration_date': u'2015-01-02T21:10:12.000Z', u'acquirer_name': u'development', u'nsu': None, u'payment_method': u'boleto', u'card_brand': None, u'tid': None, u'card_last_digits': None, u'metadata': {}, u'status': u'waiting_payment', u'authorization_code': None, u'object': u'transaction', u'referer': u'api_key', u'status_reason': u'acquirer', u'subscription_id': 12243, u'soft_descriptor': None, u'amount': 10000, u'boleto_url': u'https://pagar.me/', u'antifraud_score': None, u'installments': 1, u'date_created': u'2014-12-23T21:10:12.000Z', u'acquirer_response_code': None, u'card_first_digits': None}, u'current_period_end': u'2015-01-02T21:10:12.687Z', u'current_period_start': u'2014-12-23T21:10:12.687Z', u'charges': 0, u'plan': {u'name': u'Meu Plano', u'color': None, u'object': u'plan', u'days': 30, u'payment_methods': [u'boleto', u'credit_card'], u'charges': 10, u'amount': 10000, u'installments': 1, u'trial_days': 10, u'date_created': u'2014-12-23T20:55:07.000Z', u'id': 10849}, u'address': {u'city': u'S\xe3o Paulo', u'neighborhood': u'Jardim Paulistano', u'street_number': u'2941', u'complementary': u'8\xba andar', u'country': u'Brasil', u'object': u'address', u'zipcode': u'01452000', u'state': u'SP', u'street': u'Av. Brigadeiro Faria Lima', u'id': 13236}, u'date_created': u'2014-12-23T21:10:13.000Z', u'id': 12243, u'card': None, u'metadata': None}


===================================
Consultando dados de uma assinatura
===================================

  >>> subscription = Subscription()
  >>> subscription.find_by_id(12243)
  >>> subscription.data
  {u'status': u'trialing', u'customer': {u'name': u'John Appleseed', u'gender': None, u'document_number': u'92545278157', u'object': u'customer', u'id': 13683, u'born_at': None, u'date_created': u'2014-12-21T01:15:21.000Z', u'document_type': u'cpf', u'email': u'jappleseed@apple.com'}, u'postback_url': u'http://requestb.in/y3jcvey3', u'phone': {u'id': 13126, u'ddi': u'55', u'object': u'phone', u'number': u'30713261', u'ddd': u'11'}, u'payment_method': u'boleto', u'object': u'subscription', u'current_transaction': {u'date_updated': u'2014-12-23T21:10:13.000Z', u'ip': u'179.179.108.26', u'boleto_barcode': u'1234 5678', u'cost': 0, u'refuse_reason': None, u'id': 173719, u'card_holder_name': None, u'postback_url': None, u'boleto_expiration_date': u'2015-01-02T21:10:12.000Z', u'acquirer_name': u'development', u'nsu': None, u'payment_method': u'boleto', u'card_brand': None, u'tid': None, u'card_last_digits': None, u'metadata': {}, u'status': u'waiting_payment', u'authorization_code': None, u'object': u'transaction', u'referer': u'api_key', u'status_reason': u'acquirer', u'subscription_id': 12243, u'soft_descriptor': None, u'amount': 10000, u'boleto_url': u'https://pagar.me/', u'antifraud_score': None, u'installments': 1, u'date_created': u'2014-12-23T21:10:12.000Z', u'acquirer_response_code': None, u'card_first_digits': None}, u'current_period_end': u'2015-01-02T21:10:12.687Z', u'current_period_start': u'2014-12-23T21:10:12.687Z', u'charges': 0, u'plan': {u'name': u'Meu Plano', u'color': None, u'object': u'plan', u'days': 30, u'payment_methods': [u'boleto', u'credit_card'], u'charges': 10, u'amount': 10000, u'installments': 1, u'trial_days': 10, u'date_created': u'2014-12-23T20:55:07.000Z', u'id': 10849}, u'address': {u'city': u'S\xe3o Paulo', u'neighborhood': u'Jardim Paulistano', u'street_number': u'2941', u'complementary': u'8\xba andar', u'country': u'Brasil', u'object': u'address', u'zipcode': u'01452000', u'state': u'SP', u'street': u'Av. Brigadeiro Faria Lima', u'id': 13236}, u'date_created': u'2014-12-23T21:10:13.000Z', u'id': 12243, u'card': None, u'metadata': None}


=========================
Cancelando uma assinatura
=========================

  >>> subscription = Subscription()
  >>> subscription.find_by_id(12243)
  >>> subscription.cancel()
  >>> subscription.data
  {u'status': u'canceled', u'customer': {u'name': u'John Appleseed', u'gender': None, u'document_number': u'92545278157', u'object': u'customer', u'id': 13683, u'born_at': None, u'date_created': u'2014-12-21T01:15:21.000Z', u'document_type': u'cpf', u'email': u'jappleseed@apple.com'}, u'postback_url': u'http://requestb.in/y3jcvey3', u'phone': {u'id': 13126, u'ddi': u'55', u'object': u'phone', u'number': u'30713261', u'ddd': u'11'}, u'payment_method': u'boleto', u'object': u'subscription', u'current_transaction': {u'date_updated': u'2014-12-23T21:10:13.000Z', u'ip': u'179.179.108.26', u'boleto_barcode': u'1234 5678', u'cost': 0, u'refuse_reason': None, u'id': 173719, u'card_holder_name': None, u'postback_url': None, u'boleto_expiration_date': u'2015-01-02T21:10:12.000Z', u'acquirer_name': u'development', u'nsu': None, u'payment_method': u'boleto', u'card_brand': None, u'tid': None, u'card_last_digits': None, u'metadata': {}, u'status': u'waiting_payment', u'authorization_code': None, u'object': u'transaction', u'referer': u'api_key', u'status_reason': u'acquirer', u'subscription_id': 12243, u'soft_descriptor': None, u'amount': 10000, u'boleto_url': u'https://pagar.me/', u'antifraud_score': None, u'installments': 1, u'date_created': u'2014-12-23T21:10:12.000Z', u'acquirer_response_code': None, u'card_first_digits': None}, u'current_period_end': u'2015-01-02T21:10:12.000Z', u'current_period_start': u'2014-12-23T21:10:12.000Z', u'charges': 0, u'plan': {u'name': u'Meu Plano', u'color': None, u'object': u'plan', u'days': 30, u'payment_methods': [u'boleto', u'credit_card'], u'charges': 10, u'amount': 10000, u'installments': 1, u'trial_days': 10, u'date_created': u'2014-12-23T20:55:07.000Z', u'id': 10849}, u'card_brand': None, u'address': {u'city': u'S\xe3o Paulo', u'neighborhood': u'Jardim Paulistano', u'street_number': u'2941', u'complementary': u'8\xba andar', u'country': u'Brasil', u'object': u'address', u'zipcode': u'01452000', u'state': u'SP', u'street': u'Av. Brigadeiro Faria Lima', u'id': 13236}, u'date_created': u'2014-12-23T21:10:13.000Z', u'card_last_digits': None, u'id': 12243, u'card': None, u'metadata': None}
  >>> subscription.data['status']
  u'canceled'
