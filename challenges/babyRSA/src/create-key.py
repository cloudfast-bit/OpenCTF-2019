#!/usr/bin/env python2
from Crypto.PublicKey import RSA

n = long("""
4493337031664450212532848448292999765342668372801168420931212861076915
4698397608997456285895481964267343948928655411711877599248227535622678
8592414966201878463841861795149794699436166094617031680784723884870936
7466164236437630756613370944095603601302536890181272771950609626002026
1067117052338913680347738008923800411699319354882374527548189297445272
8311894906930933243468887118001102890140973982620128107774223288859401
9295664524955363701596407851836158155375807487553074581785955249083973
7328825208475609070912583026437562005987497251182614946273769392820462
37686926616489071067399114117393031141786969077513902381""".replace("\n",""))
e = 16L

key_params = (n, e)
pubkey = RSA.construct(key_params)
print pubkey.exportKey()
