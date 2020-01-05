# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020, Yazılımcıların Mola Yeri (ymydepo)
#

from os import listdir, environ

prefix = "ymy+"

token = environ.get("TOKEN")

if token == None:
    token = "TOKEN"

# print(token)

cogs = [f"cogs.{i.split('.')[0]}" for i in listdir("./cogs") if i.endswith("py")][
    :-1
] + ["events"]

"""Yazılımcıların Mola Yeri için özel değişkenler. Değişkenler dinamik 
üretilecek şekilde olması için daha sonra bu kodlara el atılacak."""

owner_ids = [
    428273380844765185,
]

admin_ids = [
    428273380844765185,
    335119989893890049,
]

mod_ids = [
    429276634072350720,
    272372123316649984,
    340872679047561216,
    452619449158074368,
]

ymy_guild_id = 418887354699350028

"""Reaksiyon ile rol almak için kullanılan kanal ve mesaj değişkenleri."""

reaction_role_channel_id = 485084529443471390
reaction_role_message_ids = [
    626720184425644033,
    626720225215250433,
    626720265979822110,
    626720296631664640,
    626720397173325825,
    626720468136755200,
    626720493776404502,
    626720518720192585,
    626720542736777217,
]