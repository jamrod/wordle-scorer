#!/bin/bash
curl -d '{
  "test": "event",
  "body": {
    "fromAddress": "testAddress",
    "sender": "testSender", 
    "summary": "Wordle 566 4/6 ⬛⬛🟨🟩⬛ 🟩🟩⬛🟩⬛ 🟩🟩⬛🟩⬛ 🟩🟩🟩🟩🟩"
  }
}'   -H "Content-Type: application/json"   https://eowjom0tyh9us3e.m.pipedream.net

# context
# {15}
# Copy Path
# •
# Copy Value
# event
# {7}
# body
# {15}
# IntegIdList:
# 1672974978284110001,
# Mode:
# 0
# ccAddress:
# folderId:
# 8889120000000008000
# fromAddress:
# 3039109582@vtext.com
# html
# <div>Wordle 570 4/6*<br /><br />⬛🟩⬛⬛⬛<br />⬛🟩⬛🟨⬛<br />🟩🟩🟩⬛⬛<br />🟩🟩🟩🟩🟩<br />James</div>
# messageId:
# 1673407481698100000
# receivedTime:
# 1673407481692
# sender:
# 3039109582@vtext.com
# sentDateInGMT:
# 1673407481000
# size:
# 136
# subject
# Wordle 570 4/6* ⬛🟩⬛⬛⬛ ⬛??⬛🟨⬛ 🟩🟩🟩⬛⬛ 🟩🟩🟩🟩?...
# summary
# Wordle 570 4/6* ⬛🟩⬛⬛⬛ ⬛🟩⬛🟨⬛ 🟩🟩🟩⬛⬛ 🟩🟩🟩🟩🟩 James
# toAddress:
# <james@jamescrodgers.com>
# zuid:
# 754206862
# client_ip:
# 136.143.176.60
# headers
# {7}
# method:
# POST
# path:
# /
# query
# {0}
