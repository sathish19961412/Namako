from nameko.rpc import rpc

class Sathish:
      name="Greeting_Service"
      
      @rpc
      def hello(self,name):
          return "Hello,{}".format(name)