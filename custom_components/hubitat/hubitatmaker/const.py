from homeassistant.backports.enum import StrEnum


class DeviceCapability(StrEnum):
    ALARM = "Alarm"
    CARBON_DIOXIDE = "CarbonDioxideMeasurement"
    CARBON_MONOXIDE = "CarbonMonoxideDetector"
    COLOR_CONTROL = "ColorControl"
    COLOR_MODE = "ColorMode"
    COLOR_TEMP = "ColorTemperature"
    CONTACT_SENSOR = "ContactSensor"
    DOOR_CONTROL = "DoorControl"
    ENERGY_METER = "EnergyMeter"
    ENERGY_SOURCE = "EnergySource"
    GARAGE_DOOR_CONTROL = "GarageDoorControl"
    HOLDABLE_BUTTON = "HoldableButton"
    RELEASABLE_BUTTON = "ReleasableButton"
    ILLUMINANCE_MEASUREMENT = "IlluminanceMeasurement"
    LIGHT = "Light"
    LOCK = "Lock"
    LOCK_CODES = "LockCodes"
    MOTION_SENSOR = "MotionSensor"
    MUSIC_PLAYER = "MusicPlayer"
    POWER_METER = "PowerMeter"
    POWER_SOURCE = "PowerSource"
    PRESENCE_SENSOR = "PresenceSensor"
    PRESSURE_MEASUREMENT = "PressureMeasurement"
    PUSHABLE_BUTTON = "PushableButton"
    DOUBLE_TAPABLE_BUTTON = "DoubleTapableButton"
    RELATIVE_HUMIDITY_MEASUREMENT = "RelativeHumidityMeasurement"
    SECURITY_KEYPAD = "SecurityKeypad"
    SWITCH = "Switch"
    SWITCH_LEVEL = "SwitchLevel"
    TEMPERATURE_MEASUREMENT = "TemperatureMeasurement"
    THERMOSTAT = "Thermostat"
    WINDOW_SHADE = "WindowShade"
    WINDOW_BLIND = "WindowBlind"
    FAN_CONTROL = "FanControl"
    CURRENT_METER = "CurrentMeter"
    ACCELERATION_SENSOR = "AccelerationSensor"
    BATTERY = "Battery"
    BULB = "Bulb"
    CHIME = "Chime"
    INDICATOR = "Indicator"
    OUTLET = "Outlet"
    RELAY_SWITCH = "RelaySwitch"
    SHOCK_SENSOR = "ShockSensor"
    SIGNAL_STRENGTH = "SignalStrength"
    SLEEP_SENSOR = "SleepSensor"
    SMOKE_DETECTOR = "SmokeDetector"
    SOUND_PRESSURE_LEVEL = "SoundPressureLevel"
    SOUND_SENSOR = "SoundSensor"
    STEP_SENSOR = "StepSensor"
    TAMPER_ALERT = "TamperAlert"
    THERMOSTAT_COOLING_SETPOINT = "ThermostatCoolingSetpoint"
    THERMOSTAT_FAN_MODE = "ThermostatFanMode"
    THERMOSTAT_HEATING_SETPOINT = "ThermostatHeatingSetpoint"
    THERMOSTAT_SETPOINT = "ThermostatSetpoint"
    TIMED_SESSION = "TimedSession"
    TOUCH_SENSOR = "TouchSensor"
    UV = "UltravioletIndex"
    VALVE = "Valve"
    VIDEO_CAMERA = "VideoCamera"
    VOLTAGE_MEASUREMENT = "VoltageMeasurement"
    WATER_SENSOR = "WaterSensor"
    CONSUMABLE = "consumable"
    CHANGE_LEVEL = "ChangeLevel"
    LIGHT_EFFECTS = "LightEffects"
    MOMENTARY = "Momentary"
    SPEECH_SYNTHESIS = "SpeechSynthesis"
    GAS_DETECTOR = "GasDetector"
    AIR_QUALITY = "AirQuality"
    LIQUID_FLOW_RATE = "LiquidFlowRate"


class DeviceAttribute(StrEnum):
    ACCELERATION = "acceleration"
    ALARM = "alarm"
    AQI = "aqi"
    AIR_QUALITY_INDEX = "airQualityIndex"
    AMPERAGE = "amperage"
    BATTERY = "battery"
    CARBON_DIOXIDE = "carbonDioxide"
    CARBON_DIOXIDE_LEVEL = "carbonDioxide-Level"
    CARBON_MONOXIDE = "carbonMonoxide"
    CARBON_MONOXIDE_LEVEL = "carbonMonoxide-Level"
    CODE_CHANGED = "codeChanged"
    CODE_LENGTH = "codeLength"
    COLOR_MODE = "colorMode"
    COLOR_NAME = "colorName"
    COLOR_TEMP = "colorTemperature"
    CURRENT = "current"
    CONTACT = "contact"
    CUMULATIVE_LITER = "cumulative_liter"
    CUMULATIVE_CUBIC_METER = "cumulative_cubic_meter"
    DAY_EURO = "day_euro"
    DAY_LITER = "day_liter"
    DAY_CUBIC_METER = "day_cubic_meter"
    DOOR = "door"
    DOUBLE_TAPPED = "doubleTapped"
    DEW_POINT = "DewPoint"
    ENERGY = "energy"
    ENERGY_SOURCE = "energySource"
    ENTRY_DELAY = "entryDelay"
    EXIT_DELAY = "exitDelay"
    HELD = "held"
    HEAT_ALARM = "heatAlarm"
    HUE = "hue"
    HUMIDITY = "humidity"
    HOME_HEALTH = "HomeHealth"
    ILLUMINANCE = "illuminance"
    LAST_CODE_NAME = "lastCodeName"
    RAIN_RATE = "rainRate"
    RAIN_DAILY = "rainDaily"
    RATE = "rate"
    LEVEL = "level"
    LOCK = "lock"
    LOCK_CODES = "lockCodes"
    MAX_CODES = "maxCodes"
    MOTION = "motion"
    NAME = "name"
    NATURAL_GAS = "naturalGas"
    NUM_BUTTONS = "numberOfButtons"
    PM1 = "pm1"
    PM10 = "pm10"
    PM25 = "pm25"
    PH = "pH"
    POSITION = "position"
    POWER = "power"
    PRESENCE = "presence"
    PRESSURE = "pressure"
    POWER_SOURCE = "powerSource"
    PUSHED = "pushed"
    SATURATION = "saturation"
    SECURITY_KEYPAD = "securityKeypad"
    SMOKE = "smoke"
    SOUND = "sound"
    STEPS = "steps"
    SOUND_PRESSURE_LEVEL = "soundPressureLevel"
    GOAL = "goal"
    TEMPERATURE = "temperature"
    TAMPER = "tamper"
    TOUCH = "touch"
    UV = "ultravioletIndex"
    VALVE = "valve"
    VOLTAGE = "voltage"
    VOC = "VOC"
    VOC_LEVEL = "VOC-Level"
    WATER = "water"
    WINDOW_SHADE = "windowShade"
    WIND_DIRECTION = "windDirection"
    WIND_SPEED = "windSpeed"
    WIND_GUST = "windGust"
    SPEED = "speed"
    SHOCK = "shock"
    SWITCH = "switch"
    DIRECTION = "direction"
    SOUNDNUMBER = "soundnumber"
    SOUND_EFFECTS = "soundEffects"
    SOUND_NAME = "soundName"
    EFFECT_NUMBER = "effectnumber"
    EFFECT_NAME = "effectName"
    CLIP = "clip"
    HEATING_SETPOINT = "heatingSetpoint"
    COOLING_SETPOINT = "coolingSetpoint"
    THERMOSTAT_SETPOINT = "thermostatSetpoint"
    THERMOSTAT_MODE = "thermostatMode"
    THERMOSTAT_FAN_MODE = "thermostatFanMode"
    THERMOSTAT_OPERATING_STATE = "thermostatOperatingState"
    THERMOSTAT_SETPOINT_MODE = "thermostatSetpointMode"
    SCHEDULED_SETPOINT = "scheduledSetpoint"
    TIME_REMAINING = "timeRemaining"
    SESSION_STATUS = "sessionStatus"
    LQI = "lqi"
    RSSI = "rssi"
    SLEEPING = "sleeping"
    STATUS = "status"
    CONSUMABLE_STATUS = "consumableStatus"
    INDICATOR_STATUS = "indicatorStatus"
    POWERFACTOR = "powerFactor"
    RELEASED = "released"
    TILT = "tilt"


class DeviceCommand(StrEnum):
    ARM_AWAY = "armAway"
    ARM_HOME = "armHome"
    ARM_NIGHT = "armNight"
    AUTO = "auto"
    AWAY = "away"
    BOTH = "both"
    CLOSE = "close"
    COOL = "cool"
    DELETE_CODE = "deleteCode"
    DISARM = "disarm"
    ECO = "eco"
    EMERGENCY_HEAT = "emergencyHeat"
    FAN_AUTO = "fanAuto"
    FAN_CIRCULATE = "fanCirculate"
    FAN_ON = "fanOn"
    FLASH = "flash"
    GET_CODES = "getCodes"
    HEAT = "heat"
    LOCK = "lock"
    OFF = "off"
    ON = "on"
    OPEN = "open"
    PRESENT = "present"
    PUSH = "push"
    SET_CODE = "setCode"
    SET_CODE_LENGTH = "setCodeLength"
    SET_COLOR = "setColor"
    SET_COLOR_TEMP = "setColorTemperature"
    SET_ENTRY_DELAY = "setEntryDelay"
    SET_EXIT_DELAY = "setExitDelay"
    SET_HUE = "setHue"
    SET_LEVEL = "setLevel"
    SET_POSITION = "setPosition"
    SET_SAT = "setSaturation"
    SET_HEATING_SETPOINT = "setHeatingSetpoint"
    SET_COOLING_SETPOINT = "setCoolingSetpoint"
    SET_PRESENCE = "setPresence"
    SET_THERMOSTAT_MODE = "setThermostatMode"
    SET_FAN_MODE = "setThermostatFanMode"
    SIREN = "siren"
    STROBE = "strobe"
    UNLOCK = "unlock"
    SET_SPEED = "setSpeed"
    CYCLE_SPEED = "cycleSpeed"
    MUTE = "mute"
    START_LEVEL_CHANGE = "startLevelChange"
    STOP_LEVEL_CHANGE = "stopLevelChange"
    PLAY_SOUND = "playSound"
    STOP = "stop"
    INDICATOR_NEVER = "indicatorNever"
    INDICATOR_WHEN_OFF = "indicatorWhenOff"
    INDICATOR_WHEN_ON = "indicatorWhenOn"
    PHRASE_SPOKEN = "phraseSpoken"
    SPEAK = "speak"
    CAPTURE = "capture"


# See https://docs.hubitat.com/index.php?title=Hubitat®_Safety_Monitor_Interface
class HsmCommand(StrEnum):
    ARM_ALL = "armAll"
    ARM_AWAY = "armAway"
    ARM_HOME = "armHome"
    ARM_NIGHT = "armNight"
    ARM_RULES = "armRules"
    CANCEL_ALERTS = "cancelAlerts"
    DISARM = "disarm"
    DISARM_ALL = "disarmAll"
    DISARM_RULES = "disarmRules"


class HsmStatus(StrEnum):
    ARMED_AWAY = "armedAway"
    ARMING_AWAY = "armingAway"
    ARMED_HOME = "armedHome"
    ARMING_HOME = "armingHome"
    ARMED_NIGHT = "armedNight"
    ARMING_NIGHT = "armingNight"
    DISARMED = "disarmed"
    ALL_DISARMED = "allDisarmed"


class DeviceState(StrEnum):
    ARMED_AWAY = "armed away"
    ARMED_HOME = "armed home"
    ARMED_NIGHT = "armed night"
    CLOSED = "closed"
    CLOSING = "closing"
    DISARMED = "disarmed"
    LOCKED = "locked"
    LOW = "low"
    OFF = "off"
    ON = "on"
    OPEN = "open"
    OPENING = "opening"
    PARTIALLY_OPEN = "partially open"
    UNKNOWN = "unknown"
    UNLOCKED = "unlocked"
    UNLOCKED_WITH_TIMEOUT = "unlocked with timeout"
    TESTED = "tested"
    CLEAR = "clear"
    ACTIVE = "active"
    INACTIVE = "inactive"
    DETECTED = "detected"
    NOT_DETECTED = "not detected"


class ColorMode(StrEnum):
    RGB = "RGB"
    CT = "CT"


ID_MODE = "hub_mode"
ID_HSM_STATUS = "hub_hsm_status"

DEFAULT_FAN_SPEEDS = [
    "low",
    "medium-low",
    "medium",
    "medium-high",
    "high",
    "on",
    "off",
    "auto",
]
