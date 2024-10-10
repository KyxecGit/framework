import logging

CHROME_OPTIONS = "--window-size=1920,1080"

DEFAULT_WAIT_TIME = 10

LOG_NAME = 'framework_logger'
LOG_FILE = 'framework.log'
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
ENCODING = 'utf-8'


SLIDER_URL = "https://the-internet.herokuapp.com/horizontal_slider"
CM_URL = "https://the-internet.herokuapp.com/context_menu"
ALERT_URL = "https://the-internet.herokuapp.com/javascript_alerts"
AUTH_URL = "https://{}:{}@the-internet.herokuapp.com/basic_auth"
CONTENT_URL = "https://the-internet.herokuapp.com/dynamic_content"
HANDLER_URL = "https://the-internet.herokuapp.com/windows"
HOVER_URL = "https://the-internet.herokuapp.com/hovers"
IFRAME_URL = "https://demoqa.com/alertsWindows"
SCROLL_URL = "https://the-internet.herokuapp.com/infinite_scroll"
IMAGE_URL = "https://the-internet.herokuapp.com/upload"