from http.server import BaseHTTPRequestHandler
import json, os, http.client

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        try:
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))
            api_key = os.environ.get("GROQ_API_KEY", "")

            payload = json.dumps({
                "model": "llama-3.3-70b-versatile",
                "messages": body.get("messages", []),
                "max_tokens": 1000
            })

            conn = http.client.HTTPSConnection("api.groq.com")
            conn.request("POST", "/openai/v1/chat/completions", payload, {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            })

            res = conn.getresponse()
            data = json.loads(res.read().decode())
            reply = data["choices"][0]["message"]["content"]

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"reply": reply}).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"reply": f"Error: {str(e)}"}).encode())
