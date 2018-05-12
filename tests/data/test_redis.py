import redis

con= redis.Redis(host='127.0.0.1',port=6379)

print(con)

con.set('zwb', {'1', '2'})

#con.delete("zhuang")

print(con.get("zwb"))

