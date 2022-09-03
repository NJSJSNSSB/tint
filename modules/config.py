import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "11584900"))
API_HASH = getenv("API_HASH", "ec080989e5e6e009a4937b0788a08f91")
BOT_TOKEN = getenv("BOT_TOKEN", "5764675995:AAEG6jds-orVbXKxkyk2l0MvsSy5hgF0aR4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQAOaHzpHqa54vxeKxSb-C2ENW57ywgIzeYtmVBxo00gKiHpNLyzJYscdqZF9C2x5evfbulqKSVSeq-A1BJSZd0Yd5ly2XuvPXBPM9OoRLUGjXeo9_DyaqiX1UdIvAJvyfUWjIGMQHOvuioDDlukEJyBLzAVYeDTt_pBL0xBHSBktqkZbM--j6hhjOZMwSwL8nxw-gf2Mig4ZPtYHJgEcJ9Fjx_ozXpmlMQ2H-gMdbHxIGDU17P95WYoad-gF9o1okzBI07sBAfuq8iJ6FMHzUHHTAjLys4Qdyx8PABABl28_8BR9_o6FoVZGOScbzjPsEN4lEHBZresHn7KqlfUXOPEAAAAAT4KBv0A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
