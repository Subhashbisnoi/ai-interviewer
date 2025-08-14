#!/usr/bin/env python3
"""
Port availability checker for AI Interviewer
"""

import socket
import sys

def check_port(port, service_name):
    """Check if a port is available"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', port))
            print(f"✅ Port {port} is available for {service_name}")
            return True
    except OSError:
        print(f"❌ Port {port} is already in use for {service_name}")
        return False

def main():
    """Check all required ports"""
    print("🔍 Checking port availability for AI Interviewer...")
    print("=" * 50)
    
    ports_to_check = [
        (8000, "Backend API"),
        (3000, "Frontend React")
    ]
    
    all_available = True
    for port, service in ports_to_check:
        if not check_port(port, service):
            all_available = False
    
    print("=" * 50)
    if all_available:
        print("🎉 All ports are available! You can start the application.")
        print("\nTo start the application, run:")
        print("  ./start.sh")
    else:
        print("⚠️  Some ports are occupied. Please:")
        print("  1. Stop any services using these ports, or")
        print("  2. Modify the configuration to use different ports")
        print("\nCurrent configuration:")
        print("  Backend:  http://localhost:8000")
        print("  Frontend: http://localhost:3000")
    
    return all_available

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
