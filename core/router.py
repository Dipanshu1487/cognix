import json
import re
from core.brain import unified_brain_pipeline
from core.voice import stop_speaking
from core.response_engine import process_response

def route_command(command):
    """
    Main entry point for command routing.
    Rule: LoRA Primary, Gemini Fallback. No extra features.
    """
    raw_response = _raw_route_command(command)
    return process_response(raw_response)

def _raw_route_command(command):
    """
    Internal routing logic for cogniX.
    """
    command = command.lower().strip()
    
    # 1. Hardware Overrides (Bypasses AI for speed)
    if "stop" in command or "quiet" in command or "shut up" in command:
        stop_speaking()
        return "Stopping"

    # 2. Unified Brain Pipeline (LoRA -> Gemini)
    return unified_brain_pipeline(command)