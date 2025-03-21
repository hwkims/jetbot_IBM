import asyncio
import websockets
import json
import logging
from jetbot import Robot, Camera, bgr8_to_jpeg
import base64

# --- OpenCV Handling ---
try:
    import cv2
    OPENCV_AVAILABLE = True
except ImportError:
    cv2 = None
    OPENCV_AVAILABLE = False

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Configuration ---
WEBSOCKET_PORT = 8766
CAMERA_WIDTH = 300
CAMERA_HEIGHT = 300
FPS = 20

# --- JetBot Initialization ---
try:
    robot = Robot()
    camera = Camera.instance(width=CAMERA_WIDTH, height=CAMERA_HEIGHT)
    logger.info("JetBot initialized successfully.")
except Exception as e:
    logger.error(f"JetBot initialization failed: {e}")
    robot = None
    camera = None

# --- Command Handling ---
async def handle_command(command, parameters=None):
    parameters = parameters or {}
    if not robot:
        logger.error("Robot not initialized.")
        return
    try:
        duration = parameters.get("duration", 1.0)
        speed = parameters.get("speed", 0.4)
        if command == "forward":
            robot.forward(speed)
            await asyncio.sleep(duration)
        elif command == "backward":
            robot.backward(speed)
            await asyncio.sleep(duration)
        elif command == "left":
            robot.left(speed)
            await asyncio.sleep(duration)
        elif command == "right":
            robot.right(speed)
            await asyncio.sleep(duration)
        elif command == "stop":
            robot.stop()
        elif command == "dance":
            # Dance sequence
            for _ in range(2):
                robot.left(0.5)
                await asyncio.sleep(0.5)
                robot.right(0.5)
                await asyncio.sleep(0.5)
                robot.forward(0.5)
                await asyncio.sleep(0.5)
                robot.backward(0.5)
                await asyncio.sleep(0.5)
            robot.stop()
        else:
            # Handle custom or unrecognized commands dynamically
            logger.info(f"Custom command received: {command}")
            if "spin" in command.lower():  # Example custom interpretation
                robot.right(0.5)
                await asyncio.sleep(duration * 2)
            elif "circle" in command.lower():
                robot.left(0.5)
                await asyncio.sleep(duration * 2)
            robot.stop()
    except Exception as e:
        logger.error(f"Command execution error: {e}")
        robot.stop()

# --- WebSocket Handler ---
async def websocket_handler(websocket, path):
    logger.info("WebSocket connection established")

    async def send_image_stream():
        if not camera:
            logger.error("Camera not available.")
            return
        try:
            while True:
                frame = camera.value
                if frame is None:
                    logger.warning("No frame from camera.")
                    await asyncio.sleep(1 / FPS)
                    continue
                if OPENCV_AVAILABLE:
                    _, encoded_image = cv2.imencode('.jpg', frame)
                    if encoded_image is None:
                        logger.error("Failed to encode image with OpenCV.")
                        await asyncio.sleep(1 / FPS)
                        continue
                    image_base64 = base64.b64encode(encoded_image).decode('utf-8')
                else:
                    image_base64 = base64.b64encode(bgr8_to_jpeg(frame)).decode('utf-8')
                await websocket.send(json.dumps({"image": image_base64}))
                await asyncio.sleep(1 / FPS)
        except Exception as e:
            logger.error(f"Image stream error: {str(e)}")

    image_stream_task = asyncio.ensure_future(send_image_stream())
    try:
        async for message in websocket:
            data = json.loads(message)
            command = data.get("command", "none")
            parameters = data.get("parameters", {})
            await handle_command(command, parameters)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        image_stream_task.cancel()
        if robot:
            robot.stop()

# --- Main Function ---
async def main():
    while True:
        try:
            server = await websockets.serve(websocket_handler, "0.0.0.0", WEBSOCKET_PORT)
            logger.info(f"WebSocket server running on port {WEBSOCKET_PORT}")
            await asyncio.Future()
        except Exception as e:
            logger.error(f"Server error: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    if robot:
        robot.stop()
    asyncio.get_event_loop().run_until_complete(main())
