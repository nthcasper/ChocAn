from controllers.manager_controller import *
data = BasicData()
manager = ManagerControl()
mydata = data.createBasicData()
manager.addProvider(mydata)
