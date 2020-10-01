from fastapi import FastAPI, Request, Response

app = FastAPI(openapi_url="/api/v1/debug_api/doc/openapi.json")

@app.get('/api/v1/debug_api/probe', 
    status_code=200)
async def probe():
    return {'staus': 'workong'}

@app.post('/api/v1/debug_api/debug', 
    status_code=200)
async def push(req: Request):
    for header in req.headers:
        print(f'{header}:{req.headers[header]}', flush=True)
    return {'staus': 'workong'}