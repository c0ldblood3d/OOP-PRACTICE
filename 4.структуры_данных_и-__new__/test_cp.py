from ConnectionPool import ConnectionPools

connections = []

for i in range(1, 9):
    conn = ConnectionPools(f"conn_{i}")
    connections.append(conn)

print(f"Текущее количество соединений: {len(ConnectionPools._connections)}")

try:
    conn_9 = ConnectionPools("conn_9")
except RuntimeError as e:
    print(f"Поймано исключение: {e}")

print(f"Текущее количество соединений: {len(ConnectionPools._connections)}")

for i in range(4):
    if connections:
        conn = connections.pop(0)
        conn.release() 

print(f"Текущее количество соединений: {len(ConnectionPools._connections)}")

for i in range(9, 13):
    try:
        conn = ConnectionPools(f"conn_{i}")
        connections.append(conn)
    except RuntimeError as e:
        print(f"Ошибка при создании conn_{i}: {e}")

print(f"\nИтоговое количество соединений: {len(ConnectionPools._connections)}")
print("Список активных соединений:", [conn.id for conn in ConnectionPools._connections])
