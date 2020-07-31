import time
from concurrent import futures
import sys
import os
sys.path.append("/root/go/src/github.com/jstang9527/grpc_demo")
from proto.python.arith_pb2 import ArithRequest, ArithResponse
from proto.python.arith_pb2_grpc import ArithServicer,add_ArithServicer_to_server,grpc

class Arither(ArithServicer):
    def XiangJia(self, request, context):
        return ArithResponse(result=request.num1+request.num2)
    def XiangJian(self,request,context):
        return ArithResponse(result=request.num1-request.num2)

def main():
    print("listen server on [::]:50051")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ArithServicer_to_server(Arither(), server)
    server.add_insecure_port("[::]:50051")
    server.start()

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        print("stop")
        server.stop(0)
main()