import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title="Calendar",
    openapi_url="/calendar/openapi.json",
    docs_url="/calendar/docs",
)

if __name__ == "__main__":
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
           
            reload=True,
            forwarded_allow_ips="*",
            proxy_headers=True,
        )
      
          