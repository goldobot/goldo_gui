from PyQt5.QtCore import QObject, QTimer, QSocketNotifier, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt5.QtQml import QQmlListProperty
import zmq
from zmq_codec import ZmqCodecMixin
from google.protobuf.wrappers_pb2 import Int32Value
import pb2 as _pb2
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()

from zmq.utils.monitor import recv_monitor_message

class RobotPose(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._x = 0
        self._y = 0
        self._yaw = 0

    @pyqtProperty(float)
    def x(self):
        return self._x

    @pyqtProperty(float)
    def y(self):
        return self._y

    @pyqtProperty(float)
    def yaw(self):
        return self._yaw

class RobotDetection(QObject):
    def __init__(self, cx, cy, cquality, parent=None):
        super().__init__(parent)
        self._x = cx
        self._y = cy
        self._quality = cquality

    @pyqtProperty(float, constant=True)
    def x(self):
        return self._x

    @pyqtProperty(float, constant=True)
    def y(self):
        return self._y

    @pyqtProperty(int, constant=True)
    def quality(self):
        return self._quality

    @pyqtProperty(int, constant=True)
    def axis(self):
        return self._axis

    @pyqtProperty(int, constant=True)
    def motor(self):
        return self._motor

    @pyqtProperty(int, constant=True)
    def controller(self):
        return self._controller

    @pyqtProperty(int, constant=True)
    def encoder(self):
        return self._encoder

    @pyqtProperty(int, constant=True)
    def sensorless(self):
        return self._sensorless

    @pyqtProperty(bool, constant=True)
    def is_in_error(self):
        return self._is_in_error

class ZmqClient(QObject, ZmqCodecMixin):
    # STM32 signals
    notifyHeartbeat = pyqtSignal()
    notifyConfigStatus = pyqtSignal()
    notifyNucleoResponding = pyqtSignal()

    # Match signals
    notifySide = pyqtSignal()
    notifyOpponentsNumber = pyqtSignal()
    notifyScore = pyqtSignal()
    notifyMatchTimer = pyqtSignal()
    notifyMatchState = pyqtSignal()

    # Odrive signals
    notifyODrive = pyqtSignal()

    # Sensors signals
    notifyTirette = pyqtSignal()
    notifyEmergencyStop = pyqtSignal()
    notifySensors = pyqtSignal()

    # Table signals
    notifyRobotPose = pyqtSignal()
    notifyRobotDetect = pyqtSignal()
    # RPLidar signals
    notifyRPLidar = pyqtSignal()

    # Camera signals
    cameraFrameReceived = pyqtSignal(object)
    cameraDetectionsReceived = pyqtSignal(object)
    # Others
    notifyScreenSelected = pyqtSignal()

    def _nucleo_watchdog(self):
        # If heartbeat changes, nucleo is responding
        if self._heartbeat != self._nucleo_watchdog_last_timestamp:
            self._nucleo_watchdog_last_timestamp = self._heartbeat
            self._nucleo_responding = True
        else:
            self._nucleo_responding = False
        self.notifyNucleoResponding.emit()
    def _send_side(self):
        msg = Int32Value(value=self._side)
        self.publishTopic('gui/out/side', msg)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._context = zmq.Context()

        # connect to the pub socket of goldo_main and set topic subscribe filter
        self._sub_socket = self._context.socket(zmq.SUB)
        self._sub_socket.connect('tcp://localhost:3801')
        self._sub_socket.setsockopt(zmq.SUBSCRIBE,b'gui/in/')

        # connect to the sub socket of goldo_main
        self._pub_socket = self._context.socket(zmq.PUB)
        self._pub_socket.connect('tcp://localhost:3802')

        # create notifier socket
        self._pub_monitor_socket = self._pub_socket.get_monitor_socket()

        self._notifier = QSocketNotifier(self._sub_socket.getsockopt(zmq.FD), QSocketNotifier.Read, self)
        self._notifier.activated.connect(self._on_sub_socket_event)

        self._notifier_monitor = QSocketNotifier(self._pub_monitor_socket.getsockopt(zmq.FD), QSocketNotifier.Read, self)
        self._notifier_monitor.activated.connect(self._on_monitor_socket_event)

        # STM variables
        self._heartbeat = 0
        self._config_status = 0
        self._nucleo_responding = False
        self._nucleo_watchdog_timer = QTimer(self)
        self._nucleo_watchdog_timer.timeout.connect(self._nucleo_watchdog)
        self._nucleo_watchdog_last_timestamp = 0

        # Match variables
        self._side = 0
        self._side_timer = QTimer(self)
        self._side_timer.timeout.connect(self._send_side)
        self._side_timer.start(1000)
        self._opponents_number = 1
        self._score = 0
        self._match_timer = 0
        self._match_state = 0

        # Odrive variables
        self._odrv_sync = False
        self._odrv_axis0_state = 0
        self._odrv_axis1_state = 0
        self._odrv_axis0_error = False
        self._odrv_axis1_error = False

        # Sensors variables
        self._tirette = False
        self._emergency_stop = True
        self._pavillon = True
        self._left_lift = False
        self._right_lift = False

        # RPLidar variables
        self._rplidar_running = False

        # Table variables
        self._robot_pose = RobotPose()
        self._robot_pose._x = 0.400
        self._robot_pose._y = -0.600
        self._robot_pose._yaw = 0.2
        self._robot_detection = []
        #Others
        self._gui_screen_selected = 0

    @pyqtSlot()
    def configNucleo(self):
        msg = Int32Value(value=0)
        self.publishTopic('gui/out/commands/config_nucleo', msg)

    @pyqtSlot()
    def preMatch(self):
        msg = _sym_db.GetSymbol('google.protobuf.Empty')()
        self.publishTopic('gui/out/commands/prematch', msg)

    @pyqtSlot()
    def odriveCalibration(self):
        msg = Int32Value(value=0)
        self.publishTopic('nucleo/in/propulsion/calibrate_odrive', msg)

    @pyqtSlot(int)
    def selectScreen(self, value):
        self._gui_screen_selected = value
        self.notifyScreenSelected.emit()

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

        flags = self._pub_monitor_socket.getsockopt(zmq.EVENTS)
        while flags & zmq.POLLIN:
            evt = recv_monitor_message(self._pub_monitor_socket)
            if evt['event'] == zmq.EVENT_CONNECTED:
                self._on_pub_client_connected()
            flags = self._pub_monitor_socket.getsockopt(zmq.EVENTS)

    def _on_monitor_socket_event(self):
        self._notifier_monitor.setEnabled(False)
        flags = self._pub_monitor_socket.getsockopt(zmq.EVENTS)
        while flags & zmq.POLLIN:
            evt = recv_monitor_message(self._pub_monitor_socket)
            if evt['event'] == zmq.EVENT_CONNECTED:
                self._on_pub_client_connected()
            flags = self._pub_monitor_socket.getsockopt(zmq.EVENTS)
        self._notifier_monitor.setEnabled(True)

    def _on_pub_client_connected(self):
        print('client connected')
        self.setSide(self.side)
        self.setOpponentsNumber(self.opponents_number)

    def _on_message_received(self, topic, msg):
        # State message
        print(topic)
        print(msg)
        if topic == 'gui/in/robot_state':
            #Nucleo
            if msg.nucleo.configured:
                if self._config_status != 1:
                    self._config_status = 1
                    if not self._nucleo_watchdog_timer.isActive():
                        self._nucleo_watchdog_timer.start(200)
                    self.notifyConfigStatus.emit()

            #Sensors
            self._tirette = msg.sensors["tirette"]
            self.notifyTirette.emit()
            self._emergency_stop = msg.sensors["emergency_stop"]
            self.notifyEmergencyStop.emit()
            self._pavillon = msg.sensors["switch_pavillon"]
            self._left_lift = msg.sensors["recalage_ascensceur_gauche"]
            self._right_lift = msg.sensors["recalage_ascensceur_droit"]
            self.notifySensors.emit()

            #RPLidar
            self._rplidar_running = msg.rplidar.running
            self.notifyRPLidar.emit()

            #Odrv
            self._odrv_sync = msg.nucleo.odrive.synchronized
            self._odrv_axis0_state = msg.nucleo.odrive.axis0.current_state
            self._odrv_axis1_state = msg.nucleo.odrive.axis1.current_state

            if msg.nucleo.odrive.axis0.errors.axis != 0:
                self._odrv_axis0_error = True
            elif msg.nucleo.odrive.axis0.errors.motor != 0:
                self._odrv_axis0_error = True
            elif msg.nucleo.odrive.axis0.errors.controller != 0:
                self._odrv_axis0_error = True
            elif msg.nucleo.odrive.axis0.errors.encoder != 0:
                self._odrv_axis0_error = True
            else:
                self._odrv_axis0_error = False

            if msg.nucleo.odrive.axis1.errors.axis != 0:
                self._odrv_axis1_error = True
            elif msg.nucleo.odrive.axis1.errors.motor != 0:
                self._odrv_axis1_error = True
            elif msg.nucleo.odrive.axis1.errors.controller != 0:
                self._odrv_axis1_error = True
            elif msg.nucleo.odrive.axis1.errors.encoder != 0:
                self._odrv_axis1_error = True
            else:
                self._odrv_axis1_error = False
            self.notifyODrive.emit()

            #Table
            self._robot_pose._x = msg.robot_pose.position.x
            self._robot_pose._y = msg.robot_pose.position.y
            self._robot_pose._yaw = msg.robot_pose.yaw
            self.notifyRobotPose.emit()
            #Match
            self._match_state = msg.match_state
            self.notifyMatchState.emit()
            if self._match_state == 4 :
                self._gui_screen_selected = 5
                self.notifyScreenSelected.emit()

            #Lidar detection
            self._robot_detection = []
            for detection in msg.rplidar_detections:
                _detect = RobotDetection(detection.x, detection.y, detection.detect_quality)
                self._robot_detection.append(_detect)
            self.notifyRobotDetect.emit()

        # STM messages
        if topic == 'gui/in/heartbeat':
            if(self._heartbeat > msg.timestamp):
                #If heartbeat in message is lower than current, then the nucleo has been reset
                #Reinit nucleo config status
                self._config_status = 0
                self._nucleo_watchdog_timer.stop()
                self.notifyConfigStatus.emit()
            self._heartbeat = msg.timestamp
            self.notifyHeartbeat.emit()
        if topic == 'gui/in/nucleo_config_status':
            self._config_status = msg.status + 1
            if self._config_status == 1:
                # Config is OK, run watchdog to monitor nucleo connection
                self._nucleo_watchdog_timer.start(200)
            self.notifyConfigStatus.emit()
        if topic == 'gui/in/nucleo_reset':
            self._config_status = 0
            self._nucleo_watchdog_timer.stop()
            self.notifyConfigStatus.emit()

        # Match messages
        if topic == 'gui/in/side':
            self._side = msg.value
            self.notifySide.emit()
        if topic == 'gui/in/opponents_number':
            self._opponents_number = msg.value
            self.notifyOpponentsNumber.emit()
        if topic == 'gui/in/score':
            self._score = msg.value
            self.notifyScore.emit()
        if topic == 'gui/in/match_timer':
            self._match_timer = msg.value
            self.notifyMatchTimer.emit()
            if self._match_state >= 2 :
                if self._match_timer < 5 :
                    self._gui_screen_selected = 5
                    self.notifyScreenSelected.emit()
        # Sensors messages
        if topic == 'gui/in/sensors/start_match':
            self._tirette = msg.value
            self.notifyTirette.emit()

        # Camera messages
        if topic == 'gui/in/camera/image':
            self.cameraFrameReceived.emit(msg)
        if topic == 'gui/in/camera/detections':
            self.cameraDetectionsReceived.emit(msg)

    # STM properties
    @pyqtProperty("unsigned long long", notify=notifyHeartbeat)
    def heartbeat(self):
        return self._heartbeat

    @pyqtProperty(int, notify=notifyConfigStatus)
    def config_status(self):
        return self._config_status

    @pyqtProperty(bool, notify=notifyNucleoResponding)
    def nucleo_responding(self):
        return self._nucleo_responding

    # Match properties
    def setSide(self, side):
        self._side = side
        self.notifySide.emit()
        msg = Int32Value(value=side)
        self.publishTopic('gui/out/side', msg)

    def setOpponentsNumber(self, opponents_number):
        self._opponents_number = opponents_number
        self.notifyOpponentsNumber.emit()
        msg = Int32Value(value=opponents_number)
        self.publishTopic('gui/out/opponents_number', msg)

    @pyqtProperty(int, fset=setSide, notify=notifySide)
    def side(self):
        return self._side

    @pyqtProperty(int, fset=setOpponentsNumber, notify=notifyOpponentsNumber)
    def opponents_number(self):
        return self._opponents_number

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
    @pyqtProperty(bool, notify=notifyODrive)
    def odrv_sync(self):
        return self._odrv_sync

    @pyqtProperty(int, notify=notifyODrive)
    def odrv_axis0_state(self):
        return self._odrv_axis0_state

    @pyqtProperty(int, notify=notifyODrive)
    def odrv_axis1_state(self):
        return self._odrv_axis1_state

    @pyqtProperty(bool, notify=notifyODrive)
    def odrv_axis0_error(self):
        return self._odrv_axis0_error

    @pyqtProperty(bool, notify=notifyODrive)
    def odrv_axis1_error(self):
        return self._odrv_axis1_error

    # Sensors properties
    @pyqtProperty(bool, notify=notifyTirette)
    def tirette(self):
        return self._tirette

    @pyqtProperty(bool, notify=notifyEmergencyStop)
    def emergency_stop(self):
        return self._emergency_stop

    @pyqtProperty(bool, notify=notifySensors)
    def pavillon(self):
        return self._pavillon
    @pyqtProperty(bool, notify=notifySensors)
    def left_lift(self):
        return self._left_lift

    @pyqtProperty(bool, notify=notifySensors)
    def right_lift(self):
        return self._right_lift

    @pyqtProperty(bool, notify=notifyRPLidar)
    def rplidar_running(self):
        return self._rplidar_running

     # Table properties
    @pyqtProperty(RobotPose, notify=notifyRobotPose)
    def robot_pose(self):
        return self._robot_pose

    @pyqtProperty(float, notify=notifyRobotPose)
    def robot_pose_x(self):
        return self._robot_pose.x

    @pyqtProperty(float, notify=notifyRobotPose)
    def robot_pose_y(self):
        return self._robot_pose.y

    @pyqtProperty(float, notify=notifyRobotPose)
    def robot_pose_yaw(self):
        return self._robot_pose.yaw

    @pyqtProperty(QQmlListProperty, notify=notifyRobotDetect)
    def robot_detection(self):
        return QQmlListProperty(RobotDetection, self, self._robot_detection)

    @pyqtProperty(RobotDetection, notify=notifyRobotDetect)
    def robot_detection1(self):
        return self._robot_detection[0]

    @pyqtProperty(RobotDetection, notify=notifyRobotDetect)
    def robot_detection2(self):
        return self._robot_detection[1]

    @pyqtProperty(RobotDetection, notify=notifyRobotDetect)
    def robot_detection3(self):
        return self._robot_detection[2]

    @pyqtProperty(int, notify=notifyScreenSelected)
    def gui_screen_selected(self):
        return self._gui_screen_selected
