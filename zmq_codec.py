import google.protobuf as _pb

class ZmqCodecMixin:    
    def __init__(self):
        self._sym_db = _pb.symbol_database.Default()

    def _encodeTopic(self, topic, msg):
        return [topic.encode('utf8'),
                msg.DESCRIPTOR.full_name.encode('utf8'),
                msg.SerializeToString()]
                
    def _decodeTopic(self, tup):
        topic, full_name, payload  = tup
        topic = topic.decode('utf8')
        full_name = full_name.decode('utf8')
        msg_class = self._sym_db.GetSymbol(full_name)
        if msg_class is not None:
            msg = msg_class()
            msg.ParseFromString(payload)
        else:
            msg = None
        return topic, msg