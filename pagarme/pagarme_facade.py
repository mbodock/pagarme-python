# encoding: utf-8

from six import with_metaclass

from .pagarme import Pagarme


class PagarmeInterceptor(type):
    """
    Intercepts all calls from PagarmeFacade
    """
    def __getattr__(cls, key):
        if cls.api_key is None:
            raise ValueError('Undefined api_key')
        if cls.pagarme is None:
            cls.pagarme = Pagarme(cls.api_key)
        cls.pagarme.api_key = cls.api_key
        return cls.pagarme.__getattribute__(key)


class PagarmeFacade(with_metaclass(PagarmeInterceptor)):
    api_key = None
    pagarme = None

    def __new__(self, api_key):
        return Pagarme(api_key=api_key)
