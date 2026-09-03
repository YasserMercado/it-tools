import os

def testNetUnix():
    aVariables = [
        "ifconfig | grep 'inet ' | grep -v '127.0.0.1'",
        "route -n get default | grep 'gateway'",
        "ping -c 4 www.google.com",
        "traceroute -n www.google.com"
    ]

    try:
        for i in aVariables:
            print(f"\n┌─ [START] ─────────────────────────────────")
            print(f"│ Running: {i}")
            print(f"└────────────────────────────────────────────")

            os.system(i)

            print(f"┌─ [COMPLETED] ─────────────────────────────")
            print(f"│ Status: Successfully finished")
            print(f"└────────────────────────────────────────────\n")
    except KeyboardInterrupt:
            print(f"\n [!] Execution interrupted by the user.")

testNetUnix()
