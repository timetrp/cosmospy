from __future__ import annotations

import base64
import hashlib
import json
import grpc

import ecdsa
import requests

from cosmospy._typing import SyncMode
from cosmospy._wallet import DEFAULT_BECH32_HRP, privkey_to_address, privkey_to_pubkey
import cosmospy.interfaces.any_pb2 as Any
import cosmospy.interfaces.coin_pb2 as coin
import cosmospy.interfaces.msg_send_pb2 as transfer
import cosmospy.interfaces.pubkey_pb2 as pubkey
import cosmospy.interfaces.tx_pb2 as tx
import cosmospy.interfaces.tx_osmo_pb2 as tx_osmo
import cosmospy.interfaces.query_pb2 as query
import cosmospy.interfaces.pagination_pb2 as pagination

class Pool:
    """A Pool
    """

    def __init__(
        self,
        *,
        test: str = "test",
    ) -> None:
        self.test = test
        

    def allPools(self, url):
            msg = query.QueryPoolsRequest()
            page_req = pagination.PageRequest()
            page_req.key = b'0'
            page_req.offset = 1
            page_req.limit = 1
            page_req.count_total = True
            
            res = requests.post(url=url, data=pushable_tx)
            if res.status_code == 200:
                res = res.json()
                return res
            else:
                raise Exception(
                    "Broadcact failed to run by returning code of {}".format(res.status_code)
                )
                
    def add_swap_exact_amount_in(
        self, amount: int, amount_out_min: int, routes, denom: str = "uosmo", hrp: str = "osmo"
    ) -> None:
        msg = tx_osmo.MsgSwapExactAmountIn()
        msg.sender = privkey_to_address(self._privkey, hrp=hrp)
        for route in routes:
            _route = tx_osmo.SwapAmountInRoute()
            _route.poolId = int(route["pool_id"])
            _route.tokenOutDenom = route["denom"]
            msg.routes.append(_route)
        msg.tokenIn.denom = denom
        msg.tokenIn.amount = str(amount)
        msg.tokenOutMinAmount = str(amount)
        msg_any = Any.Any()
        msg_any.Pack(msg)
        msg_any.type_url = "/osmosis.gamm.v1beta1.MsgSwapExactAmountIn"
        self._tx_body.messages.append(msg_any)
        