class ProductNotFoundException(Exception):
    pass


class DuplicateSKUException(Exception):
    pass

class CustomerNotFoundException(Exception):
    pass


class DuplicateCustomerEmailException(Exception):
    pass


class InsufficientInventoryException(Exception):
    pass

class OrderNotFoundException(Exception):
    pass