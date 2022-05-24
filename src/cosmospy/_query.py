import requests
import cosmospy.interfaces.query_pb2 as pb2
import cosmospy.interfaces.query_pb2_grpc as pb2_grpc
import grpc
class Query(object):
    def __init__(self):
        self.host = 'https://lcd-osmosis.keplr.app/osmosis/gamm/v1beta1/pools'
        # self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}'.format(self.host))

        # bind the client and the server
        self.stub = pb2_grpc.QueryStub(self.channel)

    def get_pools(self):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.QueryPoolsRequest()
        print(f'{message}')
        return self.stub.Pools(message)
