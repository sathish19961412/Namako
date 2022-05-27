from Namako.service import Service

worker = Service()
worker.other_rpc = worker.other_rpc.get_dependency()
worker.method()
del worker
