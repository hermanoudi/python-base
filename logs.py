#!/usr/bin/env python3

import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level )
#ch = logging.StreamHandler() # Console/terminal/sterr
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=100, # 10**6, 
    backupCount=10,
)
fh.setLevel(log_level)
# ch.setLevel(log_level)

fmt = logging.Formatter(
    '%(asctime)s    %(name)s    %(levelname)s   l:%(lineno)d    f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)

#log.addHandler(ch)
log.addHandler(fh)


"""
log.debug("Mensagem pro dev, qa, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execução")
log.critical("Erro geral ex: banco de dados sumiu")
"""
print("-" * 3)

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s, str(e)")