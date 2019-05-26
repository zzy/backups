class Config:
    LOGO = """
                 ▄▄▄▄▄
        ▀▀▀██████▄▄▄       _______________
      ▄▄▄▄▄  █████████▄  /                 \\
     ▀▀▀▀█████▌ ▀▐▄ ▀▐█ |   Gotta go fast!  |
   ▀▀█████▄▄ ▀██████▄██ | _________________/
   ▀▄▄▄▄▄  ▀▀█▄▀█════█▀ |/
        ▀▀▀▄  ▀▀███ ▀       ▄▄
     ▄███▀▀██▄████████▄ ▄▀▀▀▀▀▀█▌
   ██▀▄▄▄██▀▄███▀ ▀▀████      ▄██
▄▀▀▀▄██▄▀▀▌████▒▒▒▒▒▒███     ▌▄▄▀
▌    ▐▀████▐███▒▒▒▒▒▐██▌
▀▄▄▄▄▀   ▀▀████▒▒▒▒▄██▀
          ▀▀█████████▀
        ▄▄██▀██████▀█
      ▄██▀     ▀▀▀  █
     ▄█             ▐▌
 ▄▄▄▄█▌              ▀█▄▄▄▄▀▀▄
▌     ▐                ▀▀▄▄▄▀
 ▀▀▄▄▀
"""
    REQUEST_MAX_SIZE = 100000000         # 100 megababies   允许最大请求数
    REQUEST_TIMEOUT = 60                 # 60 seconds   请求超时
    ROUTER_CACHE_SIZE = 1024             # 路由缓存最大数目, sanic.router.Router._get() 中引用