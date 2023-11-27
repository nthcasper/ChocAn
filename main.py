from controllers.manager_controller import *
newObj = {'name': 'dober', 'Id': 234234234, 'address': 'lkj',
          'city': 'lkj', 'state': 'kj', 'zipcode': 98787}
manager = ManagerControl()
manager.editProvider(234234234, newObj)
