from vnpy.rpc import RpcServer
from vnpy.trader.engine import BaseEngine, MainEngine
from vnpy.trader.event import (
    EVENT_TICK,
    EVENT_ORDER,
    EVENT_TRADE,
    EVENT_POSITION,
    EVENT_ACCOUNT,
)
from vnpy.event import EventEngine, Event


APP_NAME = "RpcService"


class WebEngine(BaseEngine):
    """Web Services Engine"""

    def __init__(self, main_engine: MainEngine, event_engine: EventEngine) -> None:
        """"""
        super().__init__(main_engine, event_engine, APP_NAME)

        self.server: RpcServer = RpcServer()

        self.init_server()
        self.register_event()

    def init_server(self) -> None:
        """Initializing the RPC Server"""
        self.server.register(self.main_engine.connect)
        self.server.register(self.main_engine.subscribe)
        self.server.register(self.main_engine.send_order)
        self.server.register(self.main_engine.cancel_order)

        self.server.register(self.main_engine.get_contract)
        self.server.register(self.main_engine.get_order)
        self.server.register(self.main_engine.get_all_ticks)
        self.server.register(self.main_engine.get_all_orders)
        self.server.register(self.main_engine.get_all_trades)
        self.server.register(self.main_engine.get_all_positions)
        self.server.register(self.main_engine.get_all_accounts)
        self.server.register(self.main_engine.get_all_contracts)

    def start_server(
        self,
        rep_address: str,
        pub_address: str,
    ) -> None:
        """Starting the RPC server"""
        if self.server.is_active():
            return

        self.server.start(rep_address, pub_address)

    def register_event(self) -> None:
        """Registering event listeners"""
        self.event_engine.register(EVENT_TICK, self.process_event)
        self.event_engine.register(EVENT_TRADE, self.process_event)
        self.event_engine.register(EVENT_ORDER, self.process_event)
        self.event_engine.register(EVENT_POSITION, self.process_event)
        self.event_engine.register(EVENT_ACCOUNT, self.process_event)

    def process_event(self, event: Event) -> None:
        """Handling of events"""
        self.server.publish(event.type, event.data)

    def close(self):
        """Close the RPC server"""
        self.server.stop()
        self.server.join()
