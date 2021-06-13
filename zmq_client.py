from PyQt5.QtCore import QObject, QSocketNotifier, pyqtSignal, pyqtSlot, pyqtProperty
import zmq
from zmq_codec import ZmqCodecMixin
from google.protobuf.wrappers_pb2 import Int32Value
import pb2
import asyncio

class ZmqClient(QObject, ZmqCodecMixin):
    # STM32 signals
    notifyHeartbeat = pyqtSignal()
    notifyConfigStatus = pyqtSignal()

    # Match signals
    notifySide = pyqtSignal()
    notifyScore = pyqtSignal()
    notifyMatchTimer = pyqtSignal()
    notifyMatchState = pyqtSignal()
    
    # Odrive signals
    notifyODrive = pyqtSignal()
    
    # Sensors signals
    notifyTirette = pyqtSignal()
    notifyEmergencyStop = pyqtSignal()
    
    # Camera signals
    cameraFrameReceived = pyqtSignal(object)
    cameraDetectionsReceived = pyqtSignal(object)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._context = zmq.Context()
        
        self._sub_socket = self._context.socket(zmq.SUB)
        self._sub_socket.bind('tcp://*:3901')
        self._sub_socket.setsockopt(zmq.SUBSCRIBE,b'')
        
        self._pub_socket = self._context.socket(zmq.PUB)
        self._pub_socket.bind('tcp://*:3902')
        
        self._notifier = QSocketNotifier(self._sub_socket.getsockopt(zmq.FD), QSocketNotifier.Read, self)
        self._notifier.activated.connect(self._on_sub_socket_event)
        
        # STM variables
        self._heartbeat = 0
        self._config_status = 0

        # Match variables
        self._side = 0
        self._score = 0
        self._match_timer = 0
        self._match_state = 0

        # Odrive variables
        self._odrive_state = '00'
        self._odrive_error = False

        #Sensors variables
        self._tirette = False
        self._emergency_stop = False


        
    @pyqtSlot()
    def configNucleo(self):
        msg = Int32Value(value=0)
        self.publishTopic('gui/out/commands/config_nucleo', msg)
        
    @pyqtSlot()
    def preMatch(self):
        msg = Int32Value(value=0)
        self.publishTopic('gui/out/commands/prematch', msg)
        
    @pyqtSlot()
    def odriveCalibration(self):
        msg = Int32Value(value=0)
        self.publishTopic('nucleo/in/propulsion/calibrate_odrive', msg)
        
    def publishTopic(self, topic, msg):
        self._pub_socket.send_multipart(self._encodeTopic(topic, msg))
        
    def _on_sub_socket_event(self):        
        self._notifier.setEnabled(False)
        flags = self._sub_socket.getsockopt(zmq.EVENTS)
        while flags & zmq.POLLIN:
            topic, msg  = self._decodeTopic(self._sub_socket.recv_multipart())            
            self._on_message_received(topic, msg)
            flags = self._sub_socket.getsockopt(zmq.EVENTS)
        self._notifier.setEnabled(True)
        
    def _on_message_received(self, topic, msg):
        # STM messages
        if topic == 'gui/in/heartbeat':
            if(self._heartbeat > msg.timestamp):
                #If heartbeat in message is lower than current, then the nucleo has been reset
                #Reinit nucleo config status
                self._config_status = 0
                self.notifyConfigStatus.emit()
            self._heartbeat = msg.timestamp
            self.notifyHeartbeat.emit()
        if topic == 'gui/in/nucleo_config_status':
            self._config_status = msg.status + 1
            self.notifyConfigStatus.emit()
        if topic == 'gui/in/nucleo_reset':
            self._config_status = 0
            self.notifyConfigStatus.emit()

        # Match messages
        if topic == 'gui/in/side':
            self._side = msg.value
            self.notifySide.emit()
        if topic == 'gui/in/score':
            self._score = msg.value
            self.notifyScore.emit()
        if topic == 'gui/in/match_timer':
            self._match_timer = msg.value
            self.notifyMatchTimer.emit()
        if topic == 'gui/in/match_state':
            self._match_state = msg.value
            self.notifyMatchState.emit()

        # Odrive messages
        if topic == 'gui/in/odrive_state':
            self._odrive_state = msg.value
            self.notifyODrive.emit()
        if topic == 'gui/in/odrive_error':
            self._odrive_error = msg.value
            self.notifyODrive.emit()       

        # Sensors messages     
        if topic == 'gui/in/sensors/start_match':
            self._tirette = msg.value
            self.notifyTirette.emit()
        if topic == 'gui/in/sensors/emergency_stop':
            self._emergency_stop = msg.value
            self.notifyEmergencyStop.emit()

        # Camera messages
        if topic == 'gui/in/camera/image':
            self.cameraFrameReceived.emit(msg)
        if topic == 'gui/in/camera/detections':
            self.cameraDetectionsReceived.emit(msg)

    # STM properties
    @pyqtProperty(int, notify=notifyHeartbeat)
    def heartbeat(self):
        return self._heartbeat
    
    @pyqtProperty(int, notify=notifyConfigStatus)
    def config_status(self):
        return self._config_status

    # Match properties
    def setSide(self, side):
        self._side = side
        self.notifySide.emit()
        msg = Int32Value(value=side)
        self.publishTopic('gui/out/side', msg)

    @pyqtProperty(int, fset=setSide, notify=notifySide)
    def side(self):
        return self._side

    @pyqtProperty(int, notify=notifyScore)
    def score(self):
        return self._score

    @pyqtProperty(int, notify=notifyMatchTimer)
    def match_timer(self):
        return self._match_timer
        
    @pyqtProperty(int, notify=notifyMatchState)
    def match_state(self):
        return self._match_state

    # Odrive properties
    @pyqtProperty(str, notify=notifyODrive)
    def odrive_state(self):
        return self._odrive_state
    
    @pyqtProperty(bool, notify=notifyODrive)
    def odrive_error(self):
        return self._odrive_error
        
    # Sensors properties
    @pyqtProperty(bool, notify=notifyTirette)
    def tirette(self):
        return self._tirette
        
    @pyqtProperty(bool, notify=notifyEmergencyStop)
    def emergency_stop(self):
        return self._emergency_stop
        
