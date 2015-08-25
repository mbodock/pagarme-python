# encoding: utf-8


class PygarmeApiError(Exception): pass


class PygarmeTransactionApiError(Exception): pass
class PygarmeTransactionError(Exception): pass
class NotPaidException(PygarmeTransactionError): pass
