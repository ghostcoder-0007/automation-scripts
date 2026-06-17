import time
import hashlib

def generate_session_id(username):
    """Generates a pseudo-random session identity for diagnostics."""
    current_time = str(time.time()).encode('utf-8')
    user_bytes = username.encode('utf-8')
    
    # Simple hash generation for tracking sessions
    session_hash = hashlib.sha256(user_bytes + current_time).hexdigest()
    return f"SESS-{session_hash[:12].upper()}"

def format_timestamp():
    """Returns standard log timestamp format."""
    return time.strftime("%Y-%m-%d %H:%M:%S")
